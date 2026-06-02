import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from database import conn
from utils import resource_path
from admin_window import AdminWindow
from client_window import ClientWindow
from manager_window import ManagerWindow
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path('../setup/ui/login.ui'),self)
        self.user_data = None
        self.id_guest = False
        px = QPixmap(resource_path('../setup/Image/Icon.ico'))
        if not px.isNull():
            self.label.setPixmap(px.scaled(200,200,Qt.AspectRatioMode.KeepAspectRatio))
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.login_as_guest)
    def login(self):
        c = conn.cursor(dictionary=True)
        c.execute('select u.*, r.role_name from user u join role r on u.id_role = r.id_role where u.login = %s and u.password = %s',
                  (self.lineEdit.text(), self.lineEdit_2.text()))
        u = c.fetchone()
        c.close()
        if u:
            self.user_data = u
            self.id_guest = False
            self.accept()
        else:
            QMessageBox.warning(self, 'Ошибка','Неверный логин или пароль')
    def login_as_guest(self):
        self.user_data = None
        self.id_guest = True
        self.accept()
def main():
    app = QApplication(sys.argv)
    while True:
        dialog = LoginDialog()
        if dialog.exec()!=QDialog.DialogCode.Accepted:
            break
        if dialog.user_data and dialog.user_data.get('id_role')==1:
            window = AdminWindow(dialog.user_data)
        elif dialog.user_data and dialog.user_data.get('id_role')==2:
            window = ManagerWindow(dialog.user_data)
        else:
            window = ClientWindow(dialog.user_data, dialog.id_guest)
        window.show()
        app.exec()
    sys.exit(0)
if __name__=='__main__':
    main()