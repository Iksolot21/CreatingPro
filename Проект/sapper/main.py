import sys
import os
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
        icon_path = os.path.join(os.path.dirname(__file__), "assets", "flag.png")
        self.setWindowIcon(QIcon(icon_path))

        self.field = MineField(self.w, self.h, self.form, self.color, self.cell_size)
        self.label = QLabel(f"Mines: {self.field.getMines()}")
        self.resButton = QPushButton("Restart")
        self.cngButton = QPushButton("Change field")
        self.helpButton = QPushButton("Help") 

        self.vlt = QVBoxLayout()
        self.vlt.addWidget(self.label)
        self.vlt.addWidget(self.resButton)
        self.vlt.addWidget(self.cngButton)
        self.vlt.addWidget(self.helpButton)  
        self.vlt.addWidget(self.field)
        self.vlt.addStretch()

        self.hlt = QHBoxLayout(self)
        self.hlt.addStretch(1)  
        self.hlt.addLayout(self.vlt) 
        self.hlt.addStretch(1)

        self.field.changeCounter.connect(self.setVal)
        self.field.win.connect(self.win)
        self.field.explode.connect(self.lose)
        self.resButton.clicked.connect(self.restart)
        self.cngButton.clicked.connect(self.changeField)
        self.helpButton.clicked.connect(self.showHelp)  

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
        self.vlt.insertWidget(4, self.field) 
        self.field.changeCounter.connect(self.setVal)
        self.field.win.connect(self.win)
        self.field.explode.connect(self.lose)
        if self.color == MineField.color_rainbow:
            self.field.setCellColor(MineField.color_rainbow)
        else:
            self.field.setCellColor(MineField.colors[self.color])
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

    def showHelp(self):
        QMessageBox.information(self, "Help", "This project is a Minesweeper game. "
                                             "You can restart the game, change the field settings, and customize the game appearance. "
                                             "Try to uncover all the cells without detonating any mines!\n\n"
                                             "Created by Артём Гусев, Group 231-3212.")

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec())