from master import *
from global_ import *
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

storage = {}

def check_storage(key):
    if key not in storage:
        return -1
    else:
        return storage[key]
