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
def input():
    termination_flag = False
    start_memory = 0
    memory_address = 0

    while not termination_flag:
        temp_string = input("Enter starting Memory Address in Hexdecimal: ")
        start_memory = hex2dec(temp_string) # STARTING ADDRESS

        if start_memory == -1:
            print("***ERROR: Invalid Memory Address ***")
            termination_flag = True
        else:
            memory_address = start_memory
            print("Enter Assembly language code below")

        while not termination_flag:
            temp_string = input(f"{dec2hex(memory_address, 4)} >> ").upper()
            program_counter_increment(memory_address)
            memory[memory_address] = temp_string
            v = splitter(temp_string) # To Split the string into parts
            size = check_opcode(v[0]) # To fetch Size of OPCODE

            if size == -1:
                print("*** ERROR: INVALID 8085 COMMAND. ***")
                print("Terminating Program...")
                termination_flag = True
                break
            elif size == -2: # RETURN -2 for HLT
                break
            else:
                memory_address += size

            temp_string = ""

    return termination_flag
