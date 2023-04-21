from typing import List, Tuple
from dec2hex import dec2hex
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
import hex2dec
def dcx(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        temp = resister_is(v[1])
        if temp == 7:
            return True
        elif temp == 1 or temp == 3 or temp == 5:
            data = ""
            from_ = rpair(temp)
            from_ = from_ - 1
            if from_ == -1:
                from_ = 65535
                data = "FFFF"
            elif from_ == 0:
                from_ = 0
                data = "0000"
            else:
                data = dec2hex(from_, 4)
            name = bin(from_)[2:].zfill(16)  # store our result in binary form
            if from_ < 0:  # to set sign flag
                flag[4] = 1
            else:
                flag[4] = 0
            numberof1 = name.count('1')  # count no of 1
            if numberof1 % 2 == 0:
                flag[1] = 1
            else:
                flag[1] = 0
            numberof0 = 16 - numberof1  # count no 0
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
    else:
        return True
