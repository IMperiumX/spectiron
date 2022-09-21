import pytest

from openapi_specgen import OpenApiResponse
from tests.utils import DataclassObject


def test_response_primitive():
    expected_openapi_dict = {
        "200": {
            "description": "Test Response",
            "content": {"application/json": {"schema": {"type": "string"}}},
        }
    }
    openapi_response = OpenApiResponse("Test Response", data_type=str)
    assert expected_openapi_dict == openapi_response.asdict()


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
        "Test Response", data_type=DataclassObject, reference=True
    )
    assert expected_openapi_dict == openapi_response.asdict()


def test_response_object_without_reference():
    expected_openapi_dict = {
        "200": {
            "content": {
                "application/json": {
                    "schema": {
                        "DataclassObject": {
                            "properties": {
                                "boolean_field": {
                                    "title": "Boolean_Field",
                                    "type": "boolean",
                                },
                                "float_field": {
                                    "title": "Float_Field",
                                    "type": "number",
                                },
                                "int_field": {
                                    "title": "Int_Field",
                                    "type": "integer",
                                },
                                "list_field": {
                                    "title": "List_Field",
                                    "type": "array",
                                },
                                "str_field": {
                                    "title": "Str_Field",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "str_field",
                                "int_field",
                                "float_field",
                                "boolean_field",
                                "list_field",
                            ],
                            "title": "DataclassObject",
                            "type": "object",
                        }
                    }
                }
            },
            "description": "Test Response",
        }
    }
    openapi_response = OpenApiResponse("Test Response", data_type=DataclassObject)
    assert expected_openapi_dict == openapi_response.asdict()


def test_response_empty():
    expected_openapi_dict = {"201": {"description": "Test Empty Response"}}
    openapi_response = OpenApiResponse("Test Empty Response", "201")
    assert expected_openapi_dict == openapi_response.asdict()


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
