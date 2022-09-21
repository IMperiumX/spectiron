from dataclasses import dataclass

from openapi_specgen.schema import get_openapi_schema


@dataclass
class OpenApiResponse:
    descr: str
    status_code: int = 200
    data_type: type = None
    reference: bool = False
    http_content_type: str = "application/json"

    def asdict(self):
        openapi_dict = {str(self.status_code): {"description": self.descr}}

        if self.data_type is None:
            return openapi_dict

        openapi_dict[str(self.status_code)]["content"] = {
            self.http_content_type: {
                "schema": get_openapi_schema(self.data_type, reference=self.reference)
            }
        }

        return openapi_dict
