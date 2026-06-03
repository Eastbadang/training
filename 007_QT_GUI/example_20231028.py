import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(50, 50)

        qle = QLineEdit(self)
        qle.move(50, 10)

        btn = QPushButton('Show image', self)
        btn.move(150, 10)
        btn.clicked.connect(self.showImage)

        self.setWindowTitle('Input Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showImage(self):
        text = qle.text()
        pixmap = QPixmap(text)
        self.lbl.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
