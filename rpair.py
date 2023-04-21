import dec2hex
import hex2dec
from global_ import gpr

def rpair(start):
    temp = dec2hex(gpr[start], 2) + dec2hex(gpr[start+1], 2)
    return hex2dec(temp)

