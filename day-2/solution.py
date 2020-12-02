import re

with open("inputs.txt") as f:
    inputs = f.readlines()

test_inputs = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

pattern = r"(\d+)\-(\d+) (.)\: (.*)"

def solve_1(inputs, pattern):
    valid_passwords = 0
    for i in inputs:
        match = re.search(pattern, i)
        if match:
            lower = int(match.groups()[0])
            upper = int(match.groups()[1])
            letter = match.groups()[2]
            password = match.groups()[3]

            if lower <= password.count(letter) <= upper:
                valid_passwords += 1

    return(valid_passwords)
assert solve_1(test_inputs, pattern) == 2
print(solve_1(inputs, pattern))

def solve_2(inputs, pattern):
    valid_passwords = 0
    for i in inputs:
        match = re.search(pattern, i)
        if match:
            position_1 = int(match.groups()[0]) - 1
            position_2 = int(match.groups()[1]) - 1
            letter = match.groups()[2]
            password = match.groups()[3]

            # XOR
            if (password[position_1]==letter) ^ (password[position_2]==letter):
                valid_passwords += 1

    return(valid_passwords)

assert solve_2(test_inputs, pattern) == 1
print(solve_2(inputs, pattern))