# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Dict, Any
from enum import Enum

# Local
from . import strings

# ---------------------------------------------------------------------------------------------------------------------------------------- #




# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

def enum_free_dict(d: Dict, remove_none_values: bool = True) -> Dict:
    _enum_free_dict = {}

    for k, v in d.items():
        if remove_none_values and v is None:
            continue

        if isinstance(v, dict):
            v = enum_free_dict(v, remove_none_values=remove_none_values)

        _enum_free_dict[strings.to_string(k)] = optionally_get_enum_value(v)

    return _enum_free_dict

def optionally_get_enum_value(value: Any) -> Any:
    if issubclass(type(value), Enum):
        return value.value
    
    return value