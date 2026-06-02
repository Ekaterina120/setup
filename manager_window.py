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