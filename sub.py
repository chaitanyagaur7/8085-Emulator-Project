from check_opcode import check_opcode
from dec2hex import dec2hex
from master import *
from global_ import *
from typing import List, Tuple
#include "master.h"
#include "global.h"
#include "tools.h"
from master import *
from global_ import *
from program_counter_increment import program_counter_increment
from register_is import resister_is
import tools
import splitter
import check_storage
import rpair
import set_flag_register
import hex2dec
def sub(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        from_reg = resister_is(v[1])
        if from_reg == -1:
            return True
        elif from_reg == 7:
            from_reg = check_storage(rpair(5))
            if from_reg == -1:
                return True
            else:
                gpr[0] = gpr[0] - from_reg
        else:
            gpr[0] = gpr[0] - gpr[from_reg]
        set_flag_register(gpr[0])
        gpr[0] = abs(gpr[0])
        return False
    else:
        return True
