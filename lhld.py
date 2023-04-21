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
def lhld(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        length = len(v[1])
        if length == 4:
            address = hex2dec(v[1])
            if address == -1:
                return True
            data = dec2hex(storage[address], 2)
            temp1 = ""
            temp2 = ""
            temp1 = temp1 + data[0] + data[1]
            data = dec2hex(storage[address+1], 2)
            temp2 = temp2 + data[0] + data[1]
            gpr[6] = hex2dec(temp1)
            gpr[5] = hex2dec(temp2)
            return False
        else:
            return True
    else:
        return True
