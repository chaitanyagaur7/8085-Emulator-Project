flag = 0b00000  # initialize flag as a binary number
import global_

def set_flag_register(result):
    global flag  # declare flag as global at the beginning of the function
    if result > 255:  # set carry flag
        flag |= 0b00001
    else:
        flag &= 0b11110

    if result < 0:  # set sign flag
        flag |= 0b10000
    else:
        flag &= 0b01111

    numberof1 = bin(result).count('1')  # count number of 1's
    if numberof1 % 2 == 0:  # set parity flag
        flag |= 0b00010
    else:
        flag &= 0b11101

    numberof0 = 8 - numberof1  # count number of 0's
    if numberof0 == 8:  # set zero flag
        flag |= 0b01000
    else:
        flag &= 0b10111
