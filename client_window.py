from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from product_card import ProductCard
from database import conn
from utils import resource_path
class ClientWindow(QMainWindow):
    def __init__(self, u=None, g=None):
        super().__init__()
        uic.loadUi(resource_path('ui/client.ui'), self)
        self.id_guest = g
        self.user_data = u
        if not g and u:
            self.label_2.setText(f"Клиент: {u['familia']} {u['name']}")
        else:
            self.label_2.setText("Гость")
        px = QPixmap(resource_path('Image/Icon.ico'))
        if not px.isNull():
            self.label.setPixmap(px.scaled(151,91,Qt.AspectRatioMode.KeepAspectRatio))
        self.pushButton.clicked.connect(self.close)
        self.load()
    def load(self):
        c = conn.cursor(dictionary=True)
        q = ('select t.*, c.categor_name, p.proizvod_name, ps.postav_name from tovar t join categor c on t.id_categor = c.id_categor join proizvod p on t.id_proizvod = p.id_proizvod join postav ps on t.id_postav = ps.id_postav where 1=1')
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