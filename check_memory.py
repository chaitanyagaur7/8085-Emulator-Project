from master import *
from global_ import *
from typing import List, Tuple

from master import *
from global_ import *
from register_is import resister_is
import tools
import splitter
import check_storage
import rpair
import set_flag_register

# MAIN MEMORY OF 8085
memory = {}

def check_memory(key):
    if key not in memory:
        return -1
    else:
        return key
