from collections import Counter

with open("test_inputs.txt") as f:
    test_inputs = f.read()

with open("inputs.txt") as f:
    inputs = f.read()

def get_groups(inputs):
    groups = inputs.split("\n\n")
    return groups

def get_group_size(group):
    group_size = len(group.splitlines())
    return group_size

def get_group_answers(group):
    group_answers = "".join(group.replace("\n", "")).strip()
    return group_answers


def solve_1(inputs):
    groups = get_groups(inputs)
    answers = list(map(get_group_answers, groups))
    answer_count = sum(map(len, map(set, answers)))
    return answer_count


def solve_2(inputs):
    groups = get_groups(inputs)
    group_sizes = map(get_group_size, groups)
    group_answers = map(get_group_answers, groups)
    group_answer_counts = map(Counter, group_answers)

    tracker = 0
    for size, answers in zip(group_sizes, group_answer_counts):
        all_answered = set([a for a in answers if answers[a]==size])
        tracker += len(all_answered)
    return tracker
    

assert solve_1(test_inputs) == 11
print(solve_1(inputs))

assert solve_2(test_inputs) == 6
print(solve_2(inputs))