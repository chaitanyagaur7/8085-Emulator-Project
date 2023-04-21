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
def mov(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 3:
        to = resister_is(v[1])
        from_ = resister_is(v[2])
        if to == -1 or from_ == -1:
            return True
        elif to == 7 and from_ == 7:
            return True
        elif to == 7 and from_ != 7 and from_ != -1:
            to = rpair(5)
            storage[to] = gpr[from_]
        elif from_ == 7 and to != 7 and to != -1:
            from_ = rpair(5)
            gpr[to] = storage[from_]
        else:
            gpr[to] = gpr[from_]
        return False
    else:
        return True
