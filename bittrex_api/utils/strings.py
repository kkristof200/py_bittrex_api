# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, Dict, Any

# ---------------------------------------------------------------------------------------------------------------------------------------- #




# ------------------------------------------------------------ Public methods ------------------------------------------------------------ #

def to_string(value: Any) -> Optional[str]:
    if isinstance(value, str):
        return value

    from enum import Enum

    if issubclass(type(value), Enum):
        value = value.value

    return str(value)