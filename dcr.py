from typing import List, Tuple
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


def dcr(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        temp = resister_is(v[1])
        if temp == -1:
            return True
        elif temp == 7:
            from_ = check_storage(rpair(5))
            from_ = from_ - 1
            if from_ < 0:
                storage[rpair(5)] = 255
            else:
                storage[rpair(5)] = from_
        else:
            from_ = gpr[temp] - 1
            if from_ < 0:
                gpr[temp] = 255
            else:
                gpr[temp] = from_
        set_flag_register(from_)
        return False
    return True
