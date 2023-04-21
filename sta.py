from typing import List
from master import *
from global_ import *
from tools import splitter
import hex2dec
def sta(temp_string: str) -> bool:
    v: List[str] = splitter(temp_string)
    size: int = len(v)
    if size == 2:
        len_str: int = len(v[1])
        if len_str == 4:
            address: int = hex2dec(v[1])
            if address == -1:
                return True
            storage[address] = gpr[0]
            return False
        else:
            return True
    else:
        return True
