from master import *
from tools import *
from global_ import *
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
def set1(temp_string: str) -> bool:
    v = splitter(temp_string)
    size = len(v)
    if size == 3:
        len1 = len(v[1])
        len2 = len(v[2])
        if len1 == 4 and len2 == 2:
            len1 = hex2dec(v[1])
            len2 = hex2dec(v[2])
            if len1 == -1 or len2 == -1:
                return True
            storage[len1] = len2
            return False
        else:
            return True
    else:
        return True
