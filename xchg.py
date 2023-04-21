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
def xchg(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 1:
        swap_temp = gpr[5]
        gpr[5] = gpr[3]
        gpr[3] = swap_temp
        swap_temp = gpr[6]
        gpr[6] = gpr[4]
        gpr[4] = swap_temp
        return False
    else:
        return True
