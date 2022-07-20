from typing import List

from .param import OpenApiParam
from .response import OpenApiResponse


class OpenApiPath():

    def __init__(self,
                 path: str,
                 method: str,
                 responses: List[OpenApiResponse],
                 params: List[OpenApiParam] = [],
                 descr: str = '',
                 summary: str = '',
                 ):
        self.path = path
        self.method = method
        self.responses = responses
        self.params = params
        self.summary = summary
        self.descr = descr

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
