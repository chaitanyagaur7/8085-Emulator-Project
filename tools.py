import math
import bitarray
import string
import collections
import os

# You don't need to declare the variables as extern in Python
gpr = [0] * 7   # | A | B | C | D | E | H | L |
                # | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
flag = bitarray.bitarray('00000')   # | S | Z | AY | P | CY |
                                    # | 4 | 3 | 2  | 1 | 0  |
opcode = {}
debugger = {}
memory = {}
program_counter = [0] * 500
index_pc = 0
size_pc = 0
storage = {}
breakpoints = {}
