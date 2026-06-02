### database.py
import mysql.connector
conn = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='mydb'
)
### utils.py
import mysql.connector
conn = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='mydb'
)
### product_card.py
import os
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from utils import resource_path
class ProductCard(QWidget):
  def __init__(self,p,parent=None):
      super().__init__(parent)
      uic.loadUi(resource_path('ui/card.ui'), self)
      self.product_id = p['id_tovar']
      self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
      self.label_2.setText(f"{p['categor_name']} | {p['tovar_name']}")
      self.label_3.setText(f"Описание: {p['opisanie']}")
      self.label_4.setText(f"Производитель: {p['proizvod_name']}")
      self.label_5.setText(f"Поставщик: {p['postav_name']}")
      self.label_6.setText(f"Количество: {p['kol_sklad']} шт.")
      if p['sale'] > 15:
          self.label_8.setText(f"{p['price']} руб.")
          self.label_9.setText(f"{p['price']*(1-p['sale']/100):.2f} руб.")
          self.label_10.setText(f"Скидка {p['sale']}%")
          self.groupBox.setStyleSheet("background-color: #2E8B57")
      elif p['sale'] < 15:
          self.label_8.setText(f"{p['price']} руб.")
          self.label_9.setText(f"{p['price'] * (1 - p['sale'] / 100):.2f} руб.")
          self.label_10.setText(f"Скидка {p['sale']}%")
      else:
          self.label_8.hide()
          self.label_9.setText(f"{p['price'] * (1 - p['sale'] / 100):.2f} руб.")
          self.label_10.setText(f"Скидка 0%")
      if p.get('foto') and p['foto']:
          filename = os.path.basename(p['foto'])
          photo_path = resource_path(f"Image/{filename}")
          if os.path.exists(photo_path):
              px = QPixmap(photo_path)
              if not px.isNull():
                  self.label.setPixmap(px.scaled(200,160, Qt.AspectRatioMode.KeepAspectRatio))
          self.setFixedHeight(215)
###admin_window.py
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from database import conn
from utils import resource_path
from product_card import ProductCard
class AdminWindow(QMainWindow):
  def __init__(self,u):
      super().__init__()
      uic.loadUi(resource_path('ui/admin.ui'), self)
      self.u = u
      self.sel = None
      self.label_2.setText(f"Администратор: {u['familia']} {u['name']}")
      px = QPixmap(resource_path("Image/Icon.ico"))
      if not px.isNull():
          self.label.setPixmap(px.scaled(151,91, Qt.AspectRatioMode.KeepAspectRatio))
      self.comboBox.addItems(['Без сортировки','По возврастанию','По убыванию'])
      self.comboBox_2.addItem('Все поставщики')
      c = conn.cursor()
      c.execute('select postav_name from postav')
      for r in c.fetchall():
          self.comboBox_2.addItem(r[0])
      c.close()
      self.pushButton.clicked.connect(self.go_home)
      self.pushButton_2.clicked.connect(self.add_product)
      self.pushButton_3.clicked.connect(self.delete)
      self.pushButton_4.clicked.connect(self.edit_product)
      self.lineEdit.textChanged.connect(self.load)
      self.comboBox.currentTextChanged.connect(self.load)
      self.comboBox_2.currentTextChanged.connect(self.load)
      self.load()
  def load(self):
      c = conn.cursor(dictionary=True)
      q=("select t.*, c.categor_name, p.proizvod_name, ps.postav_name from tovar t join categor c on t.id_categor = c.id_categor join proizvod p on t.id_proizvod = p.id_proizvod join postav ps on t.id_postav = ps.id_postav where 1=1")
      p = []
      if t:= self.lineEdit.text():
          q+=" and t.tovar_name like %s or t.opisanie like %s"
          p.extend([f"%{t}%", f"%{t}%"])
      if (f:= self.comboBox_2.currentText())!="Все поставщики":
          q+=" and ps.postav_name=%s"
          p.append(f)
      if self.comboBox.currentText()=="По возврастанию":
          q+=" order by t.price asc"
      if self.comboBox.currentText()=="По убыванию":
          q+=" order by t.price desc"
      c.execute(q,p)
      pr = c.fetchall()
      c.close()
      w = self.scrollArea.takeWidget()
      if w:
          w.deleteLater()
      cont = QWidget()
      lay = QVBoxLayout(cont)
      lay.setAlignment(Qt.AlignmentFlag.AlignTop)
      for prd in pr:
          card = ProductCard(prd,self)
          card.mousePressEvent = lambda _, pid = prd['id_tovar']:self.select_product(pid)
          lay.addWidget(card)
      self.scrollArea.setWidget(cont)
      self.scrollArea.setWidgetResizable(True)
  def select_product(self,pid):
      self.sel = pid
      for card in self.scrollArea.widget().findChildren(ProductCard):
          card.setStyleSheet("background-color: #cce5ff;" if card.product_id == pid else "")
  def add_product(self):
      from add_product import AddProduct
      dialog = AddProduct()
      if dialog.exec()==QDialog.DialogCode.Accepted:
          self.load()
