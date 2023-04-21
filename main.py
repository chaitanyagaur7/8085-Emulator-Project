from does_file_exist import does_file_exist
from execution import execution
from input_file import input_file
from master import *
from global_ import *
from string_uppercase import string_uppercase
from tools import *
from debugger import *
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
from initialize_map_opcode import initialize_map_opcode
import sys
def main():
    initialize_map_opcode()  # MAP OPCODE INITIALIZATION


    argc = len(sys.argv)

    if argc == 1:  # IF NO ARGUMENT IS PASSED
        termination_flag = False
        termination_flag = input()
        if not termination_flag:
            index_pc = 0
            execution()
        else:
            print("*** ERROR: Invalid Input ***")

    elif argc == 2:  # TWO ARGUMENTS
        arg2 = sys.argv[1]
        if string_uppercase(arg2) == "--DEBUGGER":  # DEBUGGER MODE WITHOUT FILE HANDLING
            termination_flag = False
            termination_flag = input()
            if not termination_flag:
                # DEBUGGER FUNCTIONALITY
                index_pc = 0
                this_is_debugger()
            else:
                print("*** ERROR: Invalid Input. ***")
        else:  # FILE HANDLING W/O DEBUGGER # *** CHECK BLANK FILE AND SET EOF CONDITION ***
            if does_file_exist(sys.argv[1]):
                termination_flag = False
                termination_flag = input_file(sys.argv[1])
                if not termination_flag:
                    index_pc = 0
                    execution()  # FURTHER CODE
                else:
                    print("*** ERROR: Invalid Input. ***")
            else:
                print("*** ERROR: Invalid File. File does not exist. ***")

    elif argc == 3:  # FILE HANDLING WITH DEBUGGER
        arg3 = sys.argv[2]
        if string_uppercase(arg3) == "--DEBUGGER":
            if does_file_exist(sys.argv[1]):
                termination_flag = False
                termination_flag = input_file(sys.argv[1])
                if not termination_flag:
                    index_pc = 0
                    this_is_debugger()
                else:
                    print("*** ERROR: Invalid Input. ***")
            else:
                print("*** ERROR: Invalid File. File does not exist. ***")
        else:
            print("*** ERROR: Invalid Argument Format. ***\n Valid Format: [<Exectable File> <Input File> <--debugger>]")
    else:
        print("*** ERROR: Invalid Number of Arguments ***")

    print("\t*** THE END ***")

if __name__ == "__main__":
    main()
