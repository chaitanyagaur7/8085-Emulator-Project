from check_memory import check_memory
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

def print_func(v):
    s = v[1]
    l = len(s)
    if l == 1:
        r = resister_is(s)
        if r >= 0 and r <= 6:
            print(f"\t>{dec2hex(gpr[r], 2)}")
        else:
            print("*** ERROR: INVALID RESGISTER ***")
    elif l == 3:
        if s == "LOC":
            print(f"\tCURRENT LINE NUMBER: {index_pc}")
        else:
            print("*** ERROR: INVALID COMMAND ***")
    elif l == 4:
        if s == "FLAG":
            print(f"\tFLAG: {flag[4]}   {flag[3]}   {flag[2]}   {flag[1]}   {flag[0]}")
        else:
            print("*** ERROR: INVALID COMMAND ***")
    elif l == 5:
        temp = s[1:5]
        if s[0] == "X":
            value = hex2dec(temp)
            check = check_storage(value)
            if check != -1:
                print(f"\t>{dec2hex(storage[value], 4)}")
            else:
                check = check_memory(value)
                if check != -1:
                    print(f"\t>{memory[check]}")
                else:
                    print("\t>0000")
        else:
            print("*** ERROR: INVALID HEXADECIMAL ADDRESS ***")
    else:
        print("*** ERROR: INVALID ADDRESS TO REFERENCE ***")
