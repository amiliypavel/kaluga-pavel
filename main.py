import sys
from random import randrange
from UI import Ui_Form
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Диалоговые окна')
        self.pushButton.clicked.connect(self.run)
        self.can_draw = False

    def run(self):
        self.can_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.can_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
        rand = randrange(30, 100)
        qp.drawEllipse(10, 10, rand, rand)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
