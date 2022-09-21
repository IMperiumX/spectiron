import dataclasses
from datetime import date, datetime
from typing import Dict, List, Type, TypeVar, _GenericAlias

import marshmallow

from openapi_specgen.marshmallow_schema import get_openapi_schema_from_mashmallow_schema

OPENAPI_DEFAULT_TYPE = "object"


OPENAPI_TYPE_MAP = {
    str: "string",
    date: "string",
    datetime: "string",
    float: "number",
    int: "integer",
    bool: "boolean",
    List: "array",
}

OPENAPI_FORMAT_MAP = {
    date: "date",
    datetime: "date-time",
}

OPENAPI_ARRAY_ITEM_MAP = {
    List[str]: "string",
    List[float]: "number",
    List[int]: "integer",
    List[bool]: "boolean",
    List: None,
}

get_type = OPENAPI_TYPE_MAP.get
get_format = OPENAPI_FORMAT_MAP.get
get_list_generic_type = OPENAPI_ARRAY_ITEM_MAP.get


def get_openapi_array_schema(array_type: Type) -> Dict:
    openapi_array_type = get_list_generic_type(array_type)

    if isinstance(openapi_array_type, _GenericAlias):
        item_type = array_type.__args__[0]

    if item_type is None or isinstance(item_type, TypeVar):
        return {
            "type": "array",
            "items": {},
        }
    return {
        "type": "array",
        "items": {"type": get_openapi_schema(item_type)},
    }


def get_openapi_schema(data_type: Type, reference=True) -> Dict:
    openapi_type = get_type(data_type, OPENAPI_DEFAULT_TYPE)
    if openapi_type == OPENAPI_DEFAULT_TYPE:
        if issubclass(data_type, marshmallow.Schema):
            return get_openapi_schema_from_mashmallow_schema(
                data_type, reference=reference
            )
        if reference:
            return {"$ref": f"#/components/schemas/{data_type.__name__}"}
        if dataclasses.is_dataclass(data_type):
            return get_openapi_schema_from_dataclass(data_type)
        openapi_schema = {
            data_type.__name__: {
                "title": data_type.__name__,
                "required": [field.name for field in dataclasses.fields(data_type)],
                "type": OPENAPI_DEFAULT_TYPE,
                # DictComp, Iterating over fields type in dataclass Obj
                "properties": {
                    field.name: get_openapi_schema(field.type)
                    for field in dataclasses.fields(data_type)
                },
            }
        }

    for field in dataclasses.fields(data_type):
        if get_type(field.type) == "object":
            openapi_schema.update(get_openapi_schema(field.type, reference=True))
        return openapi_schema

    if openapi_type == "array":
        return get_openapi_array_schema(data_type)
    return {"type": openapi_type}


def get_openapi_schema_from_dataclass(data_type: type) -> dict:
    """Returns a dict representing the openapi schema of the dataclass data_type.

    Assumes all fields declared by this dataclass are required.

    Args:
        data_type (type): Any dataclass

    Returns:
        dict: A dict representing this dataclass as a openapi schema
    """
    openapi_schema = {
        data_type.__name__: {
            "title": data_type.__name__,
            "required": [field.name for field in dataclasses.fields(data_type)],
            "type": "object",
            "properties": {
                field.name: get_openapi_schema(field.type)
                for field in dataclasses.fields(data_type)
            },
        }
    }
    for field in dataclasses.fields(data_type):
        if get_type(field.type) == "object":
            openapi_schema.update(get_openapi_schema(field.type, reference=False))
    return openapi_schema
