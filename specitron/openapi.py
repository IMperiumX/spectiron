from dataclasses import dataclass, field
from typing import List, Union

from .constants import OPENAPI_DEFAULT_TYPE, get_type
from .path import OpenApiPath
from .schema import get_openapi_schema
from .security import OpenApiSecurity


@dataclass
class OpenApi:
    """Object to represent an OpenApi specification as defined on
    https://swagger.io/docs/specification/about/

    Args:
        title (str): Title of your Api
        paths (List[OpenApiPath]): List of OpenApiPaths that are part of this Api
        security Optional[OpenApiSecurity]: Optional OpenApiSecurity defining authentication options for this Api
    """

    paths: List[OpenApiPath] = field(default_factory=list)
    security: Union[OpenApiSecurity, None] = None

    version: str = "0.1.0"
    title: str = "OpenApi Title"

    def as_dict(self) -> dict:
        """
        Returns:
            dict: dict representing this object as an OpenApi specification.
        """
        openapi_dict = {
            "openapi": self.version,
            "info": {"title": self.title, "version": self.version},
            "paths": {},
            "components": {"schemas": {}},
        }

        for openapi_path in self.paths:
            if openapi_dict["paths"].get(openapi_path.path) is None:
                openapi_dict["paths"][openapi_path.path] = {}
            openapi_dict["paths"][openapi_path.path].update(
                openapi_path.as_dict()[openapi_path.path]
            )

            if openapi_path.request_body:
                if (
                    get_type(openapi_path.request_body, OPENAPI_DEFAULT_TYPE)
                    == "object"
                ):
                    openapi_dict["components"]["schemas"].update(
                        get_openapi_schema(openapi_path.request_body)
                    )

            for param in openapi_path.params:
                if get_type(param.data_type, OPENAPI_DEFAULT_TYPE) == "object":
                    openapi_dict["components"]["schemas"].update(
                        get_openapi_schema(param.data_type)
                    )

            for resp in openapi_path.responses:
                if get_type(resp.data_type, OPENAPI_DEFAULT_TYPE) == "object":
                    openapi_dict["components"]["schemas"].update(
                        get_openapi_schema(resp.data_type)
                    )
            if self.security:
                openapi_dict["security"] = self.security.get_security_reference()
                openapi_dict["components"]["securitySchemes"] = self.security.as_dict()

        return openapi_dict
