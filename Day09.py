from itertools import combinations

lines = [line.strip() for line in open("inputs/Day09.txt", "r")]
cleaned_lines =  [tuple(map(int, line.split(","))) for line in lines]

def partOne():
    results = []
    for (i, p1), (j, p2) in combinations(enumerate(cleaned_lines), 2):
        area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        results.append(area)    
    results.sort()
    print(results[-1])

partOne()