from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from product_card import ProductCard
from database import conn
from utils import resource_path
class AdminWindow(QMainWindow):
    def __init__(self, u):
        super().__init__()
        uic.loadUi(resource_path('../setup/ui/admin.ui'), self)
        self.sel = None
        self.u = u
        self.label_2.setText(f"Администратор: {u['familia']} {u['name']}")
        px = QPixmap(resource_path('../setup/Image/Icon.ico'))
        if not px.isNull():
            self.label.setPixmap(px.scaled(151,91,Qt.AspectRatioMode.KeepAspectRatio))
        self.comboBox.addItems(['Без сортировки','По возврастанию цены','По убыванию цены'])
        self.comboBox_2.addItem('Все поставщики')
        c = conn.cursor()
        c.execute('select postav_name from postav')
        for r in c.fetchall():
            self.comboBox_2.addItem(r[0])
        c.close()
        self.pushButton.clicked.connect(self.go_home)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_3.clicked.connect(self.add_product)
        self.lineEdit.textChanged.connect(self.load)
        self.comboBox.currentTextChanged.connect(self.load)
        self.comboBox_2.currentTextChanged.connect(self.load)
        self.load()
    def load(self):
        c = conn.cursor(dictionary=True)
        q = ('select t.*, c.categor_name, p.proizvod_name, ps.postav_name from tovar t join categor c on t.id_categor = c.id_categor join proizvod p on t.id_proizvod = p.id_proizvod join postav ps on t.id_postav = ps.id_postav where 1=1')
        p = []
        if t:=self.lineEdit.text():
            q+=" and t.tovar_name like %s or t.opisanie like %s"
            p.extend([f"%{t}%", f"%{t}%"])
        if (f:=self.comboBox_2.currentText())!="Все поставщики":
            q+= " and ps.postav_name = %s"
            p.append(f)
        if self.comboBox.currentText()=="По возврастанию цены":
            q+= " order by t.price asc"
        if self.comboBox.currentText()=="По убыванию цены":
            q+= " order by t.price desc"
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
            card.setStyleSheet("background-color: #cce5ff;" if card.product_id == pid else '')
    def delete(self):
        if not self.sel:
            QMessageBox.warning(self, 'Ошибка','Не выбран товар')
            return
        if QMessageBox.question(self,'Удалить','Удалить товар', QMessageBox.StandardButton.No |
                                                                QMessageBox.StandardButton.Yes) == QMessageBox.StandardButton.Yes:
            c = conn.cursor()
            c.execute('delete from tovar where id_tovar=%s', (self.sel,))
            conn.commit()
            c.close()
            self.sel = None
            self.load()
    def add_product(self):
        from add_product import AddProductDialog
        dialog = AddProductDialog()
        if dialog.exec()==QDialog.DialogCode.Accepted:
            self.load()
    def go_home(self):
        self.close()