from master import *
from global_ import *
from tools import *
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
def mvi(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 3:
        to = resister_is(v[1])
        if to == -1:
            return True
        elif to == 7:
            len_v2 = len(v[2])
            if len_v2 == 2:
                data = hex2dec(v[2])
                if data == -1:
                    return True
                to = rpair(5)
                storage[to] = data
            else:
                return True
        else:
            data = hex2dec(v[2])
            if data == -1:
                return True
            gpr[to] = data
        return False
    else:
        return True
