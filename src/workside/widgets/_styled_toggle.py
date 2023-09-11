"""WorkSide - Widgets - StyledToggle
"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PySide6.QtWidgets import QWidget


class StyledToggle(QWidget):
  """Custom toggle button implemented as a QWidget subclass."""

  def __init__(self):
    super().__init__()
    self.setMouseTracking(True)
    self.isUnderMouse = False  # Track under mouse state
    self.isMouseDown = False  # Track mouse down state
    self.isActivated = False  # Track activated state
    self.setMinimumSize(110, 60)

  def mousePressEvent(self, event) -> None:
    self.isMouseDown = True
    self.update()

  def mouseReleaseEvent(self, event) -> None:
    self.isUnderMouse = True
    self.isMouseDown = False
    self.isActivated = not self.isActivated  # Toggle activated state
    self.update()

  def enterEvent(self, event) -> None:
    self.isUnderMouse = True  # Mouse entered widget
    self.update()

  def leaveEvent(self, event) -> None:
    self.isUnderMouse = False  # Mouse left widget
    self.update()

  def getBackgroundColor(self) -> QColor:
    if self.isUnderMouse:
      if self.isMouseDown:
        return QColor("#008000") if self.isActivated else QColor("#007B00")
      else:
        return QColor("#FFFF00") if self.isActivated else QColor("#00FF00")
    else:
      return QColor("#FFCC00") if self.isActivated else QColor("#CCFFCC")

  def getTextColor(self) -> QColor:
    return QColor("#000000")

  def getTextLabel(self) -> str:
    return "Activated" if self.isActivated else "Inactive"

  def getShadowOffset(self) -> QPoint:
    return QPoint(3, 3) if not self.isUnderMouse else QPoint(5, 5)

  def paintEvent(self, event) -> None:
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing, True)

    # Draw shadow
    shadowOffset = self.getShadowOffset()
    shadowRect = QRect(QPoint(0, 0) + shadowOffset,
                       QPoint(self.width(), self.height()) + shadowOffset)
    painter.setBrush(QBrush(QColor("#888888")))
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(shadowRect, 10, 10)

    # Draw button
    rect = QRect(0,
                 0,
                 self.width() - shadowOffset.x(),
                 self.height() - shadowOffset.y())
    bgColor = self.getBackgroundColor()
    textColor = self.getTextColor()
    textLabel = self.getTextLabel()

    font = QFont()
    font.setPointSize(14)
    font.setFamily('Consolas')
    painter.setFont(font)

    painter.setBrush(QBrush(bgColor))
    painter.setPen(QPen(bgColor.darker(120)))
    painter.drawRoundedRect(rect, 10, 10)

    painter.setPen(QPen(textColor))
    painter.drawText(rect, Qt.AlignCenter, textLabel)

    painter.end()
