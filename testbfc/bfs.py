class Graph:
    def __init__(self):
        self.edges = []
        self.angles = []

    def addEdge(self, newEdge):
        self.edges.append(newEdge)

    def addAngle(self, fromEdge, toEdge):
        self.angles.append(tuple(fromEdge, toEdge))

    def neighbours(self, edge):
        s = []
        for conn in self.angles:
            if conn[0] == edge:
                if not conn[1] in s:
                    s.append(conn[1])
        return s
