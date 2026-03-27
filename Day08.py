# maybe not an actual Disjoint-set data structure in the traditional sense
# but it gets the job done for this specific implementation
# will also be slower than normal union-find
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

lines = [line.strip() for line in open("inputs/test.txt", "r")]
