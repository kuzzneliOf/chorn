class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.center = None
        self.right = None

    def insert_word(self, word):
        for i in word:
            self.insert(i)

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data == self.data:
            if self.center:
                self.center.insert(data)
            else:
                self.center = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def toPrint(self):
        res = ''
        if self.left:
            res += self.left.toPrint()+' '
        res += str(self.data)+' '
        if self.center:
            res += self.center.toPrint() + ' '
        if self.right:
            res += self.right.toPrint() + ' '
        return res
