from dataclasses import dataclass, field
from typing import List

import openapi_specgen
from openapi_specgen.path import OpenApiPath
from openapi_specgen.schema import (OPENAPI_DEFAULT_TYPE, get_openapi_schema,
                                    get_type)


@dataclass
class OpenApi:

    version: str = openapi_specgen.__version__
    title: str = "OpenApi"
    paths: List[OpenApiPath] = field(default_factory=list)
    reference: bool = True

    def asdict(self):
        openapi_dict = {
            "openapi": self.version,
            "info": {"title": self.title, "version": self.version},
            "paths": {path.path: path.asdict() for path in self.paths},
            "components": {
                "schemas": {
                    get_type(schema): get_openapi_schema(schema, self.reference)
                    for path in self.paths
                    for schema in path.schemas
                }
            },
        }

        # for openapi_path in self.paths:
        #     if openapi_dict["paths"].get(openapi_path.path) is None:
        #         openapi_dict["paths"][openapi_path.path] = {}
        #     openapi_dict["paths"][openapi_path.path].update(
        #         openapi_path.asdict()[openapi_path.path]
        #     )

        #     for param in openapi_path.params:
        #         if (
        #             get_type(param.data_type, OPENAPI_DEFAULT_TYPE)
        #             == OPENAPI_DEFAULT_TYPE
        #         ):
        #             openapi_dict["components"]["schemas"] = get_openapi_schema(
        #                 param.data_type
        #             )

        #     for resp in openapi_path.responses:
        #         if (
        #             get_type(resp.data_type, OPENAPI_DEFAULT_TYPE)
        #             == OPENAPI_DEFAULT_TYPE
        #         ):
        #             openapi_dict["components"]["schemas"] = get_openapi_schema(
        #                 resp.data_type
        #             )

        return openapi_dict
