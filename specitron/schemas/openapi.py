import warnings
from urllib.parse import urljoin

from .generators import BaseSchemaGenerator


class SchemaGenerator(BaseSchemaGenerator):
    def get_info(self):
        # Title and version are required by openapi specification 3.x
        info = {"title": self.title or "", "version": self.version or ""}

        if self.description is not None:
            info["description"] = self.description

        return info

    def check_duplicate_operation_id(self, paths):
        ids = {}
        for route in paths:
            for method in paths[route]:
                if "operationId" not in paths[route][method]:
                    continue
                operation_id = paths[route][method]["operationId"]
                if operation_id in ids:
                    warnings.warn(
                        "You have a duplicated operationId in your OpenAPI schema: {operation_id}\n"
                        "\tRoute: {route1}, Method: {method1}\n"
                        "\tRoute: {route2}, Method: {method2}\n"
                        "\tAn operationId has to be unique across your schema. Your schema may not work in other tools.".format(
                            route1=ids[operation_id]["route"],
                            method1=ids[operation_id]["method"],
                            route2=route,
                            method2=method,
                            operation_id=operation_id,
                        )
                    )
                ids[operation_id] = {"route": route, "method": method}

    def get_schema(self, request=None, public=False):
        """
        Generate a OpenAPI schema.
        """
        self._initialise_endpoints()
        components_schemas = {}

        # Iterate endpoints generating per method path operations.
        paths = {}
        _, view_endpoints = self._get_paths_and_endpoints(None if public else request)
        for path, method, view in view_endpoints:
            if not self.has_view_permissions(path, method, view):
                continue

            operation = view.schema.get_operation(path, method)
            components = view.schema.get_components(path, method)
            for k in components.keys():
                if k not in components_schemas:
                    continue
                if components_schemas[k] == components[k]:
                    continue
                warnings.warn(
                    'Schema component "{}" has been overriden with a different value.'.format(
                        k
                    )
                )

            components_schemas.update(components)

            # Normalise path for any provided mount url.
            if path.startswith("/"):
                path = path[1:]
            path = urljoin(self.url or "/", path)

            paths.setdefault(path, {})
            paths[path][method.lower()] = operation

        self.check_duplicate_operation_id(paths)

        # Compile final schema.
        schema = {
            "openapi": "3.0.2",
            "info": self.get_info(),
            "paths": paths,
        }

        if len(components_schemas) > 0:
            schema["components"] = {"schemas": components_schemas}

        return schema
