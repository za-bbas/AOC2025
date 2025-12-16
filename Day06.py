lines = [line.strip() for line in open("inputs/test.txt", "r")]

def partOne():
    equations = [line.split() for line in lines]
    count = 0
    temp = 0
    for c in range(len(equations[0])):
        temp = int(equations[0][c])
        for r in range(1, len(equations)-1):
            if equations[-1][c] == '+':
                temp += int(equations[r][c])
            else:
                temp *= int(equations[r][c])
        count += temp
    print(count)

partOne()