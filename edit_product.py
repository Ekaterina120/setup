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