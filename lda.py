from tools import splitter, hex2dec
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
def lda(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        len_v1 = len(v[1])
        if len_v1 == 4:
            data = hex2dec(v[1])
            if data == -1:
                return True
            gpr[0] = storage[data]
            return False
        else:
            return True
    else:
        return True
