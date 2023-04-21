from tools import splitter
from global_ import storage, gpr

def shld(temp_string):
    v = splitter(temp_string)
    size = len(v)
    if size == 2:
        address = int(v[1], 16)
        if len(v[1]) == 4 and address != -1:
            storage[address] = gpr[6]
            storage[address+1] = gpr[5]
            return False
        else:
            return True
    else:
        return True
