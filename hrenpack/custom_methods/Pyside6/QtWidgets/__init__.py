from PySide6.QtWidgets import *
from typing import Union
# Здесь будут методы, которые предназначены для разных классов


def textWidth(self):
    return self.fontMetrics().boundingRect(self.text()).width()


def defaultStyleSheet(self):
    self.default_styleSheet = self.styleSheet()


def adjustFontSize(self):
    try:
        max_size = self.maxFontSize
    except AttributeError:
        max_size = 32767
    try:
        min_size = self.minFontSize
    except AttributeError:
        min_size = 1
    try:
        sub = self.textBrim
    except AttributeError:
        sub = 0
    font_size = 16
    while self.textWidth() > self.width() - sub:
        font_size -= 1
        if font_size < min_size:
            break
        self.setStyleSheet('font-size: ' + str(font_size) + 'pt;\n' + self.default_styleSheet)
    while textWidth(self) < self.width() - sub:
        font_size += 1
        if font_size > max_size:
            break
        self.setStyleSheet('font-size: ' + str(font_size) + 'pt;\n' + self.default_styleSheet)


def setText_with_adjust(self, text: str):
    self.setText(text)
    self.adjustFontSize()