def edit_product(self):
   if not self.sel:
       QMessageBox.warning(self, 'Ошибка', 'Не выбран товар')
       return
   c = conn.cursor(dictionary=True)
   c.execute("""select t.*, c.categor_name, p.proizvod_name, ps.postav_name
                    from tovar t
                    join categor c on t.id_categor = c.id_categor
                    join proizvod p on t.id_proizvod = p.id_proizvod
                    join postav ps on t.id_postav = ps.id_postav
                    where t.id_tovar = %s""", (self.sel,))
   product = c.fetchone()
   c.close()
   if product:
       from edit_product import EditProductDialog
       dialog = EditProductDialog(product)
       if dialog.exec() == QDialog.DialogCode.Accepted:
           self.load()
  def delete(self):
      if not self.sel:
          QMessageBox.warning(self,'Ошибка','Не выбран товар')
          return
      if QMessageBox.question(self,'Удалить','Удалить?', QMessageBox.StandardButton.Yes |
QMessageBox.StandardButton.No)==QMessageBox.StandardButton.Yes:
          c = conn.cursor()
          c.execute('delete from tovar where id_tovar=%s',(self.sel,))
          conn.commit()
          c.close()
          self.sel = None
          self.load()
  def go_home(self):
      self.close()
###edit_product.py
from PyQt6 import uic
from PyQt6.QtWidgets import *
from database import conn
from utils import resource_path
class EditProductDialog(QDialog):
   def __init__(self, product_data):
       super().__init__()
       uic.loadUi(resource_path("ui/add_product.ui"), self)
       self.setWindowTitle("Редактирование товара")
       self.label.setText("Редактирование товара")
       self.pushButton_2.setText("Сохранить")
       self.product_id = product_data['id_tovar']
       self.photo_path = product_data.get('foto')
       self.lineEdit.setText(product_data['tovar_name'] or '')
       self.lineEdit_2.setText(product_data['opisanie'] or '')
       self.lineEdit_3.setText(str(product_data['price']))
       self.lineEdit_4.setText(str(product_data['sale']) if product_data['sale'] else '0')
       self.lineEdit_5.setText(str(product_data['kol_sklad']) if product_data['kol_sklad'] else '0')
       if self.photo_path:
           self.lineEdit_6.setText(self.photo_path)
       self.load_combo_boxes(product_data)
       self.pushButton.clicked.connect(self.browser)
       self.pushButton_2.clicked.connect(self.save_product)
       self.pushButton_3.clicked.connect(self.reject)
   def load_combo_boxes(self, product_data):
       c = conn.cursor()
       c.execute('select id_categor, categor_name from categor')
       categories = c.fetchall()
       for i, r in enumerate(categories):
           self.comboBox.addItem(r[1], r[0])
           if r[0] == product_data.get('categor_name'):
               self.comboBox.setCurrentIndex(i)
       c.execute('select id_proizvod, proizvod_name from proizvod')
       manufacturers = c.fetchall()
       for i, r in enumerate(manufacturers):
           self.comboBox_2.addItem(r[1], r[0])
           if r[0] == product_data.get('proizvod_name'):
               self.comboBox_2.setCurrentIndex(i)
       c.execute('select id_postav, postav_name from postav')
       suppliers = c.fetchall()
       for i, r in enumerate(suppliers):
           self.comboBox_3.addItem(r[1], r[0])
           if r[0] == product_data.get('postav_name'):
               self.comboBox_3.setCurrentIndex(i)
       c.close()
   def browser(self):
       file, _ = QFileDialog.getOpenFileName(self, 'Фото', '', 'Image(*.png *.jpg)')
       if file:
           self.photo_path = file
           self.lineEdit_6.setText(file)
   def save_product(self):
       if not self.lineEdit.text():
           QMessageBox.warning(self, 'Ошибка', 'Введите название товара')
           return
       if not self.lineEdit_3.text():
           QMessageBox.warning(self, 'Ошибка', 'Введите цену товара')
           return
       try:
           sale_value = int(self.lineEdit_4.text()) if self.lineEdit_4.text() else 0
           kol_value = int(self.lineEdit_5.text()) if self.lineEdit_5.text() else 0
           c = conn.cursor()
           c.execute("""update tovar set
                        tovar_name = %s,
                        opisanie = %s,
                        id_categor = %s,
                        id_proizvod = %s,
                        id_postav = %s,
                        price = %s,
                        sale = %s,
                        kol_sklad = %s,
                        foto = %s
                        where id_tovar = %s""",
            (self.lineEdit.text(),
                    self.lineEdit_2.text(),
                    self.comboBox.currentData(),
                    self.comboBox_2.currentData(),
                    self.comboBox_3.currentData(),
                    float(self.lineEdit_3.text()),
                      sale_value,
                      kol_value,
                      self.photo_path,
                      self.product_id))
           conn.commit()
           c.close()
           QMessageBox.information(self, 'Успех', 'Товар обновлен')
           self.accept()
       except Exception as e:
           QMessageBox.critical(self, 'Ошибка', f'Не удалось обновить товар: {str(e)}')
