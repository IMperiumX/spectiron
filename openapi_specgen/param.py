from dataclasses import dataclass
from typing import Any

from openapi_specgen.schema import get_openapi_schema


@dataclass
class OpenApiParam:
    name: str = "param_name"
    location: str = "query"
    data_type: type = None
    default: Any = None
    required: bool = True
    reference: bool = True

    def asdict(self):
        openapi_dict = {
            "name": self.name,
            "in": self.location,
            "required": self.required,
            "schema": {
                self.data_type
                if get_openapi_schema(self.data_type, self.reference)
                else self.default
            },
            "title": self.name,
        }
        return openapi_dict
