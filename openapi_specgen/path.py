from dataclasses import dataclass, field
from typing import List


from .param import OpenApiParam
from .response import OpenApiResponse


@dataclass
class OpenApiPath():
    path: str
    method: str
    responses: List[OpenApiResponse]
    # make params optional & fix dataclasses ValueError with mutable default
    # Stackoverflow:https://stackoverflow.com/questions/53632152/why-cant-dataclasses-have-mutable-defaults-in-their-class-attributes-declaratio
    params: List[OpenApiParam] = field(default_factory=list)
    descr: str = ''
    summary: str = ''

    def asdict(self):
        return {
            self.path: {
                self.method.upper(): {
                    'description': self.descr,
                    'summary': self.summary,
                    'operationId': f'[{self.method.upper()}]_{self.path}',
                    'responses': {
                        k: v for response in self.responses for k, v in response.asdict().items()
                    },
                    'parameters': [
                        param.asdict() for param in self.params
                    ]
                }
            }
        }

    def __repr__(self) -> str:
        return f"Here we are => {self.asdict()!r}"
