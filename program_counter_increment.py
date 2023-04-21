from global_ import program_counter

index_pc = 0
size_pc = 0

def program_counter_increment(temp_memory):
    global index_pc, size_pc, program_counter
    program_counter[index_pc] = temp_memory
    index_pc += 1
    if index_pc > size_pc:
        size_pc = index_pc
