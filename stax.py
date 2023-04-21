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
def stax(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        index = resister_is(v[1])
        if index == 1 or index == 3 or index == 5:
            temp = dec2hex(gpr[index], 2) + dec2hex(gpr[index+1], 2)
            address = hex2dec(temp)
            if address == -1:
                return True
            storage[address] = gpr[0]
            return False
        else:
            return True
    else:
        return True
