import sys
from PyQt4 import QtCore, QtGui, uic 
import sqlite3
from sign_auto import *
import login_mod


class Sign(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_sign, QtCore.SIGNAL('clicked()'), self.sign)

    def sign(self):
        if self.ui.rb_y.isChecked():
            t = "Yes"
        elif self.ui.rb_n.isChecked():
            t = "No"
        else:
            QtGui.QMessageBox.warning(self, "警告!",  "请选择你是否知道手语!")
            return False
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO username VALUES(?,?)", (self.ui.le_user.text(),t))
        except sqlite3.Error as e:
            if str(e).rstrip() == "UNIQUE constraint failed: username.username":
                QtGui.QMessageBox.warning(self, "警告!", "用户名已经存在!")
                return False
            print(e)
            return False
        conn.commit()
        cursor.close()
        QtGui.QMessageBox.about(self, "成功!", "成功创建账户!")
        m = login_mod.Login()
        m.show()
        self.close()
        m.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = Sign(None)
    myWindow.show()
    app.exec_()
