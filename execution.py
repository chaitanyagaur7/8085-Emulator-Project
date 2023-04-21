from check_function import check_function
from dec2hex import dec2hex
from master import *
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

from tools import *
from arithmetic import *
from branching import *
from logical import *
from load import *

def execution():
    global index_pc
    index_pc = 0

    while index_pc < size_pc:
        function1 = memory[program_counter[index_pc]]
        check = check_function(function1)

        if index_pc > size_pc:
            print("Invalid memory location")

        if check:
            print(f"*** SYNTAX ERROR at Line Number {index_pc} -> {function1} ***")
            break

        index_pc += 1

    for i in range(7):
        print(dec2hex(gpr[i], 2), end=" ")

    print()
