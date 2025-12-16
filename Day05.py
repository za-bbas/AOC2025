# could be cleaner with how I parse...
lines = [line.strip() for line in open("inputs/Day05.txt", "r")]
ranges = []
ids = []
for line in lines:
    if "-" in line:
        ranges.append(line)
    elif line:
        ids.append(int(line))

def partOne():
    count = set()
    for idx in ids:
        for r in ranges:
            a, b = r[:r.find("-")], r[r.find("-")+1:]
            if int(a) <= idx <= int(b): 
                count.add(int(idx))
    print(len(count))

def partTwo():
    sortedRanges = sorted(ranges, key=lambda r: int(r.split("-")[0]))
    a, b = sortedRanges[0].split("-")
    a, b = int(a), int(b)
    union = []
    for r in sortedRanges[1:]:
        c, d = r.split("-")
        c, d = int(c), int(d)

        if c <= b:
            b = max(b, d)
        else:
            union.append((a,b))
            a, b = c, d
    union.append((a,b))
    count = 0
    for u in union:
        a, b = u
        count += (b-a + 1)
    print(count)
        

partOne()
partTwo()