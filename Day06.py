lines = open("inputs/Day06.txt").read().splitlines()
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

def partTwo():
    transpose = list(map(list, zip(*lines)))
    count = 0
    temp = 0
    add = False
    for row in transpose:
        if not ''.join(row[0:4]).strip(): #note that sample input only goes to 3, not 4
            continue
        a = int(''.join(row[0:4]).strip())
        if '+' in row or '*' in row:
            count += temp
            temp = a 
            add = False
            if '+' in row: add = True
        elif add:
            temp += a
        else:
            temp *= a
    count += temp
    print(count)


partOne()
partTwo()