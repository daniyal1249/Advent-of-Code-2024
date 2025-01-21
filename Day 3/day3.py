def extract_tuples(line):
    substrings = line.split('mul')[1:]
    pairs = []
    for string in substrings:
        if string[0] != '(':
            continue
        try:
            right_idx = string.index(')')
        except ValueError:
            continue

        pairs.append(string[:right_idx + 1])
    return pairs

def enabled_tuples(line):
    substrings = line.split('mul')[1:]  # no do/don't before first mul
    enabled = True

    pairs = []
    for string in substrings:
        valid = True
        if string[0] != '(':
            valid = False
        try:
            right_idx = string.index(')')
        except ValueError:
            valid = False

        if valid and enabled:
            pairs.append(string[:right_idx + 1])

        for i in range(len(string)):
            if string[i:i + 4] == 'do()':
                enabled = True
            elif string[i:i + 7] == 'don\'t()':
                enabled = False
    return pairs

def parse_tuple(string):
    string = string[1:-1]
    nums = string.split(',')
    if len(nums) != 2:
        return 0, 0
    
    digits = '0123456789'
    for num in nums:
        if not 0 < len(num) < 4:
            return 0, 0
        if not all([char in digits for char in num]):
            return 0, 0
        
    return int(nums[0]), int(nums[1])

def part1(file):
    total_sum = 0
    for line in f:
        pairs = extract_tuples(line)
        for pair in pairs:
            x, y = parse_tuple(pair)
            total_sum += (x * y)
    return total_sum

def part2(file):
    total_sum = 0
    pairs = enabled_tuples(f.read())
    for pair in pairs:
        x, y = parse_tuple(pair)
        total_sum += (x * y)
    return total_sum

if __name__ == '__main__':
    with open('day3_input.txt', 'r') as f:
        print(part1(f))
    with open('day3_input.txt', 'r') as f:
        print(part2(f))