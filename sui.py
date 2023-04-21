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
from tools import splitter, register_is, hex2dec, set_flag_register

def sui(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        from_register = register_is(v[1])
        if from_register == -1:
            if len(v[1]) == 2:
                from_register = hex2dec(v[1])
                if from_register == -1:
                    return True
                gpr[0] = gpr[0] - from_register
                set_flag_register(gpr[0])
                gpr[0] = abs(gpr[0])
                return False
            else:
                return True
        else:
            return True
    else:
        return True
