import os
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from utils import resource_path
class ProductCard(QWidget):
    def __init__(self, p, parent=None):
        super().__init__(parent)
        uic.loadUi(resource_path('../setup/ui/card.ui'), self)
        self.product_id = p['id_tovar']
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.label_2.setText(f"{p['categor_name']} | {p['tovar_name']}")
        self.label_3.setText(f"Описание: {p['opisanie']}")
        self.label_4.setText(f"Производитель: {p['proizvod_name']}")
        self.label_5.setText(f"Поставщик: {p['postav_name']}")
        self.label_6.setText(f"Количество: {p['kol_sklad']} шт.")
        if p['sale']<15:
            self.label_8.setText(f"{p['price']} руб.")
            self.label_9.setText(f"{p['price']*(1-p['sale']/100):.2f} руб.")
            self.label_10.setText(f"Скидка {p['sale']}%")
        elif p['sale']>15:
            self.label_8.setText(f"{p['price']} руб.")
            self.label_9.setText(f"{p['price'] * (1 - p['sale'] / 100):.2f} руб.")
            self.label_10.setText(f"Скидка {p['sale']}%")
            self.groupBox.setStyleSheet("background-color: #2E8B57;")
        else:
            self.label_8.hide()
            self.label_9.setText(f"{p['price']} руб.")
            self.label_10.setText("Скидка 0%")
        if p.get('foto') and p['foto']:
            filename = os.path.basename(p['foto'])
            photo_path = resource_path(f"Image/{filename}")
            if os.path.exists(photo_path):
                px = QPixmap(photo_path)
                if not px.isNull():
                    self.label.setPixmap(px.scaled(200,160,Qt.AspectRatioMode.KeepAspectRatio))
            self.setFixedHeight(215)