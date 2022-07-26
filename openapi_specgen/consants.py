from typing import List

OPENAPI_DEFAULT_TYPE = "object"


OPENAPI_TYPE_MAP = {
    str: "string",
    float: "number",
    int: "integer",
    bool: "boolean",
    list: "array",
    List: "array",
    List[str]: "array",
    List[float]: "array",
    List[int]: "array",
    List[bool]: "array"
}

OPENAPI_ARRAY_ITEM_MAP = {
    List[str]: "string",
    List[float]: "number",
    List[int]: "integer",
    List[bool]: "boolean",
    List: None
}
