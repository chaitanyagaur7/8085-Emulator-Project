from typing import List, Tuple
#include "master.h"
#include "global.h"
#include "tools.h"
from master import *
from global_ import *
from register_is import resister_is
import tools
import splitter
import check_storage
import rpair
import set_flag_register
import hex2dec
def adi(temp_string: str) -> bool:
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        from_reg = resister_is(v[1])
        if from_reg == -1:
            if len(v[1]) == 2:
                data = hex2dec(v[1])
                if data == -1:
                    return True
                gpr[0] = gpr[0] + data
                set_flag_register(gpr[0])
                return False
            else:
                return True
        else:
            return True
    else:
        return True
