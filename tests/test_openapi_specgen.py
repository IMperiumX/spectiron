#!/usr/bin/env python

"""Tests for `specitron` package."""


import pytest
from click.testing import CliRunner

from specitron import (
    ApiKeyAuth,
    BasicAuth,
    BearerAuth,
    OpenApi,
    OpenApiParam,
    OpenApiPath,
    OpenApiResponse,
    OpenApiSecurity,
    cli,
)
from tests.utils import DataclassObject


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "specitron.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_openapi():
    expected_openapi_dict = {
        "openapi": "0.1.0",
        "info": {"title": "test_api", "version": "0.1.0"},
        "paths": {
            "/test_path": {
                "GET": {
                    "description": "Description of the endpoint",
                    "summary": "Summary of the endpoint",
                    "operationId": "[GET]_/test_path",
                    "responses": {
                        "200": {
                            "description": "test_response",
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
                                                "list_field": {
                                                    "type": "array",
                                                    "items": {},
                                                },
                                            },
                                        }
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
                            "schema": {
                                "title": "Test_Param",
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
                            },
                        }
                    ],
                    "requestBody": {
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
                                            "list_field": {
                                                "type": "array",
                                                "items": {},
                                            },
                                        },
                                    }
                                }
                            }
                        }
                    },
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
                        "str_field": {"type": "string"},
                        "int_field": {"type": "integer"},
                        "float_field": {"type": "number"},
                        "boolean_field": {"type": "boolean"},
                        "list_field": {"type": "array", "items": {}},
                    },
                }
            },
            "securitySchemes": {
                "BasicAuth": {"type": "http", "scheme": "basic"},
                "BearerAuth": {"type": "http", "scheme": "bearer"},
                "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "X-API-Key"},
            },
        },
        "security": [{"ApiKeyAuth": []}, {"BasicAuth": []}, {"BearerAuth": []}],
    }
    test_resp = OpenApiResponse(
        description="test_response",
        data_type=DataclassObject,
    )
    test_param = OpenApiParam(
        name="test_param",
        location="query",
        data_type=DataclassObject,
    )
    test_path = OpenApiPath(
        path="/test_path",
        method="get",
        responses=[test_resp],
        params=[test_param],
        request_body=DataclassObject,
    )
    test_security = OpenApiSecurity(BasicAuth(), BearerAuth(), ApiKeyAuth())
    test_api = OpenApi(title="test_api", paths=[test_path], security=test_security)
    assert expected_openapi_dict == test_api.as_dict()
