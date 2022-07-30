from dataclasses import dataclass
from .utils import get_openapi_schema


@dataclass
class OpenApiParam():
    name: str
    location: str
    data_type: type = None
    default: bool = None
    required: bool = True

    def asdict(self):
        openapi_dict = {
            'required': self.required,
            'name': self.name,
            'in': self.location
        }

        schema = {}

        if self.data_type:
            schema = get_openapi_schema(self.data_type)
        if self.default:
            schema['default'] = self.default

        schema['title'] = self.name.title()
        openapi_dict['schema'] = schema
        return openapi_dict
