from openapi_specgen import OpenApiParam, OpenApiPath, OpenApiResponse


def test_path_with_params():
    expected_openapi_dict = {
        "/test_path": {
            "GET": {
                "description": "Test Description",
                "summary": "Test Summary",
                "operationId": "[GET]_/test_path",
                "responses": {"200": {"description": "Test Response"}},
                "parameters": [
                    {
                        "required": True,
                        "schema": {"title": "Test_Param", "type": "string"},
                        "name": "test_param",
                        "in": "query",
                    }
                ],
            }
        }
    }
    openapi_path = OpenApiPath(
        "/test_path",
        "GET",
        [OpenApiResponse("Test Response")],
        [OpenApiParam("test_param", "query", str)],
        "Test Description",
        "Test Summary",
    )
    assert expected_openapi_dict == openapi_path.as_dict()


def test_path_no_params():
    expected_openapi_dict = {
        "/test_path": {
            "GET": {
                "description": "Test Description",
                "summary": "Test Summary",
                "operationId": "[GET]_/test_path",
                "responses": {"200": {"description": "Test Response"}},
                "parameters": [],
            }
        }
    }
    openapi_path = OpenApiPath(
        "/test_path",
        "GET",
        [OpenApiResponse("Test Response")],
        description="Test Description",
        summary="Test Summary",
    )
    assert expected_openapi_dict == openapi_path.as_dict()
