from typing import List, Tuple
from dec2hex import dec2hex
from hex2dec import hex2dec
#include "master.h"
#include "global.h"
#include "tools.h"
from master import *
from global_ import *
from register_is import resister_is
import tools
import splitter
import check_storage
import rpair
import set_flag_register

def dad(temp_string):

    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        temp = resister_is(v[1])
        if temp == 7:
            return True
        elif temp == 1 or temp == 3 or temp == 5:
            from_reg = rpair(temp)
            with_reg = rpair(5)
            result = gpr[from_reg] + gpr[with_reg]
            if result > 65535:
                flag[0] = 1
            data = dec2hex(result, 4)
            X1 = data[0] + data[1]
            X2 = data[2] + data[3]
            gpr[5] = hex2dec(X1)
            gpr[6] = hex2dec(X2)
            return False
        else:
            return True
    else:
        return True
