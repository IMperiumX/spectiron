#!/usr/bin/env python

"""Tests for `openapi_specgen` package."""


from openapi_specgen import OpenApi, OpenApiParam, OpenApiPath, OpenApiResponse
from tests.utils import DataclassObject

# from click.testing import CliRunner

# from openapi_specgen import cli


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert "openapi_specgen.cli.main" in result.output
#     help_result = runner.invoke(cli.main, ["--help"])
#     assert help_result.exit_code == 0
#     assert "--help  Show this message and exit." in help_result.output


def test_openapi():
    expected_openapi_dict = {
        "openapi": "0.1.0",
        "info": {"title": "test_api", "version": "0.1.0"},
        "paths": {
            "/test_path": {
                "GET": {
                    "description": "",
                    "summary": "",
                    "operationId": "[GET]_/test_path",
                    "responses": {
                        "200": {
                            "description": "test_response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/DataclassObject"
                                    }
                                }
                            },
                        }
                    },
                    "parameters": [
                        {
                            "required": True,
                            "name": "test_param",
                            "in": "query",
                            "schema": {"title": "Test_Param", "type": "string"},
                        }
                    ],
                }
            }
        },
        "components": {
            "schemas": {
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
                        "str_field": {"title": "Str_Field", "type": "string"},
                        "int_field": {"title": "Int_Field", "type": "integer"},
                        "float_field": {"title": "Float_Field", "type": "number"},
                        "boolean_field": {"title": "Boolean_Field", "type": "boolean"},
                        "list_field": {"title": "List_Field", "type": "array"},
                    },
                }
            }
        },
    }

    test_resp = OpenApiResponse("test_response", data_type=DataclassObject)
    test_param = OpenApiParam("test_param", "query", data_type=str)
    test_path = OpenApiPath("/test_path", "get", [test_resp], [test_param])
    test_api = OpenApi("test_api", [test_path])
    return expected_openapi_dict == test_api.asdict()
