class Tree:
    leader = []
    next = []

    def __init__(self, num_nodes):
        for i in range(num_nodes):
            self.leader.append(-1)
            self.next.append(-1)

    def makeSet(self, x):
        self.leader[x] = x
        self.next[x] = -1

    def findSet(self, x):
        return self.leader[x]

    def union(self, x, y):
        lead_x = self.findSet(x)
        lead_y = self.findSet(y)
        #print(lead_x, lead_y)
        y = lead_y
        self.leader[y] = lead_x
        while self.next[y] != -1:
            #print(y)
            y = self.next[y]
            #print(y)
            self.leader[y] = lead_x
        #print("entrato qui")
        self.next[y] = self.next[lead_x]
        self.next[lead_x] = lead_y

