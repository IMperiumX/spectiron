from dataclasses import fields

from .consants import *


def get_openapi_type(data_type: type) -> str:
    return OPENAPI_TYPE_MAP.get(data_type, OPENAPI_DEFAULT_TYPE)


def get_openapi_list_generic_type(data_type: type) -> str:
    return OPENAPI_ARRAY_ITEM_MAP.get(data_type)


def get_openapi_array_schema(array_type: type) -> dict:
    openapi_array_type = get_openapi_list_generic_type(array_type)
    if openapi_array_type is None:
        return {
            'type': 'array',
            'items': {}
        }
    return {
        'type': 'array',
        'items': {
            'type': openapi_array_type
        }
    }


def get_openapi_schema(data_type: type, reference=True) -> dict:
    openapi_type = get_openapi_type(data_type)
    if openapi_type == 'object':
        if reference:
            return {
                '$ref': f'#/components/schemas/{data_type.__name__}'
            }
        return {
            data_type.__name__: {
                'title': data_type.__name__,
                'required': [field.name for field in fields(data_type)],
                'type': 'object',
                'properties': {
                    field.name: {
                        'title': field.name.title(),
                        'type': get_openapi_type(field.type)
                    } for field in fields(data_type)
                }
            }
        }
    if openapi_type == 'array':
        return get_openapi_array_schema(data_type)
    return {'type': openapi_type}
