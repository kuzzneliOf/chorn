class BFS:
    def __init__(self, map,pl_y, pl_x):
        self.player_coor = (pl_y, pl_x)
        self.map = map

    def run_logic(self):
        new_eat = False
        x,y = 1,0
        if (y == 0 or x == 0) and ((y == 1 or x == 1) or (y == -1 or x == -1)):
            if self.map[self.player_coor[0] + y][self.player_coor[1] + x] != '#':
                self.map[self.player_coor[0]][self.player_coor[1]] = '*'
                self.player_coor = (self.player_coor[0] + y, self.player_coor[1] + x)
                self.map[self.player_coor[0]][self.player_coor[1]] = '%'
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end = ' ')
            print()
        return (x,y)


    # def running(self):
    #     for (all nodes i) visited[i] = false; // спочатку список відвіданих вузлів порожній
    #     queue.push(start_node); // починаючи
    #     з
    #     вузла - джерела
    #     visited[start_node] = true;
    #     while (! queue.empty() ) {// поки черга не порожня
    #     node = queue.pop(); // витягти перший елемент в черзі
    #     if (node == goal_node) {
    #     return true; // перевірити, чи
    #     не
    #     є
    #     поточний
    #     вузол
    #     цільовим
    #     }
    #     foreach(child in expand(node))
    #     { // всі
    #     наступники
    #     поточного
    #     вузла, ...
    #     if (visited[child] == false) {//...які ще не були відвідані...
    #     queue.push(child); //...додати в кінець черги...
    #     visited[child] = true; //...і позначити як відвідані
    #     }
    #
    # }
    # }
    # return false;

class Graph:
    def __init__(self, map, pl_y, pl_x):
        self.map = []

        for i in range(len(map) + 2):
            self.map.append([])

        self.map[0] = [None]*(len(map[0])+2)
        self.map[len(self.map)-1] = [None]*(len(map[0])+2)

        for i in range(1,len(self.map)-1):
            self.map[i].append(None)
            for j in range(len(map)):
                self.map[i].append(Node(map[i-1][j]))
            self.map[i].append(None)
        self.create_rel()
        self.player_node = self.map[pl_y+1][pl_x+1]

    def get_player_node(self):
        return self.player_node

    def create_rel(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j]:
                    if self.map[i][j+1]:
                        self.map[i][j].insert(self.map[i][j+1])
                    if self.map[i +1][j]:
                        self.map[i][j].insert(self.map[i+1][j])
                    if self.map[i-1][j]:
                        self.map[i][j].insert(self.map[i-1][j])
                    if self.map[i][j - 1]:
                        self.map[i][j].insert(self.map[i][j-1])

class Node:
    def __init__(self, sign):
        self.neighbours = []
        self.is_visited = False
        self.sign = sign
    def getNeigbours(self):
        return self.neighbours
    def clear(self):
        self.is_visited = False
    def visit(self):
        self.is_visited = True
    def insert(self, new_node):
        self.neighbours.append(new_node)
    def __str__(self):
        return sign + 'neigh: [{}]'.format(self.neighbours)