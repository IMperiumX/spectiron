from typing import List

import pytest

from specitron import OpenApiParam


@pytest.mark.parametrize("location", [("query"), ("path"), ("header"), ("cookie")])
def test_param_location(location):
    expected_param_dict = {
        "required": True,
        "name": "test_param",
        "in": location,
        "schema": {"title": "Test_Param", "type": "string"},
    }

    openapi_param = OpenApiParam(
        name="test_param",
        location=location,
        data_type=str,
    )
    assert expected_param_dict == openapi_param.as_dict()


def test_param_optinal():
    expected_param_dict = {
        "required": False,
        "name": "test_param",
        "in": "path",
        "schema": {"title": "Test_Param", "type": "string"},
    }
    openapi_param = OpenApiParam(
        name="test_param",
        location="path",
        data_type=str,
        required=False,
    )
    assert expected_param_dict == openapi_param.as_dict()


def test_param_default():
    expected_param_dict = {
        "required": True,
        "name": "test_param",
        "in": "path",
        "schema": {"title": "Test_Param", "type": "string", "default": "default_value"},
    }
    openapi_param = OpenApiParam(
        name="test_param",
        location="path",
        data_type=str,
        default="default_value",
    )
    assert expected_param_dict == openapi_param.as_dict()


def test_param_any_type():
    expected_param_dict = {
        "required": True,
        "name": "test_param",
        "in": "path",
        "schema": {"title": "Test_Param"},
    }
    openapi_param = OpenApiParam(
        name="test_param",
        location="path",
    )
    assert expected_param_dict == openapi_param.as_dict()


@pytest.mark.parametrize(
    "data_type, openapi_item_type",
    [
        (list, {}),
        (list[str], {"type": "string"}),
        (list[int], {"type": "integer"}),
        (list[float], {"type": "number"}),
        (list[bool], {"type": "boolean"}),
        (list[bool], {"type": "boolean"}),
    ],
)
def test_param_typed_list(data_type, openapi_item_type):
    expected_param_dict = {
        "required": True,
        "name": "test_param",
        "in": "path",
        "schema": {"title": "Test_Param", "type": "array", "items": openapi_item_type},
    }
    openapi_param = OpenApiParam(
        name="test_param",
        location="path",
        data_type=data_type,
    )
    assert expected_param_dict == openapi_param.as_dict()


# @pytest.mark.skip("WIP")
# def test_param_enum():
#     pass


# @pytest.mark.skip("WIP")
# def test_param_examples():
#     pass


# @pytest.mark.skip("WIP")
# def test_param_empty_value():
#     pass


# @pytest.mark.skip("WIP")
# def test_param_nullable():
#     pass


# @pytest.mark.skip("WIP")
# def test_param_deprecated():
#     pass
