import re

with open("inputs.txt") as f:
    inputs = f.read()

with open("test_inputs.txt") as f:
    test_inputs = f.read()

def solve_1(inputs):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    all_fields = required_fields + ["cid"]

    passports = inputs.split("\n\n") # isolate each passport block
    passports = map(lambda x: x.replace("\n", " "), passports) # bring multi-line passports together

    valid_passports = 0
    for p in passports:
        if all(map(lambda f: f+":" in p, required_fields)):
            valid_passports += 1

    return valid_passports

assert solve_1(test_inputs) == 2
print(solve_1(inputs))