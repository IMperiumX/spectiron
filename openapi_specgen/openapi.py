from dataclasses import dataclass, field
from typing import List

from openapi_specgen.path import OpenApiPath
from openapi_specgen.schema import OPENAPI_DEFAULT_TYPE, get_openapi_schema, get_type


@dataclass
class OpenApi:

    version: str = "0.1.0"
    title: str = ""
    paths: List[OpenApiPath] = field(default_factory=list)
    reference: bool = False

    def asdict(self):
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
                openapi_path.asdict()[openapi_path.path]
            )

            for param in openapi_path.params:
                if (
                    get_type(param.data_type, OPENAPI_DEFAULT_TYPE)
                    == OPENAPI_DEFAULT_TYPE
                ):
                    openapi_dict["components"]["schemas"] = get_openapi_schema(
                        param.data_type
                    )

            for resp in openapi_path.responses:
                if (
                    get_type(resp.data_type, OPENAPI_DEFAULT_TYPE)
                    == OPENAPI_DEFAULT_TYPE
                ):
                    openapi_dict["components"]["schemas"] = get_openapi_schema(
                        resp.data_type
                    )

        return openapi_dict
