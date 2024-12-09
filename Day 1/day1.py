import numpy as np

array = np.loadtxt('day1_input.txt', dtype='int32')

def sum_distance(lst1, lst2):
    lst1, lst2 = sorted(lst1), sorted(lst2)
    distances = [abs(x - y) for x, y in zip(lst1, lst2)]
    return sum(distances)

def similarity_score(lst1, lst2):
    score = 0
    lst2 = list(lst2)
    for num in lst1:
        score += lst2.count(num) * num
    return score

if __name__ == '__main__':
    lst1, lst2 = array.T
    print(sum_distance(lst1, lst2))
    print(similarity_score(lst1, lst2))