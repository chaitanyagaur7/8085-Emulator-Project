from typing import List, Tuple
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

def breakpoint(v: List[str]) -> int:
    s = v[1]
    l = len(s)
    breakpoint = 0
    for i in range(l):
        if s[i] >= '0' and s[i] <= '9':
            breakpoint = breakpoint * 10 + (ord(s[i]) - 48)
        else:
            return -1
    return breakpoint
