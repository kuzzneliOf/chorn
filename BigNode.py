class BigNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def toPrint(self):
        res = ''
        if self.left:
            res += self.left.toPrint() + ' '
        res += str(self.data) + ' '
        if self.right:
            res += self.right.toPrint() + ' '
        return res