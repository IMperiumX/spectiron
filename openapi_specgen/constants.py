from datetime import date, datetime

OPENAPI_DEFAULT_TYPE = "object"

OPENAPI_TYPE_MAP = {
    str: "string",
    date: "string",
    datetime: "string",
    float: "number",
    int: "integer",
    bool: "boolean",
    list: "array",
}

OPENAPI_FORMAT_MAP = {
    date: "date",
    datetime: "date-time",
}

OPENAPI_ARRAY_ITEM_MAP = {
    list[str]: "string",
    list[float]: "number",
    list[int]: "integer",
    list[bool]: "boolean",
    list: None,
}

get_type = OPENAPI_TYPE_MAP.get
get_format = OPENAPI_FORMAT_MAP.get
get_list_generic_type = OPENAPI_ARRAY_ITEM_MAP.get

__all__ = [
    "OPENAPI_DEFAULT_TYPE",
    "get_type",
    "get_list_generic_type",
]
