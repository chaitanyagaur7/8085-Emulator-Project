from tools import dec2hex

def help():
    print("\t*** HELP ***\n")
    print("1. break or b 'line number' :\n\tIt will set break point on give line number.\n")
    print("2. run	or r :\n\tRun the program until it ends or breakpoint is enountered.\n")
    print("3. step or s :\n\tIt will run the program one instruction at a time.\n")
    print("4. print or p 'Resister / Memory Address' :\n\tIt prints the value of register or Memory location. \n\tfor ex p A will print the value of register A. \n\tp x2500 will print the value at memory location x2500 if any.\n")
    print("5. quit or q :\n\tQuits the debugger.\n")
    print("6. help :\n\tIt will show all commands of debugger.\n")
