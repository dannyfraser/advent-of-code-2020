with open("test_inputs.txt") as f:
    test_inputs = f.read()

with open("inputs.txt") as f:
    inputs = f.read()

def read_instructions(inp):
    return inp.splitlines()

def parse_instruction(inst):
    operation, argument = inst.split(" ")
    return operation, int(argument)


def execute(instructions):

    executed = set()
    current_instruction = 0
    accumulator = 0
    correct_termination = False

    while current_instruction not in executed and current_instruction < len(instructions):
        if current_instruction == len(instructions) - 1:
            correct_termination = True
        executed.add(current_instruction)
        op, arg = parse_instruction(instructions[current_instruction])
        
        if op == "acc":
            accumulator += arg
            current_instruction += 1
        if op == "nop":
            current_instruction += 1
        if op == "jmp":
            current_instruction += arg

    return accumulator, correct_termination

assert(execute(read_instructions(test_inputs)) == (5, False))
print(execute(read_instructions(inputs)))

def modify_instruction(instructions, i):
    op, arg = parse_instruction(instructions[i])
    if op == "jmp":
        instructions[i] = f"nop {arg}"
    if op == "nop":
        instructions[i] = f"jmp {arg}"
    return instructions

def generate_modified_instructions(instructions):
    for i in range(len(instructions) - 1):
        modded = modify_instruction(instructions.copy(), i)
        yield modded

assert(list(filter(lambda x: x[1] == True, list(map(execute, generate_modified_instructions(read_instructions(test_inputs))))))[0] == (8, True))
print(list(filter(lambda x: x[1] == True, list(map(execute, generate_modified_instructions(read_instructions(inputs)))))))
    
