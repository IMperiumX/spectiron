import dataclasses
from typing import Dict, Type, TypeVar, _GenericAlias

import marshmallow

from openapi_specgen.marshmallow_schema import get_openapi_schema_from_mashmallow_schema

from .constants import *

get_schema = lambda data_type: {
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


def _get_openapi_array_schema(array_type: Type, item_type=None) -> Dict:
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


def _get_openapi_schema_from_dataclass(data_type: Type) -> dict:
    """Returns a dict representing the openapi schema of the dataclass data_type.

    Assumes all fields declared by this dataclass are required.

    Args:
        data_type (type): Any dataclass

    Returns:
        dict: A dict representing this dataclass as a openapi schema
    """
    openapi_schema = get_schema(data_type)

    for field in dataclasses.fields(data_type):
        if get_type(field.type) == "object":
            openapi_schema.update(get_openapi_schema(field.type, reference=False))
    return openapi_schema


def get_openapi_schema(data_type: Type, reference=True) -> Dict:
    openapi_type = get_type(data_type, OPENAPI_DEFAULT_TYPE)
    print(openapi_type)
    if reference:
        return {"$ref": f"#/components/schemas/{data_type.__name__}"}
    if issubclass(data_type, marshmallow.Schema):
        return get_openapi_schema_from_mashmallow_schema(data_type, reference=reference)
    if dataclasses.is_dataclass(data_type):
        return _get_openapi_schema_from_dataclass(data_type)
    if openapi_type == "array":
        return _get_openapi_array_schema(data_type)
    return {"type": openapi_type}
