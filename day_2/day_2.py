import numpy as np


def part_1(lines):
    safe_count = 0
    for row in lines:
        safe_count += \
            all([1 <= b-a <= 3 for a, b in zip(row, row[1:])]) or \
            all([1 <= a-b <= 3 for a, b in zip(row, row[1:])])
    return safe_count
    

def part_2(lines):
    safe_count = 0

    for row in lines:
        if not is_possibly_increasing(row, tolerance=1):
            row = list(reversed(row))
        diffs = np.diff(row)
        violators = np.where((diffs < 1) | (diffs > 3))[0]

        if len(violators) == 0:
            safe_count += 1
        elif len(violators) == 1: 
            i = violators[0]
            safe_count += (
                ( i > 0 and 1 <= diffs[i-1] + diffs[i] <=3) or \
                (i < diffs.shape[0]-1 and 1 <= diffs[i] + diffs[i+1] <= 3) or \
                i == 0 or i == diffs.shape[0]-1)
        elif len(violators) == 2 and violators[1] == violators[0] + 1:
            safe_count += (1 <= diffs[violators[0]] + diffs[violators[1]] <= 3)

    return safe_count


def is_possibly_increasing(seq, tolerance=0):
    if len(seq) < 2 + tolerance*2:
        raise ValueError("Too short sequence")
    return sum([seq[-(i + 1)] > seq[0] for i in range(1 + tolerance*2)]) >= tolerance + 1


def read_data(filename):
    with open(filename) as f:
        lines = list(map(lambda x: list(map(int, x.strip().split())), f.readlines()))
    return lines


#############################
test_data = read_data('input_t.txt')

assert (res := part_1(test_data)) == 2, f'Actual: {res}'
assert (res := part_2(test_data)) == 4, f'Actual: {res}'
#############################

data = read_data('input.txt')

print(part_1(data))
print(part_2(data))
