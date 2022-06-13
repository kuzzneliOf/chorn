class BFS:
    def __init__(self, map,pl_y, pl_x):
        self.player_coor = (pl_y, pl_x)
        self.map = map

    def run_logic(self):
        new_eat = False
        x,y = 1,0
        if (y == 0 or x == 0) and ((y == 1 or x == 1) or (y == -1 or x == -1)):
            if self.map[self.player_coor[0] + y][self.player_coor[1] + x] != '#':
                if self.map[self.player_coor[0] + y][self.player_coor[1] + x] == '/':
                    self.score += 1
                    new_eat = True
                self.map[self.player_coor[0]][self.player_coor[1]] = '*'
                self.player_coor = (self.player_coor[0] + y, self.player_coor[1] + x)
                self.map[self.player_coor[0]][self.player_coor[1]] = '%'
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end = ' ')
            print()
        return (x,y)

