import uuid

from django.db import models
from rest_framework import serializers
from rest_framework.viewsets import ViewSet


class OpenAPIExample(models.Model):
    first_name = models.CharField(max_length=30)


class ExampleSerializerModel(serializers.Serializer):
    date = serializers.DateField()
    datetime = serializers.DateTimeField()
    hstore = serializers.HStoreField()
    uuid_field = serializers.UUIDField(default=uuid.uuid4)

    class Meta:
        model = OpenAPIExample


class ExampleViewSet(ViewSet):
    serializer_class = ExampleSerializerModel

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
