lines = [line.strip() for line in open("inputs/Day01.txt", "r")]

def partOne():
    current = 50
    count = 0
    T = {"L": -1, "R": 1}
    for line in lines:
        num = int(line[1:]) % 100
        current += T[line[0]] * num
        if current > 99: current %= 100
        if current < 0: current += 100
        if current == 0: count += 1

    print(count)

def partTwo():
    current = 50
    count = 0
    T = {"L": -1, "R": 1}
    for line in lines:
        num = int(line[1:])
        direction = T[line[0]]
        count += num // 100
        remainder = num % 100
        new = current + direction * remainder
        if direction == 1:
            count += new >= 100
        else:
            count += new <= 0 and current != 0
        current = new % 100
        
    print(count)

partOne()
partTwo()