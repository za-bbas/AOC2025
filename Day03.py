lines = [line.strip() for line in open("inputs/Day03.txt", "r")]

def partOne():
    count = 0
    for line in lines:
        a = b = 0
        for i in range(len(line)):
            n = int(line[i])
            if n > a and i < len(line) -1:
                a = n
                b = 0
            elif n > b:
                b = n
        count += a*10 + b
    print(count)

def partTwo():
    count = 0
    for line in lines:
        # python doesn't actually have a stack data structure, so list will do
        stack = []
        for i in range(len(line)):
            n = int(line[i])
            while stack and (stack[-1] < n) and (len(stack) + (len(line) - i) > 12):
                stack.pop(-1)
            stack.append(n)
        stack = stack[:12]
        count += stackToNum(stack)
    print(count)

def stackToNum(s):
    n = 0
    for i in range(len(s)):
        n += (10**i) * (s[-i-1])
    return n

partOne()
partTwo()