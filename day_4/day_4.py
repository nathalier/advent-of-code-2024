import numpy as np
import re


def part_1(matrix):
    counter = 0
    for line in lines_gen(matrix):
        matches = re.findall('XMAS', line)
        counter += len(matches)
        # print(f'{line = }, {matches = }, {len(matches) = }')
    return counter

def lines_gen(m):
    for r in m:
        line = ''.join(r)
        yield line
        yield line[::-1]
    for c in m.T:
        line = ''.join(c)
        yield line
        yield line[::-1]
    for i in range(-(m.shape[0]-1), m.shape[1]):
        line = ''.join(np.diagonal(m, offset=i))
        yield line
        yield line[::-1]
    reverse_m = m[:, ::-1]
    for i in range(-(reverse_m.shape[0]-1), reverse_m.shape[1]):
        line = ''.join(np.diagonal(reverse_m, offset=i))
        yield line
        yield line[::-1]
    
def part_2(matrix):
    count = 0
    for sm in submatrices_gen(matrix, w_shape=(3,3)):
        x_strings = get_diag_strings(sm)
        count += 1 if x_strings.count('MAS') >= 2 else 0
    return count

def submatrices_gen(m, w_shape=(3,3)):
    n_rows, n_cols = m.shape
    k_rows, k_cols = w_shape
    for i in range(n_rows - k_rows + 1):
        for j in range(n_cols - k_cols + 1):
            yield m[i:i+k_rows, j:j+k_cols] 

def get_diag_strings(sm):
    left_diag_str = ''.join(np.diagonal(sm))
    right_diag_str = ''.join(np.diagonal(sm[:, ::-1]))
    return [left_diag_str,
            left_diag_str[::-1],
            right_diag_str,
            right_diag_str[::-1] ]

def read_data(filename):
    with open(filename) as f:
        data = list(map(lambda x: list(x.strip()), f.readlines()))
        matrix = np.char.array(data)
        # print(matrix)
    return matrix


#############################
test_data = read_data('input_t.txt')

assert (res := part_1(test_data)) == 18, f'Actual: {res}'
assert (res := part_2(test_data)) == 9, f'Actual: {res}'
#############################


data = read_data('input.txt')

print(part_1(data))
print(part_2(data))
