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

def solve_2(inputs):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    field_rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020, 
        "eyr": lambda x: 2020 <= int(x) <= 2030, 
        "hgt": lambda x: re.match(r"^\d+(cm|in)$", x) is not None and ((150 <= int(x[:-2]) <= 193) if x.endswith("cm") else (59 <= int(x[:-2]) <= 76)), 
        "hcl": lambda x: re.match(r"^#(?:[0-9a-f]{3}){1,2}$", x) is not None, 
        "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"), 
        "pid": lambda x: re.match(r"^\d{9}$", x) is not None,
        "cid": lambda x: True
    }

    passports = inputs.split("\n\n") # isolate each passport block
    passports = map(lambda x: x.replace("\n", " "), passports) # bring multi-line passports together

    valid_passports = 0
    for p in passports:
        if all(map(lambda f: f+":" in p, required_fields)):
            # turn the passport string into a dict
            items = {x.split(":")[0]:x.split(":")[1].strip() for x in p.split(" ")}
            # a list to save the pass/fail statuses
            status = []
            for i in items:
                try:
                    passed = field_rules[i](items[i])
                except Exception:
                    passed = False
                status.append(passed)
            if all(status):
                valid_passports += 1
    return valid_passports

with open("test_invalid.txt") as f:
    test_invalid = f.read()
with open("test_valid.txt") as f:
    test_valid = f.read()

assert solve_2(test_invalid) == 0
assert solve_2(test_valid) == 4
print(solve_2(inputs))