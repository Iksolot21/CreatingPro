import math
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QRegion, QPolygon, QPainter, QPen, QColor, QIcon, QPixmap

style = """
QPushButton {
    background-color: #d0d0d0;
    font-size: 15px;
}
QPushButton:pressed, QPushButton:hover {
    background-color: #aaaaaa;
}
"""


class MineCell(QPushButton):
    t_tri = 0
    t_hex = 1
    t_arrow = 2

    def __init__(self, i, j, form, color, cell_size, parent=None):
        self.parent = parent
        super().__init__(parent)
        self.i, self.j = i, j
        self.fl = False
        self.disc = False
        self.mine = False

        self.setFixedSize(int(cell_size*40), int(cell_size*40))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setIconSize(QSize(int(cell_size//2*40), int(cell_size//2*40)))

        self.setStyleSheet(style)

        self.setText("")
        w, h = self.width(), self.height()
        points = []
        self.borderPoints = []

        self.ic = QIcon()
        icon_path = os.path.join(os.path.dirname(__file__), "assets", "flag.png")
        self.ic.addPixmap(QPixmap(icon_path), QIcon.Mode.Normal)
        self.ic.addPixmap(QPixmap(icon_path), QIcon.Disabled)

        if form == self.t_hex:
            for it in range(7):
                points.append(QPoint(int((math.cos(it / 3 * math.pi) * w + w) / 2),
                                          int((math.sin(it / 3 * math.pi) * h + h) / 2)))
                self.borderPoints.append(QPoint(int((math.cos(it / 3 * math.pi) * w) / 2.2 + w / 2 + 1),
                                     int((math.sin(it / 3 * math.pi) * h) / 2.2 + h / 2)))
        elif form == self.t_arrow:
                points = [QPoint(w,h//2),QPoint(w//2,h),QPoint(w//2,(h*3)//4),QPoint(0,(h*3)//4),
                          QPoint(0,h//4), QPoint(w//2,h//4), QPoint(w//2,0), QPoint(w,h//2)]
                if i%2==1:
                    points = [QPoint(0,h//2),QPoint(w//2,h),QPoint(w//2,(h*3)//4),QPoint(w,(h*3)//4),
                          QPoint(w,h//4), QPoint(w//2,h//4), QPoint(w//2,0), QPoint(0,h//2)]
                self.borderPoints = points          
        else:
            parity = int(i % 2 == j % 2) * 2 - 1
            for it in range(4):
                points.append(QPoint(int((math.sin(it / 3 * 2 * math.pi) * w + w) / 2),
                                          int((math.cos(it / 3 * 2 * math.pi) * parity * h + h) / 2)))
                self.borderPoints.append(QPoint(int((math.sin(it / 3 * 2 * math.pi) * w) / 2.4 + w / 2),
                                     int((math.cos(it / 3 * 2 * math.pi) * parity * h) / 2.4 + h / 2)))

        self.setMask(QRegion(QPolygon(points)))


    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        if e.button() == Qt.RightButton and not self.disc:
            self.setFlag(not self.fl)

    def setFlag(self, fl):
        if fl:
            self.setIcon(self.ic)
            self.setIconSize(QSize(int(self.width() // 2), int(self.height() // 2)))  # Установка размера значка
            self.parent.counterDec(self.mine)
            self.fl = True
        else:
            self.setIcon(QIcon(""))
            self.parent.counterInc(self.mine)
            self.fl = False

    def paintEvent(self, ev):
        super().paintEvent(ev)

        w, h = self.width(), self.height()

        pr = QPainter(self)
        pr.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setColor(QColor(0x505050))
        pen.setWidth(3)
        pr.setPen(pen)
        pr.drawPolyline(self.borderPoints)

    def setMines(self, n):
        self.setText(f"{n}")
        colors = ["#0000ff", "#00d000", "#ff0000", "#000080", "#800000", "#008080",
                  "#000000", "#ffffff", "#ffff00", "#d0d000", "#ff00ff", "#d000d0"]
        style_disc = f"""
        background-color: #d0d0d0;
        font-size: 15px;
        font-weight: 800;
        color: {colors[n-1]};
        """
        self.setStyleSheet(style_disc)