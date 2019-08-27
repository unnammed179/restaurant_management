from PyQt5.QtWidgets import QApplication
import app
import sys

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    win = app.MainWindow()
    win.show()
    sys.exit(myApp.exec_())