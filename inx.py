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
def inx(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        temp = resister_is(v[1])
        if temp == 7:
            return True
        elif temp == 1 or temp == 3 or temp == 5:
            data = ""
            from_val = rpair(temp) + 1
            if from_val > 65535:
                from_val = 0
                data = "0000"
            else:
                data = dec2hex(from_val, 4)
            name = bin(from_val)[2:].zfill(16) # store our result in binary form
            if from_val < 0: # to set sign flag
                flag[4] = 1
            else:
                flag[4] = 0
            numberof1 = name.count('1') # count no of 1
            if numberof1 % 2 == 0:
                flag[1] = 1
            else:
                flag[1] = 0
            numberof0 = 16 - numberof1 # count no 0
            if numberof0 == 16:
                flag[3] = 1
            else:
                flag[3] = 0
            X1, X2 = "", ""
            X1 = X1 + data[0] + data[1]
            X2 = X2 + data[2] + data[3]
            gpr[temp] = hex2dec(X1)
            gpr[temp+1] = hex2dec(X2)
            return False
        else:
            return True
    return True
