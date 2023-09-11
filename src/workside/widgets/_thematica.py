"""WorkSide - Widgets - Thematica
"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations
from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtWidgets import QWidget, QApplication
import sys

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtWidgets import QWidget, QApplication
import sys


class CustomButton(QWidget):
  """Custom button implemented as a QWidget subclass."""

  def __init__(self):
    super().__init__()
    self.setMouseTracking(True)
    self.state = "normal"
    self.setMinimumSize(100, 50)

  def mousePressEvent(self, event) -> None:
    self.state = "pressed"
    self.update()

  def mouseReleaseEvent(self, event) -> None:
    self.state = "hover"
    self.update()

  def enterEvent(self, event) -> None:
    self.state = "hover"
    self.update()

  def leaveEvent(self, event) -> None:
    self.state = "normal"
    self.update()

  def getBackgroundColor(self) -> QColor:
    colors = {
      "normal" : QColor("#CCFFCC"),  # Light Lime
      "hover"  : QColor("#00FF00"),  # Lime
      "pressed": QColor("#008800")  # Dark Lime
    }
    return colors.get(self.state, QColor("#CCFFCC"))

  def getTextColor(self) -> QColor:
    colors = {
      "normal" : QColor("#006600"),  # Dark Green
      "hover"  : QColor("#004400"),  # Darker Green
      "pressed": QColor("#CCFFCC")  # Very Light Lime
    }
    return colors.get(self.state, QColor("#006600"))

  def getTextLabel(self) -> str:
    labels = {
      "normal" : "Normal",
      "hover"  : "Hover",
      "pressed": "Pressed"
    }
    return labels.get(self.state, "Normal")

  def paintEvent(self, event) -> None:
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing, True)
    rect = QRect(0, 0, self.width(), self.height())

    bgColor = self.getBackgroundColor()
    textColor = self.getTextColor()
    textLabel = self.getTextLabel()

    painter.setBrush(QBrush(bgColor))
    painter.setPen(QPen(bgColor.darker(120)))
    painter.drawRoundedRect(rect, 10, 10)

    painter.setPen(QPen(textColor))
    painter.drawText(rect, Qt.AlignCenter, textLabel)
    painter.end()
