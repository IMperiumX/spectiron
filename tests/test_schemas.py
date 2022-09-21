from typing import List

import pytest

from openapi_specgen.schema import get_openapi_schema

from .utils import DataclassNestedObject, DataclassObject


@pytest.mark.parametrize(
    "data_type, openapi_schema",
    [
        (str, {"type": "string"}),
        (int, {"type": "integer"}),
        (float, {"type": "number"}),
        (bool, {"type": "boolean"}),
        (List, {"type": "array", "items": {}}),
        (List[str], {"type": "array", "items": {"type": "string"}}),
        (List[int], {"type": "array", "items": {"type": "integer"}}),
        (List[float], {"type": "array", "items": {"type": "number"}}),
        (List[bool], {"type": "array", "items": {"type": "boolean"}}),
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
        DataclassObject, reference=False
    )


def test_nested_objects():
    expected_openapi_schema = {
        "DataclassNestedObject": {
            "title": "DataclassNestedObject",
            "type": "object",
            "required": ["str_field", "nested_object"],
            "properties": {
                "str_field": {"type": "string"},
                "nested_object": {"$ref": "#/components/schemas/DataclassObject"},
            },
        },
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
        },
    }
    assert expected_openapi_schema == get_openapi_schema(
        DataclassNestedObject, reference=False
    )