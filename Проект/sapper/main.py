import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from MineField import MineField
from cngDialog import cngDialog

class MyWidget(QWidget):
    w = 20
    h = 10
    form = 2
    color = 0
    cell_size = 1

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper")
        self.setWindowIcon(QIcon("assets/flag.png"))

        self.field = MineField(self.w, self.h, self.form, self.color, self.cell_size)
        self.label = QLabel(f"Mines: {self.field.getMines()}")
        self.resButton = QPushButton("Restart")
        self.cngButton = QPushButton("Change field")

        self.lt = QVBoxLayout(self)
        self.lt.addWidget(self.label)
        self.lt.addWidget(self.resButton)
        self.lt.addWidget(self.cngButton)
        self.lt.addWidget(self.field)
        self.lt.addStretch()

        self.field.changeCounter.connect(self.setVal)
        self.field.win.connect(self.win)
        self.field.explode.connect(self.lose)
        self.resButton.clicked.connect(self.restart)
        self.cngButton.clicked.connect(self.changeField)

    def setVal(self, val):
        if self.field.state == self.field.s_play:
            self.label.setText(f"Mines: {val}")

    def win(self):
        self.label.setText("Win!")

    def lose(self):
        self.label.setText("Lose!")

    def restart(self):
        self.field.deleteLater()
        self.field = MineField(self.w, self.h, self.form, self.color, self.cell_size, parent=self)
        self.lt.addWidget(self.field)
        self.field.changeCounter.connect(self.setVal)
        self.field.win.connect(self.win)
        self.field.explode.connect(self.lose)
        self.label.setText(f"Mines: {self.field.getMines()}")

    def changeField(self):
        dialog = cngDialog(self.w, self.h, self.form, self.color, self.cell_size)
        if dialog.exec():
            self.w, self.h, self.form, color, self.cell_size = dialog.getInputs()
            if color == len(MineField.colors):  
                self.color = MineField.color_rainbow
            else:
                self.color = color
            self.restart()
            if self.color == MineField.color_rainbow:
                self.field.setCellColor(MineField.color_rainbow)
            else:
                self.field.setCellColor(MineField.colors[self.color])

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec())