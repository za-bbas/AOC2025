with open("Day02.txt", "r") as f:
    line = f.readline().strip()

def partOne():
    combinations = line.split(",")
    count = 0
    for c in combinations:
        start, end = c.split("-")
        for i in range(int(start), int(end) + 1):
            num = str(i)
            first, second = num[:len(num)//2], num[len(num)//2:]
            if first == second:
                count += i
                # print(num)

    print(count)

def partTwo():
    combinations = line.split(",")
    count = 0
    for c in combinations:
        start, end = c.split("-")
        for i in range(int(start), int(end) + 1):
            num = str(i)
            valid = False
            for j in range(2, len(num) + 1):
                valid |= isRepeatingString(num, j)
            if valid:
                count += i
                # print(i)
    print(count)

def isRepeatingString(s, r):
    if len(s) % r != 0:
        return False
    size = len(s) // r
    parts = [s[i : i + size] for i in range(0, len(s), size)]
    for part in parts:
        if part != parts[0]: return False
    return True

partOne()
partTwo()