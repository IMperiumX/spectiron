from typing import List

import pytest

from specitron.schema import get_openapi_schema

from .utils import DataclassNestedObject, DataclassObject


@pytest.mark.parametrize(
    "data_type, openapi_schema",
    [
        (str, {"type": "string"}),
        (int, {"type": "integer"}),
        (float, {"type": "number"}),
        (bool, {"type": "boolean"}),
        (list, {"type": "array", "items": {}}),
        (list[str], {"type": "array", "items": {"type": "string"}}),
        (list[int], {"type": "array", "items": {"type": "integer"}}),
        (list[float], {"type": "array", "items": {"type": "number"}}),
        (list[bool], {"type": "array", "items": {"type": "boolean"}}),
    ],
)
def test_openapi_schema(data_type, openapi_schema):
    assert openapi_schema == get_openapi_schema(data_type)


def test_dataclass_schema():
    expected_openapi_schema = {
        "DataclassObject": {
            "title": "DataclassObject",
            "type": "object",
            "required": [
                "str_field",
                "int_field",
                "float_field",
                "boolean_field",
                "list_field",
            ],
            "properties": {
                "str_field": {"type": "string"},
                "int_field": {"type": "integer"},
                "float_field": {"type": "number"},
                "boolean_field": {"type": "boolean"},
                "list_field": {"type": "array", "items": {}},
            },
        }
    }
    assert expected_openapi_schema == get_openapi_schema(
        DataclassObject,
    )


def test_nested_objects():
    expected_openapi_schema = {
        "DataclassNestedObject": {
            "title": "DataclassNestedObject",
            "required": ["str_field", "nested_object"],
            "type": "object",
            "properties": {
                "str_field": {"type": "string"},
                "nested_object": {
                    "DataclassObject": {
                        "title": "DataclassObject",
                        "required": [
                            "str_field",
                            "int_field",
                            "float_field",
                            "boolean_field",
                            "list_field",
                        ],
                        "type": "object",
                        "properties": {
                            "str_field": {"type": "string"},
                            "int_field": {"type": "integer"},
                            "float_field": {"type": "number"},
                            "boolean_field": {"type": "boolean"},
                            "list_field": {"type": "array", "items": {}},
                        },
                    }
                },
            },
        }
    }
    assert expected_openapi_schema == get_openapi_schema(
        DataclassNestedObject,
    )
