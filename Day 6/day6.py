class Map:
    guard_dict = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

    def __init__(self, map):
        self.map = map
        self.init_guard_pos()

    @property
    def guard(self):
        i, j = self.guard_pos
        return self.map[i][j]

    def init_guard_pos(self):
        for i, row in enumerate(self.map):
            for j, item in enumerate(row):
                if item in Map.guard_dict:
                    self.guard_pos = (i, j)

    def move_guard(self):
        i, j = self.guard_pos
        delta_i, delta_j = Map.guard_dict[self.guard]
        try:
            if self.map[i + delta_i][j + delta_j] == '#':
                if self.guard == '^':
                    self.map[i][j] = '>'
                elif self.guard == 'v':
                    self.map[i][j] = '<'
                elif self.guard == '>':
                    self.map[i][j] = 'v'
                elif self.guard == '<':
                    self.map[i][j] = '^'
                
            else:
                self.map[i + delta_i][j + delta_j] = self.guard
                self.guard_pos = (i + delta_i, j + delta_j)
        except IndexError:
            return 'exit'

    def get_positions(self):
        positions = 0
        for row in self.map:
            for item in row:
                positions += 1 if item in Map.guard_dict else 0
        return positions

def part1(file):
    array = [list(row.strip()) for row in f.readlines()]
    guard_map = Map(array)
    while True:
        move_status = guard_map.move_guard()
        if move_status == 'exit':
            break
    return guard_map.get_positions()

def part2(file):
    pass

if __name__ == '__main__':
    with open('day6_input.txt', 'r') as f:
        print(part1(f))
    with open('day6_input.txt', 'r') as f:
        print(part2(f))