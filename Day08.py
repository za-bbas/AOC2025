from itertools import combinations
#  maybe not an actual Disjoint-set data structure in the traditional sense
# but it gets the job done for this specific implementation
# will also be slower than normal union-find
# also, this implementation won't work for part 2 I don't think...maybe change case 5?
class unionFind:
    def __init__(self):
        # list of the different empty sets
        self.sets = []
    # Behavior: can add in pairs of things (numbers). If either number shows up in a previously
    # added pair, the pair gets added to that set
    # If the pair is in no sets (disjoint), it gets added to its own set
    # If the pair is in two seperate sets, we take their union
    def add(self, pair):
        x, y  = pair
        xAppear = yAppear = -1
        # check if either number is already in a set
        for i in range(len(self.sets)):
            if x in self.sets[i]:
                xAppear = i
            if y in self.sets[i]:
                yAppear = i
            if xAppear != -1 and yAppear != -1:
                break
        # case 1: neither is in a set; append a new set
        # case 2: x is in a set, y isn't
        # case 3: inverse of case 2
        # case 4: they are in two different sets
        # case 5: they are in the same set; do nothing :)
        if xAppear == yAppear and xAppear == -1:
            self.sets.append(set())
            self.sets[-1].add(x)
            self.sets[-1].add(y)
        elif yAppear == -1:
            self.sets[xAppear].add(y)
        elif xAppear == -1:
            self.sets[yAppear].add(x)
        elif xAppear != yAppear:
            self.unionSets(xAppear, yAppear)
    def unionSets(self, i, j):
        # takes the union of sets i and j; removes j from the list
        self.sets[i] = self.sets[i] | self.sets[j]
        self.sets.pop(j)
    def largestThreeProd(self):
        lengths = [len(s) for s in self.sets]
        lengths.sort(reverse=True)
        return lengths[0] * lengths[1] * lengths[2]
    def largestSet(self):
        if self.sets:
            lengths = [len(s) for s in self.sets]
            lengths.sort(reverse=True)
            return lengths[0]
        else:
            return 0
    def __str__(self):
        return self.sets

lines = [line.strip() for line in open("inputs/Day08.txt", "r")]
cleaned_lines =  [tuple(map(int, line.split(","))) for line in lines] # I hate python
results = []
    
for (i, p1), (j, p2) in combinations(enumerate(cleaned_lines), 2):
    # order by square of distance so we don't have annoying FP issues
    dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
    results.append((dist, i, j, p1, p2))    
results.sort(key=lambda x: x[0])

def partOne():
    circuits = unionFind()
    
    for i in range(1000):
        d, x, y, p1, p2 = results[i]
        circuits.add((x, y))
    print(circuits.largestThreeProd())

def partTwo():
    # so it needs to connect ALL of them into one circuit?
    # maybe just keep going until the longest circuit has 1000 elements...
    circuits = unionFind()
    x1 = x2 = -1
    i = 0
    while circuits.largestSet() < 1000:
        d, x, y, p1, p2 = results[i]
        circuits.add((x, y))
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        i += 1
    print(x1 * x2)

partOne()
partTwo()