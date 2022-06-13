import random
from tkinter import *


class Game:
    def __init__(self, end_score):
        self.finish = False
        self.map = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '%', '*', '*', '*', '*', '*', '*', '*', '#'],
            ['#', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
            ['#', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
            ['#', '#', '#', '#', '#', '*', '*', '*', '*', '#'],
            ['#', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
            ['#', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
            ['#', '*', '*', '*', '*', '#', '#', '#', '#', '#'],
            ['#', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]
        self.score = 0
        self.player_coor = (1, 1)
        self.end_score = end_score
        self.pixel_size = 32
        self.draw()

    def move(self, x, y):
        new_eat = False
        if (y == 0 or x == 0) and ((y == 1 or x == 1) or (y == -1 or x == -1)):
            if self.map[self.player_coor[0] + y][self.player_coor[1] + x] != '#':
                if self.map[self.player_coor[0] + y][self.player_coor[1] + x] == '/':
                    self.score += 1
                    new_eat = True
                self.map[self.player_coor[0]][self.player_coor[1]] = '*'
                self.player_coor = (self.player_coor[0] + y, self.player_coor[1] + x)
                self.map[self.player_coor[0]][self.player_coor[1]] = '%'
        if new_eat:
            self.draw_eat()
            if self.score == self.end_score:
                self.finish = True
                self.tk.unbind('<Down>')
                self.tk.unbind('<Up>')
                self.tk.unbind('<Right>')
                self.tk.unbind('<Left>')
                self.tk.bind('e', self.tk.destroy)
        self.draw_map()

    def draw(self):
        self.tk = Tk()
        self.elements = []
        self.tk.geometry('1000x1000')

        self.canvas = Canvas(width=1000, height=1000)
        self.canvas.pack()
        self.player_image = PhotoImage(file='./snake (1).png')
        self.eat_image = PhotoImage(file='./rhombus.png')
        self.draw_eat()
        self.draw_map()
        # self.tk.bind('<Down>', lambda e: self.move(0, 1))
        # self.tk.bind('<Up>', lambda e: self.move(0, -1))
        # self.tk.bind('<Right>', lambda e: self.move(1, 0))
        # self.tk.bind('<Left>', lambda e: self.move(-1, 0))
        self.tk.mainloop()

    def draw_eat(self):
        self.eat = (random.randint(0, len(self.map) - 1), random.randint(0, len(self.map[0]) - 1))
        while not self.map[self.eat[0]][self.eat[1]] == '*':
            self.eat = (random.randint(0, len(self.map)), random.randint(0, len(self.map[0])))
        self.map[self.eat[0]][self.eat[1]] = '/'

    def draw_map(self):
        for i in self.elements:
            self.canvas.delete(i)
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '#':
                    self.elements.append(self.canvas.create_rectangle(j * self.pixel_size, i * self.pixel_size,
                                                                      (j + 1) * self.pixel_size,
                                                                      (i + 1) * self.pixel_size, fill='black'))
                elif self.map[i][j] == '%':
                    self.elements.append(
                        self.canvas.create_image(j * self.pixel_size, i * self.pixel_size, image=self.player_image,
                                                 anchor=NW))
                elif self.map[i][j] == '*':
                    self.elements.append(self.canvas.create_rectangle(j * self.pixel_size, i * self.pixel_size,
                                                                      (j + 1) * self.pixel_size,
                                                                      (i + 1) * self.pixel_size))
                elif self.map[i][j] == '/':
                    self.elements.append(
                        self.canvas.create_image(j * self.pixel_size, i * self.pixel_size, image=self.eat_image,
                                                 anchor=NW))
                self.elements.append(self.canvas.create_text(150, len(self.map)*self.pixel_size + 50 , fill="black", font="Times 20 italic bold",
                                        text="Your score is {}".format(self.score)))

game = Game(10)
