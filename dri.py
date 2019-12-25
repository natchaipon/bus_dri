import time
import sys
from PyQt5.QtWidgets import QWidget , QApplication , QMainWindow , QMessageBox
from PyQt5.QtCore import *
from dri_ui import Ui_Form

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.main_task)
        self.timer.start()

        self.data = 0 

    def main_task(self):
        # print("hello")
        self.ui.lcdNumber.display(self.data)
        self.data += 1
        # time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())