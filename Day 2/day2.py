def str_to_lst(string):
    return [int(i) for i in string.split()]

def is_safe(lst):
    increasing = True if lst[0] < lst[1] else False
    for i in range(len(lst) - 1):
        if increasing:
            if not 0 < lst[i+1] - lst[i] < 4:
                return False
        else:
            if not 0 < lst[i] - lst[i+1] < 4:
                return False
    return True

def part1(file):
    count = 0
    for line in file:
        lst = str_to_lst(line.strip())
        if is_safe(lst):
            count += 1
            continue
    return count

def part2(file):
    count = 0
    for line in file:
        lst = str_to_lst(line.strip())
        if is_safe(lst):
            count += 1
            continue
        for i in range(len(lst)):
            if is_safe(lst[:i] + lst[i+1:]):
                count += 1
                break
    return count

if __name__ == '__main__':
    with open('day2_input.txt', 'r') as f:
        print(part1(f))
    with open('day2_input.txt', 'r') as f:
        print(part2(f))