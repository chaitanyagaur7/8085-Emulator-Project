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
def inr(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        temp = resister_is(v[1])
        if temp == -1:
            return True
        elif temp == 7:
            from_ = check_storage(rpair(5))
            from_ += 1
            if from_ > 255:
                from_ = 0
            storage[rpair(5)] = from_
        else:
            from_ = gpr[temp] + 1
            if from_ > 255:
                from_ = 0
            else:
                gpr[temp] = from_
        set_flag_register(from_)
        return False
    return True
