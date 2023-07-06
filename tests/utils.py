from dataclasses import dataclass, field


@dataclass
class DataclassObject:
    str_field: str = "test"
    int_field: int = 1
    float_field: float = 1.0
    boolean_field: bool = True
    list_field: list = field(default_factory=list)


@dataclass
class DataclassNestedObject:
    str_field: str = "test"
    nested_object: DataclassObject = field(default_factory=DataclassObject)
