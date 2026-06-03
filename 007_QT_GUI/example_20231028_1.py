import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Multiplication')

        self.num1 = QLineEdit(self)
        self.num1.move(20, 20)

        self.num2 = QLineEdit(self)
        self.num2.move(20, 60)

        self.result = QLabel(self)
        self.result.move(20, 100)

        btn = QPushButton('Multiply', self)
        btn.move(20, 140)
        btn.clicked.connect(self.multiply)

    def multiply(self):
        num1 = self.num1.text()
        num2 = self.num2.text()

        if not num1.isdigit() or not num2.isdigit():
            self.result.setText("Please enter valid numbers.")
            return

        result = int(num1) * int(num2)
        self.result.setText(f"Result: {result}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