###add_product.py
from PyQt6 import uic
from PyQt6.QtWidgets import *
from database import conn
from utils import resource_path
class AddProduct(QDialog):
  def __init__(self):
      super().__init__()
      uic.loadUi(resource_path("ui/add_product.ui"), self)
      self.pushButton.clicked.connect(self.browser)
      self.pushButton_2.clicked.connect(self.add_product)
      self.pushButton_3.clicked.connect(self.reject)
      c = conn.cursor()
      c.execute('select id_categor, categor_name from categor')
      for r in c.fetchall():
          self.comboBox.addItem(r[1], r[0])
      c.close()
      c = conn.cursor()
      c.execute('select id_proizvod, proizvod_name from proizvod')
      for r in c.fetchall():
          self.comboBox_2.addItem(r[1], r[0])
      c.close()
      c = conn.cursor()
      c.execute('select id_postav, postav_name from postav')
      for r in c.fetchall():
          self.comboBox_3.addItem(r[1], r[0])
      c.close()
      self.photo_path = None
  def browser(self):
      file, _ = QFileDialog.getOpenFileName(self, 'Фото', '', 'Image(*.png, *.jpg)')
      if file:
          self.photo_path = file
          self.lineEdit_6.setText(file)
  def add_product(self):
      if not self.lineEdit.text():
          QMessageBox.warning(self, 'Ошибка', 'Нет названия товара')
          return
      if not self.lineEdit_3.text():
          QMessageBox.warning(self, 'Ошибка', 'Нет цены товара')
          return
      c = conn.cursor()
      c.execute("insert into tovar (tovar_name, opisanie, id_categor, id_proizvod, id_postav, price, sale, kol_sklad, foto) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.lineEdit.text(),
                 self.lineEdit_2.text(),
                 self.comboBox.currentData(),
                 self.comboBox_2.currentData(),
                 self.comboBox_3.currentData(),
                 float(self.lineEdit_3.text()),
                 int(self.lineEdit_4.text()),
                 int(self.lineEdit_5.text()),
                 self.photo_path
                 ))
      conn.commit()
      c.close()
      QMessageBox.information(self,'Успех','Товар добавлен')
      self.accept()
###client_window.py
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from database import conn
from utils import resource_path
from product_card import ProductCard
class ClientWindow(QMainWindow):
  def __init__(self,u=None, g=None):
      super().__init__()
      uic.loadUi(resource_path('ui/client.ui'), self)
      self.user_data = u
      self.id_guest = g
      if not g and u:
          self.label_2.setText(f"Клиент: {u['familia']} {u['name']}")
      else:
          self.label_2.setText(f"Гость")
      px = QPixmap(resource_path("Image/Icon.ico"))
      if not px.isNull():
          self.label.setPixmap(px.scaled(151,91, Qt.AspectRatioMode.KeepAspectRatio))
          self.pushButton.clicked.connect(self.go_home)
      self.load()
  def load(self):
      c = conn.cursor(dictionary=True)
      q=("select t.*, c.categor_name, p.proizvod_name, ps.postav_name from tovar t join categor c on t.id_categor = c.id_categor join proizvod p on t.id_proizvod = p.id_proizvod join postav ps on t.id_postav = ps.id_postav where 1=1")
      c.execute(q)
      pr = c.fetchall()
      c.close()
      w = self.scrollArea.takeWidget()
      if w:
          w.deleteLater()
      cont = QWidget()
      lay = QVBoxLayout(cont)
      lay.setAlignment(Qt.AlignmentFlag.AlignTop)
      for prd in pr:
          card = ProductCard(prd,self)
          lay.addWidget(card)
      self.scrollArea.setWidget(cont)
      self.scrollArea.setWidgetResizable(True)
  def go_home(self):
      self.close()
