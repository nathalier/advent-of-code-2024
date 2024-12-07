def find_path(mapa, direction, loc):
    map_size = (len(mapa), len(mapa[0]))
    visited = set()
    looped = False

    while True:
        visited.add((loc, direction))
        next_loc = (loc[0] + step[direction][0], loc[1] + step[direction][1])
        if not (0 <= next_loc[0] < map_size[0] and
                 0 <= next_loc[1] < map_size[1]):
            break
        while mapa[next_loc[0]][next_loc[1]] == 1:
            visited.add((loc, direction))
            direction = turn[direction]
            next_loc = (loc[0] + step[direction][0], loc[1] + step[direction][1])
        loc = next_loc 
        if (loc, direction) in visited:
            looped = True
            break
    
    return visited, looped


def part_1(mapa, direction, loc):
    visited, _ = find_path(mapa, direction, loc)
    return len({loc[0] for loc in visited})


def part_2(mapa, direction, loc):
    map_size = (len(mapa), len(mapa[0]))
    visited, visited_in_dir = set(), set()
    loop_options = 0

    while True:
        visited_in_dir.add((loc, direction))
        visited.add(loc)
        next_loc = (loc[0] + step[direction][0], loc[1] + step[direction][1])
        if not (0 <= next_loc[0] < map_size[0] and
                 0 <= next_loc[1] < map_size[1]):
            break
        while mapa[next_loc[0]][next_loc[1]] == 1:
            direction = turn[direction]
            next_loc = (loc[0] + step[direction][0], loc[1] + step[direction][1])
        if next_loc not in visited:
            mapa[next_loc[0]][next_loc[1]] = 1
            _, looped = find_path(mapa, direction, loc)
            loop_options += looped
            mapa[next_loc[0]][next_loc[1]] = 0
        loc = next_loc 
        if (loc, direction) in visited_in_dir:
            break
    return loop_options


def read_data(filename):
    mapa = []
    with open(filename) as f:
        i = 0
        while line := f.readline().strip():
            mapa.append([1 if c == '#' else 0 for c in line])
            guard = set(line).difference({'.', '#'})
            if len(guard) > 0:
                dir_sym = guard.pop()
                guard_loc = (i, line.find(dir_sym))
            i += 1
    return mapa, dir_sym, guard_loc


step = {'^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1) }
turn = {'^': '>',
        '>': 'v',
        'v': '<',
        '<': '^' }

#############################
mapa, dir_sym, guard_loc = read_data('input_t.txt')

assert (res := part_1(mapa, dir_sym, guard_loc)) == 41, f'Actual: {res}'
assert (res := part_2(mapa, dir_sym, guard_loc)) == 6, f'Actual: {res}'
#############################


mapa, dir_sym, guard_loc = read_data('input.txt')

print(part_1(mapa, dir_sym, guard_loc))
print(part_2(mapa, dir_sym, guard_loc))
