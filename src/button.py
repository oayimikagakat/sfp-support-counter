from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPainterPath, QPixmap, QPen, QFont
from PyQt5.QtWidgets import QPushButton

from app import ROOT_DIR
from src.settings import save_settings, idol_list


class IdolButton(QPushButton):
    def __init__(self, slot, idol_id, parent=None):
        super(IdolButton, self).__init__("", parent)
        self.setFixedSize(76, 76)

        self.slot = slot
        self.idol_id = idol_id

        self.pixmap = None
        self.update_icon()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(Qt.darkGray, 5)
        painter.setPen(pen)

        clip_path = QPainterPath()
        clip_path.addEllipse(0, 0, self.width(), self.height())
        painter.setClipPath(clip_path)

        painter.setBrush(Qt.white)
        painter.drawEllipse(0, 0, self.width(), self.height())

        icon_x = (self.width() - self.pixmap.width()) / 2
        icon_y = self.height() - self.pixmap.height()
        painter.drawPixmap(icon_x, icon_y, self.pixmap)

        painter.setClipPath(QPainterPath())
        painter.drawEllipse(1, 1, self.width() - 2, self.height() - 2)

    def update_icon(self):
        save_settings(self.slot, self.idol_id)
        self.pixmap = QPixmap(self.image_path(self.idol_id)).scaled(95, 95, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.repaint()

    def mousePressEvent(self, event):
        new_idx = idol_list.index(self.idol_id)
        if event.button() == Qt.LeftButton:
            new_idx += 1
        elif event.button() == Qt.RightButton:
            new_idx -= 1
        self.idol_id = idol_list[new_idx % len(idol_list)]
        self.update_icon()

    @staticmethod
    def image_path(idol_id):
        return str(ROOT_DIR / f"img/Support_SD_{idol_id:02d}.png")


class CountButton(QPushButton):
    def __init__(self, text="0", parent=None):
        super(CountButton, self).__init__(text, parent)
        self.setFixedSize(38, 76)
        self.setStyleSheet("QPushButton { color: white; }")
        self.setFont(QFont("Arial", 40))
        self.count = 0

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.count = min(self.count + 1, 8)
        elif event.button() == Qt.RightButton:
            self.count = max(self.count - 1, 0)
        self.setText(str(self.count))

    def reset_count(self):
        self.count = 0
        self.setText(str(self.count))
