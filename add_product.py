from PyQt6 import uic
from PyQt6.QtWidgets import *
from database import conn
from utils import resource_path
class AddProductDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path('../setup/ui/add_product.ui'), self)
        self.pushButton.clicked.connect(self.browser)
        self.pushButton_2.clicked.connect(self.add_product)
        self.pushButton_3.clicked.connect(self.reject)
        c = conn.cursor()
        c.execute('select id_categor, categor_name from categor')
        for r in c.fetchall():
            self.comboBox.addItem(r[1],r[0])
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
        file, _ = QFileDialog.getOpenFileName(self,'Фото','','Image(*.png, *.jpg)')
        if file:
            self.photo_path = file
            self.lineEdit_6.setText(file)
    def add_product(self):
        if not self.lineEdit.text():
            QMessageBox.warning(self, 'Ошибка', 'Введите название товара')
            return
        if not self.lineEdit_3.text():
            QMessageBox.warning(self, 'Ошибка', 'Введите цену товара')
            return
        c = conn.cursor()
        c.execute('insert into tovar (tovar_name, opisanie, id_categor, id_proizvod, id_postav, price, sale, kol_sklad, foto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                  (self.lineEdit.text(),
                   self.lineEdit_2.text(),
                   self.comboBox.currentData(),
                   self.comboBox_2.currentData(),
                   self.comboBox_3.currentData(),
                   float(self.lineEdit_3.text()),
                   int(self.lineEdit_4.text()),
                   int(self.lineEdit_5.text()),
                   self.photo_path,
                   ))
        conn.commit()
        c.close()
        QMessageBox.information(self,'Успех','Товар добавлен')
        self.accept()