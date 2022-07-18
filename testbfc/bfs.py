class Graph:
    def __init__(self):
        self.edges = []
        self.angles = []

    def addEdge(self, newEdge):
        self.edges.append(newEdge)

    def addAngle(self, fromEdge, toEdge):
        self.angles.append(Connection(fromEdge, toEdge))

    def neighbours(self, edge):
        s = []
        for conn in self.angles:
            if conn.getFromEdge() == edge:
                if not conn.getToEdge() in s:
                    s.append(conn.getToEdge())
        return s


class Connection:
    def __init__(self, edge1, edge2):
        self.edgeFrom = edge1
        self.edgeTo = edge2

    def getFromEdge(self):
        return self.edgeFrom

    def getToEdge(self):
        return self.edgeTo
