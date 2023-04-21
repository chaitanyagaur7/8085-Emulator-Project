from joblib import MemorizedResult
from check_opcode import check_opcode
import hex2dec
from program_counter_increment import program_counter_increment
from splitter import splitter
def input_file(arg):

    termination_flag = False
    with open(arg, 'r') as input_file:
        temp_string = input_file.readline().rstrip()
        start_memory = hex2dec(temp_string)  # STARTING ADDRESS
        if start_memory == -1:
            print("***ERROR: Invalid Memory Address ***")
            termination_flag = True
        else:
            memory_address = start_memory
        for temp_string in input_file:
            temp_string = temp_string.rstrip().upper()
            program_counter_increment(memory_address)
            MemorizedResult[memory_address] = temp_string
            v = splitter(temp_string)  # To Split the string into parts
            size = check_opcode(v[0])  # To fetch Size of OPCODE
            if size == -1:
                print("*** ERROR: INVALID 8085 COMMAND. ***\nTerminating Program...")
                termination_flag = True
                break
            elif size == -2:  # RETURN -2 for HLT
                break
            else:
                memory_address += size
            temp_string = ""
    return termination_flag
