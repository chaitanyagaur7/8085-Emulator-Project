from master import *
from typing import Dict
import array
import bitarray
import initailize_map_debugger as initilize_map_debugger
from typing import Dict
import array
import bitarray
from splitter import splitter

gpr = array.array('i', [0] * 7)      # | A | B | C | D | E | H | L |
                                      # | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
flag = bitarray.bitarray('00000')    # | S | Z | AY | P | CY |
                                      # | 4 | 3 | 2  | 1 | 0  |

opcode: Dict[str, int] = {}          # FOR CHECK_OPCODE for the size of opcode
debugger: Dict[str, int] = {}        # FOR DEBUGGER for the CODE of instruction
memory: Dict[int, str] = {}          # MAIN MEMORY OF 8085
program_counter = [0] * 500


gpr = array.array('i', [0] * 7)      # | A | B | C | D | E | H | L |
                                      # | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
flag = bitarray.bitarray('00000')    # | S | Z | AY | P | CY |
                                      # | 4 | 3 | 2  | 1 | 0  |

opcode: Dict[str, int] = {}          # FOR CHECK_OPCODE for the size of opcode
debugger: Dict[str, int] = {}        # FOR DEBUGGER for the CODE of instruction
memory: Dict[int, str] = {}          # MAIN MEMORY OF 8085
program_counter = [0] * 500

from tools import *
from debugger import *

def this_is_debugger():
    initilize_map_debugger()
    print("\n\t*** DEBUGGER MODE ***")
    temp_string=""
    code=-1
    breakpoints[size_pc-1]=True
    print("Enter Debugger code below or type help for list of instructions")
    while True:
        temp_string=input("$ ").upper()
        v=splitter(temp_string)
        size=len(v)
        code=check_debugger(v[0])
        if code==-1:
            print("*** ERROR: Invalid Debugger Command. *** \nType correct command or type help for list of commands.")
            continue
        elif code==0:
            # Break
            if size==2:
                n=breakpoint(v)
                if n==-1:
                    print("*** ERROR: Invalid Line Number. ***")
                elif n>=size_pc:
                    print("*** ERROR: Line Number out of Bound. Enter Line Number less than "+str(size_pc)+". ***")
                else:
                    breakpoints[n]=True
            else:
                print("*** ERROR: Invalid Number of arguments. ***")
        elif code==1:
            # RUN
            if size==1:
                debugger_execution()
            else:
                print("*** ERROR: Invalid Number of arguments. ***")
        elif code==2:
            # STEP
            if size==1:
                debugger_execution(index_pc)
            else:
                print("*** ERROR: Invalid Number of arguments. ***")
        elif code==3:
            # PRINT
            if size==2:
                print(v)
            else:
                print("*** ERROR: Invalid Number of arguments. ***")
        elif code==4:
            # QUIT
            if size==1:
                break
            else:
                print("*** ERROR: Invalid Number of arguments. ***")
                break
        elif code==5:
            # HELP
            if size==1:
                help()
            else:
                print("*** ERROR: Invalid Number of arguments. ***")
        temp_string=""
