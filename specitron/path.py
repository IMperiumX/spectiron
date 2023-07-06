from dataclasses import dataclass, field
from typing import Any, List

from specitron.param import OpenApiParam
from specitron.response import OpenApiResponse
from specitron.schema import get_openapi_schema


@dataclass
class OpenApiPath:
    path: str
    method: str

    responses: list[OpenApiResponse] = field(default_factory=list)
    params: list[OpenApiParam] = field(default_factory=list)

    description: str = "Description of the endpoint"
    summary: str = "Summary of the endpoint"
    request_body: Any = None

    def as_dict(self):
        self.method = self.method.upper()
        openapi_dict = {
            self.path: {
                self.method: {
                    "description": self.description,
                    "summary": self.summary,
                    "operationId": f"[{self.method.upper()}]_{self.path}",
                    "responses": {
                        k: v
                        for response in self.responses
                        for k, v in response.as_dict().items()
                    },
                    "parameters": [param.as_dict() for param in self.params],
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
