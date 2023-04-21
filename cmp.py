from typing import List
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

def cmp(temp_string: str) -> bool:
    v: List[str] = splitter(temp_string)
    size: int = len(v)
    if size == 2:
        compare: int = resister_is(v[1])
        if compare == -1:
            return True
        elif compare == 7:
            compare = check_storage(rpair(5))
            if compare == -1:
                return True
            else:
                if compare == gpr[0]:
                    flag[3] = 1
                    flag[0] = 0  # SET ZERO FLAG
                elif compare > gpr[0]:
                    flag[0] = 1
                    flag[3] = 0  # SET CARRY FLAG
                else:
                    flag[0] = 0
                    flag[3] = 0  # RESET ZERO AND CARRY FLAG
        else:
            if gpr[compare] == gpr[0]:
                flag[3] = 1
                flag[0] = 0  # SET ZERO FLAG
            elif gpr[compare] > gpr[0]:
                flag[0] = 1
                flag[3] = 0  # SET CARRY FLAG
            else:
                flag[0] = 0
                flag[3] = 0  # RESET ZERO AND CARRY FLAG
        return False
    else:
        return True
