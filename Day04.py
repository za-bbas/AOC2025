# not particularly proud of it but it works
graph = [line.strip() for line in open("inputs/Day04.txt", "r")]

def partOne(lines):
    count = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c]=='@' and countAround(r, c, lines) < 4: 
                count += 1
    print(count)

def partTwo(lines):
    lines = [list(line) for line in lines]
    count = 0
    while True:
        delta = 0
        for r in range(len(lines)):
            for c in range(len(lines[0])):
                if lines[r][c]=='@' and countAround(r, c, lines) < 4: 
                    delta += 1
                    lines[r][c] = '.'
        count += delta
        if delta == 0: break
    print(count)

def countAround(r, c, lines):
    g = {'.':0, '@':1}
    if r==0 and c==0: return 3
    if r==0 and c==len(lines[r]) -1: return 3
    if r == len(lines) - 1 and c == 0: return 3
    if r == len(lines) - 1 and c == len(lines[r]) - 1: return 3
    if r == 0:
        return (g[lines[r][c-1]]+
                g[lines[r][c+1]]+
                g[lines[r+1][c]]+
                g[lines[r+1][c-1]]+
                g[lines[r+1][c+1]])
    elif r == len(lines) - 1:
        return (g[lines[r][c-1]]+
                g[lines[r][c+1]]+
                g[lines[r-1][c]]+
                g[lines[r-1][c-1]]+
                g[lines[r-1][c+1]])
    elif c == 0:
        return (g[lines[r-1][c]]+
                g[lines[r-1][c+1]]+
                g[lines[r+1][c]]+
                g[lines[r+1][c+1]]+
                g[lines[r][c+1]])
    elif c == len(lines[r]) - 1:
        return (g[lines[r-1][c]]+
                g[lines[r-1][c-1]]+
                g[lines[r+1][c]]+
                g[lines[r+1][c-1]]+
                g[lines[r][c-1]])
    else:
        return (g[lines[r-1][c]]+
                g[lines[r+1][c]]+
                g[lines[r][c-1]]+
                g[lines[r][c+1]]+
                g[lines[r-1][c-1]]+
                g[lines[r-1][c+1]]+
                g[lines[r+1][c-1]]+
                g[lines[r+1][c+1]])

partOne(graph)
partTwo(graph)