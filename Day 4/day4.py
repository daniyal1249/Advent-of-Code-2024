def extend_array(array, n):
    extended = []
    for row in array:
        extended.append(([''] * n) + row + ([''] * n))

    row_length = len(array[0])  # array must be nonempty
    empty_rows = [[''] * (row_length + 2 * n)]
    return (empty_rows * n) + extended + (empty_rows * n)

def count_word(word, array, idx):
    i, j = idx
    if array[i][j] != word[0]:
        return 0
    
    directions = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)}
    word_length = len(word)
    pos_idx = [[(dir[0] * i, dir[1] * i) for i in range(word_length)] for dir in directions]

    count = 0
    for dir in pos_idx:
        for delta_idx, char in zip(dir, word):
            delta_i, delta_j = delta_idx
            if array[i + delta_i][j + delta_j] != char:
                break
        else:
            count += 1
    return count

def is_x(word, array, idx):
    i, j = idx
    mid_idx = (len(word) - 1) // 2
    if array[i][j] != word[mid_idx]:  # word must have odd length
        return False

    pos_dir = [array[i + delta_i - mid_idx][j + delta_j - mid_idx] 
               for delta_i, delta_j in [(1 * n, 1 * n) for n in range(len(word))]]
    neg_dir = [array[i + delta_i - mid_idx][j + delta_j + mid_idx] 
               for delta_i, delta_j in [(1 * n, -1 * n) for n in range(len(word))]]

    word_lst = list(word)
    word_lst_rev = word_lst[::-1]
    if pos_dir == word_lst or pos_dir == word_lst_rev:
        if neg_dir == word_lst or neg_dir == word_lst_rev:
            return True
    return False

def part1(file):
    array = [list(line.strip()) for line in f.readlines()]  # each line must end in \n
    array = extend_array(array, 3)

    count = 0
    for i, row in enumerate(array):
        for j in range(len(row)):
            count += count_word('XMAS', array, (i, j))
    return count

def part2(file):
    array = [list(line.strip()) for line in f.readlines()]  # each line must end in \n
    array = extend_array(array, 2)

    count = 0
    for i, row in enumerate(array):
        for j in range(len(row)):
            count += 1 if is_x('MAS', array, (i, j)) else 0
    return count
    
if __name__ == '__main__':
    with open('day4_input.txt', 'r') as f:
        print(part1(f))
    with open('day4_input.txt', 'r') as f:
        print(part2(f))