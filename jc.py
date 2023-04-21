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

def jc(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        if flag[0] == 1:
            address = hex2dec(v[1])
            if address == -1:
                return True
            is_there = False
            for i in range(size_pc):
                if program_counter[i] == address:
                    is_there = True
                    index_pc = i - 1
                    return False
            if not is_there:
                return True
        else:
            return False
    return True
