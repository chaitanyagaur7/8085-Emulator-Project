from tools import splitter
from global_ import flag, program_counter, size_pc

def jnz(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        if flag[3] == 0:
            address = int(v[1], 16)
            if address == -1:
                return True
            is_there = False
            for i in range(size_pc):
                if program_counter[i] == address:
                    is_there = True
                    index_pc = i-1
                    return False
            if not is_there:
                return True
        else:
            return False
    return True
