from dataclasses import dataclass
from typing import Any

from specitron.schema import get_openapi_schema


@dataclass
class OpenApiParam:
    name: str = "param_name"
    location: str = "query"
    data_type: type = None
    default: Any = None
    required: bool = True

    def as_dict(self):
        openapi_dict = {
            "required": self.required,
            "name": self.name,
            "in": self.location,
            "schema": {
                "title": self.name.title(),
            },
        }
        if self.data_type is not None:
            openapi_dict["schema"].update(get_openapi_schema(self.data_type))
        if self.default:
            openapi_dict["schema"]["default"] = self.default
        return openapi_dict
