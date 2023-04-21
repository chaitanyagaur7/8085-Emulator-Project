from typing import Dict
import array
import bitarray


gpr = array.array('i', [0] * 7)      # | A | B | C | D | E | H | L |
                                      # | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
flag = bitarray.bitarray('00000')    # | S | Z | AY | P | CY |
                                      # | 4 | 3 | 2  | 1 | 0  |

opcode: Dict[str, int] = {}          # FOR CHECK_OPCODE for the size of opcode
debugger: Dict[str, int] = {}        # FOR DEBUGGER for the CODE of instruction
memory: Dict[int, str] = {}          # MAIN MEMORY OF 8085
program_counter = [0] * 500
