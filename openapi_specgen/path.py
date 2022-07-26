from dataclasses import dataclass
from typing import List

from param import OpenApiParam
from response import OpenApiResponse


@dataclass
class OpenApiPath():
    path: str
    method: str
    responses: List[OpenApiResponse]
    params: List[OpenApiParam] = []
    descr: str = '',
    summary: str = ''

    def asdict(self):
        return {
            self.path: {
                self.method: {
                    'description': self.descr,
                    'summary': self.summary,
                    'operationId': f'[{self.method}]_{self.path}',
                    'responses': {
                        k: v for response in self.responses for k, v in response.asdict().items()
                    },
                    'parameters': [
                        param.asdict() for param in self.params
                    ]
                }
            }
        }
