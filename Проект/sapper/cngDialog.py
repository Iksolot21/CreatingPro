from PyQt5.QtWidgets import *

class cngDialog(QDialog):
    def __init__(self, w, h, form, color, cell_size, parent=None):
        super().__init__(parent)
        self.first = QSpinBox(self)
        self.first.setValue(w)
        self.first.setMaximum(25)
        self.first.setMinimum(1)

        self.second = QSpinBox(self)
        self.second.setValue(h)
        self.second.setMaximum(25)
        self.second.setMinimum(1)

        self.three = QDoubleSpinBox(self)
        self.three.setValue(cell_size)
        self.three.setRange(0.5,2.5)
        self.three.setSingleStep(0.1)

        self.fcombo = QComboBox(self)
        self.fcombo.addItems(["Triangular", "Hexagonal", "Arrow"])
        self.fcombo.setCurrentIndex(form)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.ccombo = QComboBox(self)
        self.ccombo.addItems(["Yellow", "Blue", "Green", "Rainbow"])
        self.ccombo.setCurrentIndex(color)


        layout = QFormLayout(self)
        layout.addRow("Width:", self.first)
        layout.addRow("Height:", self.second)
        layout.addRow("Size:", self.three)
        layout.addRow("Form:", self.fcombo) 
        layout.addRow("Color:", self.ccombo)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.value(), self.second.value(), self.fcombo.currentIndex(), self.ccombo.currentIndex(), self.three.value())