from dataclasses import fields
from typing import List, Type

OPENAPI_DEFAULT_TYPE = "object"


OPENAPI_TYPE_MAP = {
    str: "string",
    float: "number",
    int: "integer",
    bool: "boolean",
    List: "array",
    List[str]: "array",
    List[float]: "array",
    List[int]: "array",
    List[bool]: "array",
}

get_type = OPENAPI_TYPE_MAP.get

OPENAPI_ARRAY_ITEM_MAP = {
    List[str]: "string",
    List[float]: "number",
    List[int]: "integer",
    List[bool]: "boolean",
    List: None,
}

get_list_generic_type = OPENAPI_ARRAY_ITEM_MAP.get



def get_openapi_array_schema(array_type: Type) -> dict:
    openapi_array_type = get_list_generic_type(array_type)
    if openapi_array_type is None:
        return {"type": "array", "items": {}}
    return {"type": "array", "items": {"type": openapi_array_type}}


def get_openapi_schema(data_type: Type, reference=False) -> dict:
    openapi_type = get_type(data_type, OPENAPI_DEFAULT_TYPE)
    if openapi_type == OPENAPI_DEFAULT_TYPE:
        if reference:
            return {"$ref": f"#/components/schemas/{data_type.__name__}"}
        openapi_schema =  {
            data_type.__name__: {
                "title": data_type.__name__,
                "required": [field.name for field in fields(data_type)],
                "type": OPENAPI_DEFAULT_TYPE,
                # DictComp, Iterating over fields type in dataclass Obj
                "properties": {
                    field.name: get_openapi_schema(field.type) for field in fields(data_type),
            }
        }
        }
        
    for field in fields(data_type):
        if get_type(field.type) == 'object':
            openapi_schema.update(get_openapi_schema(field.type, reference=False))
    return openapi_schema

    if openapi_type == "array":
        return get_openapi_array_schema(data_type)
    return {"type": openapi_type}
