import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5')
        self.move(300, 300)
        self.resize(300, 300)

        btn = QPushButton("Start", self)

        layout = QHBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)

        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())