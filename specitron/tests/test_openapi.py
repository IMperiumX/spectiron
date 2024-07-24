"""
{'openapi': '3.0.2',
 'info': {'title': [<URLPattern '^account/new/$' [name='account-new']>,
   <URLPattern '^account/old/$' [name='account-old']>],
  'version': ''},
 'paths': {}} # models was not set in ExampleSerializer!
"""
from django.test import RequestFactory
from rest_framework import routers
from rest_framework.request import Request

from . import views
from openapi_specgen import SchemaGenerator


def create_request(path):
    factory = RequestFactory()
    request = Request(factory.get(path))
    return request


class TestOperations:
    def test_operation_id_viewset(self):
        router = routers.SimpleRouter()
        router.register("account", views.ExampleViewSet, basename="account")
        urlpatterns = router.urls

        generator = SchemaGenerator(patterns=urlpatterns)

        request = create_request("/")
        schema = generator.get_schema(request=request)
        print(schema)
        assert (
            schema["paths"]["/account/"]["get"]["operationId"] == "listExampleViewSets"
        )
        assert (
            schema["paths"]["/account/"]["post"]["operationId"]
            == "createExampleViewSet"
        )
        assert (
            schema["paths"]["/account/{id}/"]["get"]["operationId"]
            == "retrieveExampleViewSet"
        )
        assert (
            schema["paths"]["/account/{id}/"]["put"]["operationId"]
            == "updateExampleViewSet"
        )
        assert (
            schema["paths"]["/account/{id}/"]["patch"]["operationId"]
            == "partialUpdateExampleViewSet"
        )
        assert (
            schema["paths"]["/account/{id}/"]["delete"]["operationId"]
            == "destroyExampleViewSet"
        )
