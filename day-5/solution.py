with open("inputs.txt") as f:
    inputs = f.read()

def partition(partitions, size, lower_code):
    options = list(range(size))
    for p in partitions:
        if p == lower_code:
            options = options[:int(len(options)/2)]
        else:
            options = options[int(len(options)/2):]
    if len(options) == 1:
        return options[0]
    else:
        raise ValueError("wrong range size")

def get_row_number(pass_code):
    return partition(pass_code[:7], 128, "F")
def get_column_number(pass_code):
    return partition(pass_code[7:], 8, "L")

def get_seat_id(pass_code):
    row_number = get_row_number(pass_code)
    column_number = get_column_number(pass_code)
    seat_id = (8 * row_number) + column_number
    return seat_id


test_inputs = [
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
]

assert get_row_number(test_inputs[0]) == 70
assert get_row_number(test_inputs[1]) == 14
assert get_row_number(test_inputs[2]) == 102

assert get_column_number(test_inputs[0]) == 7
assert get_column_number(test_inputs[1]) == 7
assert get_column_number(test_inputs[2]) == 4

assert get_seat_id(test_inputs[0]) == 567
assert get_seat_id(test_inputs[1]) == 119
assert get_seat_id(test_inputs[2]) == 820


seat_ids = [get_seat_id(p) for p in inputs.splitlines()]
print(max(seat_ids))

sorted_seat_ids = sorted(seat_ids)
missing = [
    s for i, s in enumerate(sorted_seat_ids)
    if sorted_seat_ids[i-1] != s-1
][1] - 1

print(missing)