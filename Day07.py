lines = [line.strip() for line in open("inputs/Day07.txt", "r")]
cleaned_lines = lines[0::2]

def partOne():
    count = 0
    tachyons_prev = set()
    for line in cleaned_lines:
        tachyons = set()
        if 'S' in line:
            tachyons.add(line.index('S'))
        else:
            for t in tachyons_prev:
                if line[t] == '^':
                    count += 1
                    tachyons.add(t-1)
                    tachyons.add(t+1)
                else:
                    tachyons.add(t)
        
        tachyons_prev = tachyons.copy()
    print(count)


def partTwo():
    # keep track of active tachyons (parallel universe) at each level
    # at the end, count how many tachyons exist
    tachyons_prev = dict()
    for line in cleaned_lines:
        tachyons = dict()
        if 'S' in line:
            tachyons[line.index('S')] = 1
        else:
            for t in tachyons_prev.keys():
                if line[t] == '^':
                    tachyons[t-1] = tachyons.get(t-1, 0) + tachyons_prev[t]
                    tachyons[t+1] = tachyons.get(t+1, 0) + tachyons_prev[t]
                else:
                    tachyons[t] = tachyons.get(t, 0) + tachyons_prev[t] 
        tachyons_prev = tachyons.copy()
    print(sum(tachyons_prev.values()))

partOne()
partTwo()