import dataclasses
from typing import TypeVar

import marshmallow

from openapi_specgen.marshmallow_schema import get_openapi_schema_from_mashmallow_schema

from .constants import (
    OPENAPI_ARRAY_ITEM_MAP,
    OPENAPI_DEFAULT_TYPE,
    get_list_generic,
    get_type,
)

get_schema = lambda data_type: {
    data_type.__name__: {
        "title": data_type.__name__,
        "required": [field.name for field in dataclasses.fields(data_type)],
        "type": OPENAPI_DEFAULT_TYPE,
        "properties": {
            field.name: get_openapi_schema(field.type)
            for field in dataclasses.fields(data_type)
        },
    }
}


def _get_openapi_array_schema(array_type: type, item_type=None) -> dict:
    if get_list_generic(array_type) is None or isinstance(array_type, TypeVar):
        return {
            "type": "array",
            "items": {},
        }
    return {
        "type": "array",
        "items": {"type": get_list_generic(array_type)},
    }


def _get_openapi_schema_from_dataclass(data_type: type) -> dict:
    """Returns a dict representing the openapi schema of the dataclass data_type.

    Assumes all fields declared by this dataclass are required.

    Args:
        data_type (type): Any dataclass

    Returns:
        dict: A dict representing this dataclass as a openapi schema
    """
    openapi_schema = get_schema(data_type)

    for field in dataclasses.fields(data_type):
        if get_type(field.type) == OPENAPI_DEFAULT_TYPE:
            openapi_schema.update(get_openapi_schema(field.type))
    return openapi_schema


def get_openapi_schema(data_type: type, reference=False) -> dict:
    openapi_type = get_type(data_type, OPENAPI_DEFAULT_TYPE)
    if reference:
        return {"$ref": f"#/components/schemas/{data_type.__name__}"}
    if issubclass(data_type, marshmallow.Schema):
        return get_openapi_schema_from_mashmallow_schema(data_type, reference=reference)
    if dataclasses.is_dataclass(data_type):
        return _get_openapi_schema_from_dataclass(data_type)
    if data_type in OPENAPI_ARRAY_ITEM_MAP.keys():
        return _get_openapi_array_schema(data_type)
    return {"type": openapi_type}
