from master import *
from global_ import *
from splitter import splitter
from tools import *
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

def cma(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 1:
        temp = bin(gpr[0])[2:].zfill(8)
        temp = ''.join(['0' if i == '1' else '1' for i in temp])
        gpr[0] = int(temp, 2)
        return False
    else:
        return True
