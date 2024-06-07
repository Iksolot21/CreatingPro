from random import randint
from cngDialog import cngDialog

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget
from MineCell import MineCell

class MineField(QWidget):
    s_play = 0
    s_win = 1
    s_lose = 2

    t_tri = 0
    t_hex = 1
    t_arrow = 2
    colors = ['#FFCC66', '#6699CC', '#99CC99']
    rainbow_colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3']
    color_rainbow = 3

    explode = pyqtSignal()
    win = pyqtSignal()
    changeCounter = pyqtSignal(int)

    hex_sizer = (29, 30, 0, 15)
    tri_sizer = (16, 29, 0, 0)
    arr_sizer = (21, 37, 0, 15)

    def __init__(self, width, height, form, color=0, cell_size=1, parent=None):
        super().__init__(parent)
        self.cs = cell_size
        self.w = width
        self.h = height
        self.form = form
        self.color = color

        self.confType(form)
        self.setMinimumSize(int(width * self.sizer[0]*cell_size + self.sizer[2]*cell_size), int(height * self.sizer[1]*cell_size + self.sizer[3]*cell_size))

        self.cells = []

        self.mines = 0

        for i in range(width):
            self.cells.append([])
            for j in range(height):
                self.cells[i].append(MineCell(i, j, form, color, cell_size, self))
                if form == self.t_hex:
                    self.cells[i][j].move(int(i * 27 * self.cs), int((j * 30 + (i % 2 * 2 - 1) * 7 + 3)*self.cs))
                elif form == self.t_arrow:
                    self.cells[i][j].move(int(i * 20 * self.cs), int((j * 36 + (i % 2 * 2 - 1) * 9 + 7)*self.cs))
                else:
                    self.cells[i][j].move(int(i * 15 * self.cs), int((j * 28 + ((i % 2 != j % 2) * 2 - 1) * 5 + 3)*self.cs))
                if randint(0, 100) < 20:
                    self.cells[i][j].mine = True
                    self.mines += 1
                self.cells[i][j].clicked.connect(self.press)
                self.cells[i][j].setStyleSheet(f"background-color: {self.color}; font-size: 15px;")
        if self.mines == 0:
            self.cells[0][0].mine = True
            self.mines += 1

        self.fakeCounter = self.mines
        self.realCounter = self.mines
        self.discovered = 0
        self.total = height * width

        self.state = self.s_play
        

    def confType(self, form):
        if form == self.t_tri:
            self.sizer = self.tri_sizer
            self.neighbours = self.triNeighbours
        elif form == self.t_arrow:
            self.sizer = self.arr_sizer
            self.neighbours = self.ArrowNeighbours
        else:
            self.sizer = self.hex_sizer
            self.neighbours = self.hexNeighbours

    def hexNeighbours(self, i, j):
        sh = -1 if i % 2 == 0 else 1
        return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j + sh), (i + 1, j + sh)]

    def triNeighbours(self, i, j):
        parity = 1 if i % 2 != j % 2 else -1
        return [(i - 1, j), (i + 1, j),
              (i - 1, j + 1), (i + 1, j + 1),
              (i - 1, j - 1), (i + 1, j - 1),
              (i - 2, j), (i + 2, j),
              (i, j - 1), (i, j + 1),
              (i - 2, j + parity), (i + 2, j + parity)]
    def ArrowNeighbours(self, i, j):
        sh = 0 if i % 2 == 0 else 1
        return [(i - 2, j), (i - 1, j+sh), (i, j + 1), (i, j + 1), (i + 1, j + sh), (i + 2, j), (i+1,j+sh-1),(i,j-1), (i-1,j+sh-1)]

    def getMines(self):
        return self.mines

    def disableMines(self):
        for i0 in range(self.w):
            for j0 in range(self.h):
                self.cells[i0][j0].setDisabled(True)

    def counterDec(self, isMine):
        if isMine:
            self.realCounter -= 1
            if self.realCounter == 0:
                self.win.emit()
                self.state = self.s_win
                self.disableMines()
        self.fakeCounter -= 1
        self.changeCounter.emit(self.fakeCounter)

    def counterInc(self, isMine):
        if isMine:
            self.realCounter += 1
        self.fakeCounter += 1
        self.changeCounter.emit(self.fakeCounter)

    def checkMine(self, i, j):
        if 0 <= i < self.w and 0 <= j < self.h:
            return self.cells[i][j].mine
        return 0

    def discover(self, b: MineCell):
        self.discovered += 1
        b.disc = True
        if self.realCounter == 0:
            self.win.emit()
            self.state = self.sWin
        if b.fl:
            b.setFlag(False)
            self.counterInc(b.mine)
        i = b.i
        j = b.j

        if b.mine:
            b.setText("")
            b.setStyleSheet("background-color: red")
            self.explode.emit()
            self.state = self.s_lose
            self.disableMines()
            return

        cs = self.neighbours(i, j)
        ms = 0
        for p in cs:
            ms += self.checkMine(p[0], p[1])

        if ms > 0:
            b.setMines(ms)
        else:
            b.setStyleSheet("background-color: #a0a0a0")
            for p in cs:
                if 0 <= p[0] < self.w and 0 <= p[1] < self.h and not self.cells[p[0]][p[1]].disc:
                    self.discover(self.cells[p[0]][p[1]])

    def press(self):
        b = self.sender()
        self.discover(b)

    def setCellColor(self, color):
        if color == self.color_rainbow:
            total_cells = len(self.rainbow_colors)
            for i, row in enumerate(self.cells):
                for j, cell in enumerate(row):
                    idx = (i * len(row) + j) % total_cells
                    cell.setStyleSheet(f"background-color: {self.rainbow_colors[idx]}; font-size: 15px;")
        else:
            for row in self.cells:
                for cell in row:
                    cell.setStyleSheet(f"background-color: {color}; font-size: 15px;")
    

