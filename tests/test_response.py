import pytest

from specitron import OpenApiResponse
from tests.utils import DataclassObject


def test_response_primitive():
    expected_openapi_dict = {
        "200": {
            "description": "Test Response",
            "content": {"application/json": {"schema": {"type": "string"}}},
        }
    }

    openapi_response = OpenApiResponse("Test Response", data_type=str)
    assert expected_openapi_dict == openapi_response.as_dict()


def test_response_object_with_reference():
    expected_openapi_dict = {
        "200": {
            "description": "Test Response",
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/DataclassObject"}
                }
            },
        }
    }
    openapi_response = OpenApiResponse(
        "Test Response",
        data_type=DataclassObject,
        reference=True,
    )
    assert expected_openapi_dict == openapi_response.as_dict()


def test_response_object_without_reference():
    expected_openapi_dict = {
        "200": {
            "description": "Test Response",
            "content": {
                "application/json": {
                    "schema": {
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
                    }
                }
            },
        }
    }

    openapi_response = OpenApiResponse(
        description="Test Response",
        data_type=DataclassObject,
    )
    assert expected_openapi_dict == openapi_response.as_dict()


def test_response_empty():
    expected_openapi_dict = {"201": {"description": "Test Empty Response"}}
    openapi_response = OpenApiResponse("Test Empty Response", "201")
    assert expected_openapi_dict == openapi_response.as_dict()


@pytest.mark.skip("WIP")
def test_response_format():
    pass


@pytest.mark.skip("WIP")
def test_response_headers():
    pass


@pytest.mark.skip("WIP")
def test_response_any_of():
    pass


@pytest.mark.skip("WIP")
def test_response_links():
    pass


@pytest.mark.skip("WIP")
def test_response_multiple_media_types():
    pass
