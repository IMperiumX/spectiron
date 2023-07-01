from openapi_specgen import OpenApiSecurity, BasicAuth, BearerAuth, ApiKeyAuth


def test_openapi_security_referece():
    expected_openapi_dict = [{"ApiKeyAuth": []}, {"BasicAuth": []}, {"BearerAuth": []}]
    openapi_security = OpenApiSecurity(
        basic_auth=BasicAuth(),
        bearer_auth=BearerAuth(),
        api_key_auth=ApiKeyAuth(),
    )
    assert expected_openapi_dict == openapi_security.get_security_reference()


def test_openpi_security():
    expected_openapi_dict = {
        "BasicAuth": {"type": "http", "scheme": "basic"},
        "BearerAuth": {"type": "http", "scheme": "bearer"},
        "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "X-API-Key"},
    }
    openapi_security = OpenApiSecurity(
        basic_auth=BasicAuth(),
        bearer_auth=BearerAuth(),
        api_key_auth=ApiKeyAuth(),
    )
    assert expected_openapi_dict == openapi_security.as_dict()
