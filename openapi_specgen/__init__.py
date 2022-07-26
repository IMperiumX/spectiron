"""Top-level package for openapi-specgen."""
from openapi import OpenApi
from param import OpenApiParam
from path import OpenApiPath
from response import OpenApiResponse

__all__ = ['OpenApiParam', 'OpenApiResponse', 'OpenApiPath', 'OpenApi']
__author__ = """Yusuf Adel"""
__email__ = 'yusufadell.dev@gmail.com'
__version__ = '0.1.0'
