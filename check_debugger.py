from typing import Dict
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

debugger: Dict[str, int] = {}

def check_debugger(key: str) -> int:
    if key not in debugger:
        return -1
    else:
        return debugger[key]
