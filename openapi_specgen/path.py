from dataclasses import dataclass, field
from typing import List

from openapi_specgen.param import OpenApiParam
from openapi_specgen.response import OpenApiResponse
from openapi_specgen.schema import get_openapi_schema


@dataclass
class OpenApiPath:
    path: str
    method: str

    responses: List[OpenApiResponse] = field(default_factory=list)
    params: List[OpenApiParam] = field(default_factory=list)

    descr: str = "Description of the endpoint"
    summary: str = "Summary of the endpoint"

    def asdict(self):
        openapi_dict = {
            self.path: {
                self.method.upper(): {
                    "description": self.descr,
                    "summary": self.summary,
                    "operationId": f"[{self.method.upper()}]_{self.path}",
                    "responses": {
                        k: v
                        for response in self.responses
                        for k, v in response.asdict().items()
                    },
                    "parameters": [param.asdict() for param in self.params],
                }
            }
        }
        if self.request_body is not None:
            openapi_dict[self.path][self.method]["requestBody"] = {
                "content": {
                    "application/json": {
                        "schema": get_openapi_schema(self.request_body)
                    }
                }
            }
        return openapi_dict
