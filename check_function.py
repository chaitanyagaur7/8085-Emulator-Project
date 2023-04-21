
from master import *
from global_ import *
from set import set1
from tools import *
from arithmetic import *
from branching import *
from logical import *
from load import *
from splitter import splitter
def check_function(instruction):
    v = splitter(instruction)
    if v[0] == "MOV":
        return mov(instruction)
    elif v[0] == "MVI":
        return mvi(instruction)
    elif v[0] == "LXI":
        return lxi(instruction)
    elif v[0] == "LDA":
        return lda(instruction)
    elif v[0] == "STA":
        return sta(instruction)
    elif v[0] == "SHLD":
        return shld(instruction)
    elif v[0] == "LHLD":
        return lhld(instruction)
    elif v[0] == "STAX":
        return stax(instruction)
    elif v[0] == "XCHG":
        return xchg(instruction)
    elif v[0] == "ADD":
        return add(instruction)
    elif v[0] == "ADI":
        return adi(instruction)
    elif v[0] == "SUB":
        return sub(instruction)
    elif v[0] == "INR":
        return inr(instruction)
    elif v[0] == "DCR":
        return dcr(instruction)
    elif v[0] == "INX":
        return inx(instruction)
    elif v[0] == "DCX":
        return dcx(instruction)
    elif v[0] == "DAD":
        return dad(instruction)
    elif v[0] == "SUI":
        return sui(instruction)
    elif v[0] == "CMA":
        return cma(instruction)
    elif v[0] == "CMP":
        return cmp(instruction)
    elif v[0] == "JMP":
        return jmp(instruction)
    elif v[0] == "JC":
        return jc(instruction)
    elif v[0] == "JNZ":
        return jnz(instruction)
    elif v[0] == "JZ":
        return jz(instruction)
    elif v[0] == "JNC":
        return jnc(instruction)
    elif v[0] == "HLT":
        return False
    elif v[0] == "SET":
        return set1(instruction)
    else:
        return True
