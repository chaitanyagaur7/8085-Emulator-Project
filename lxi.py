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
def lxi(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 3:
        to = resister_is(v[1])
        if to == -1 or to == 7:
            return True
        else:
            data = v[2]
            if len(data) == 4:
                temp1, temp2 = data[0:2], data[2:4]
                if to == 1:
                    gpr[1], gpr[2] = hex2dec(temp1), hex2dec(temp2)
                elif to == 3:
                    gpr[3], gpr[4] = hex2dec(temp1), hex2dec(temp2)
                elif to == 5:
                    gpr[5], gpr[6] = hex2dec(temp1), hex2dec(temp2)
                else:
                    return True
            else:
                return True
        return False
    else:
        return True