###manager_window.py
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from database import conn
from utils import resource_path
from product_card import ProductCard
class ManagerWindow(QMainWindow):
  def __init__(self,u):
      super().__init__()
      uic.loadUi(resource_path('ui/admin.ui'), self)
      self.u = u
      self.sel = None
      self.label_2.setText(f"Менеджер: {u['familia']} {u['name']}")
      px = QPixmap(resource_path("Image/Icon.ico"))
      if not px.isNull():
          self.label.setPixmap(px.scaled(151,91, Qt.AspectRatioMode.KeepAspectRatio))
      self.comboBox.addItems(['Без сортировки','По возврастанию','По убыванию'])
      self.comboBox_2.addItem('Все поставщики')
      c = conn.cursor()
      c.execute('select postav_name from postav')
      for r in c.fetchall():
          self.comboBox_2.addItem(r[0])
      c.close()
      self.pushButton.clicked.connect(self.go_home)
      self.pushButton_2.hide()
      self.pushButton_3.hide()
      self.pushButton_4.hide()
      self.lineEdit.textChanged.connect(self.load)
      self.comboBox.currentTextChanged.connect(self.load)
      self.comboBox_2.currentTextChanged.connect(self.load)
      self.load()
  def load(self):
      c = conn.cursor(dictionary=True)
      q=("select t.*, c.categor_name, p.proizvod_name, ps.postav_name from tovar t join categor c on t.id_categor = c.id_categor join proizvod p on t.id_proizvod = p.id_proizvod join postav ps on t.id_postav = ps.id_postav where 1=1")
      p = []
      if t:= self.lineEdit.text():
          q+=" and t.tovar_name like %s or t.opisanie like %s"
          p.extend([f"%{t}%", f"%{t}%"])
      if (f:= self.comboBox_2.currentText())!="Все поставщики":
          q+=" and ps.postav_name=%s"
          p.append(f)
      if self.comboBox.currentText()=="По возврастанию":
          q+=" order by t.price asc"
      if self.comboBox.currentText()=="По убыванию":
          q+=" order by t.price desc"
      c.execute(q,p)
      pr = c.fetchall()
      c.close()
      w = self.scrollArea.takeWidget()
      if w:
          w.deleteLater()
      cont = QWidget()
      lay = QVBoxLayout(cont)
      lay.setAlignment(Qt.AlignmentFlag.AlignTop)
      for prd in pr:
          card = ProductCard(prd,self)
          lay.addWidget(card)
      self.scrollArea.setWidget(cont)
      self.scrollArea.setWidgetResizable(True)
  def go_home(self):
      self.close()
###main.py
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from database import conn
from utils import resource_path
from admin_window import AdminWindow
from client_window import ClientWindow
from manager_window import ManagerWindow
class LoginDialog(QDialog):
  def __init__(self):
      super().__init__()
      uic.loadUi(resource_path('ui/login.ui'), self)
      self.user_data = None
      self.id_guest = False
      px = QPixmap(resource_path('Image/Icon.ico'))
      if not px.isNull():
          self.label.setPixmap(px.scaled(200,200,Qt.AspectRatioMode.KeepAspectRatio))
      self.pushButton.clicked.connect(self.login)
      self.pushButton_2.clicked.connect(self.login_as_guest)
  def login(self):
      c = conn.cursor(dictionary=True)
      c.execute('select u.*, r.role_name from user u join role r on u.id_role = r.id_role where u.login = %s and u.password =%s',
                (self.lineEdit.text(), self.lineEdit_2.text()))
      u = c.fetchone()
      c.close()
      if u:
          self.user_data = u
          self.id_guest = False
          self.accept()
      else:
          QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль')
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
