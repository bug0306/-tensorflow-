import os
import detect_mod
import login_mod
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

with open("login.txt", "r") as f:
    y = f.read()
y.rstrip()
with open("text.txt", "w") as f:
    f.write("")

if y == "":
    app = QtGui.QApplication(sys.argv)
    myapp = login_mod.Login()
    #
    # app = QApplication(sys.argv)
    # window = QMainWindow()
    #
    # palette = QPalette()
    # palette.setBrush(QPalette.Background, QBrush(QPixmap("back1.jpg")))
    #
    # window.setPalette(palette)
    # window.setWindowTitle("QMainWindow Background Image")
    # window.show()

    myapp.show()
    sys.exit(app.exec_())
else:
    app = QtGui.QApplication(sys.argv)
    myapp = detect_mod.Detect(yes=y)
    myapp.show()
    sys.exit(app.exec_())