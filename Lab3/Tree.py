
class Tree:
    leader = []
    next = []

    def __init__(self, num_nodes):
        for i in range(num_nodes):
            self.leader.append(None)
            self.next.append(None)

    def makeSet(self, x):
        self.leader[x] = x
        self.next[x] = None

    def findSet(self, x):
        return self.leader[x]

    def union(self, x, y):
        lead_x = self.findSet(x)
        lead_y = self.findSet(y)
        y = lead_y
        self.leader[y] = lead_x
        while self.next[y]:
            y = self.next[y]
            self.leader[y] = lead_x

        self.next[y] = self.next[x]
        self.next[lead_x] = lead_y

