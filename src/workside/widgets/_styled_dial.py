"""WorkSide - Widgets - StyledDial"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import math

from PySide6.QtCore import Qt, QRectF, QPointF, Signal, QEvent
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QMouseEvent
from PySide6.QtWidgets import QWidget


class StyledDial(QWidget):
  """Custom circular slider implemented as a QWidget subclass."""

  valueChanged = Signal(float)

  def __init__(self):
    super().__init__()
    self.setMouseTracking(True)
    self.isUnderMouse = False
    self.isMouseDown = False
    self.angle = 0  # Angle in degrees
    self.squareSize = 100  # Default square size
    self.setFixedSize(self.squareSize, self.squareSize)
    self.center = None

  def mousePressEvent(self, event: QMouseEvent) -> None:
    self.isMouseDown = True
    self.updateAngle(event.globalPos())
    self.update()

  def mouseReleaseEvent(self, event: QMouseEvent) -> None:
    self.isUnderMouse = True
    self.isMouseDown = False
    self.updateAngle(event.globalPos())
    self.update()

  def mouseMoveEvent(self, event: QMouseEvent) -> None:
    if self.isMouseDown:
      self.updateAngle(event.globalPos())
    self.update()

  def enterEvent(self, event: QEvent) -> None:
    self.isUnderMouse = True
    self.update()

  def leaveEvent(self, event: QEvent) -> None:
    self.isUnderMouse = False
    self.update()

  def updateAngle(self, globalPos) -> None:
    if self.center is None:
      self.center = self.mapToGlobal(self.rect().center())
    dx = globalPos.x() - self.center.x()
    dy = globalPos.y() - self.center.y()
    self.angle = math.degrees(math.atan2(dx, dy) - math.pi / 2)
    self.valueChanged.emit(self.angle)

  def getDialColor(self) -> QColor:
    if self.isMouseDown:
      return QColor("#008000")
    elif self.isUnderMouse:
      return QColor("#00FF00")
    else:
      return QColor("#004000")

  def paintEvent(self, event) -> None:
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing, True)

    # Draw dial
    rect = QRectF(10, 10, self.width() - 20, self.height() - 20)
    dialColor = self.getDialColor()
    painter.setBrush(QBrush(dialColor))
    painter.setPen(QPen(dialColor.darker(120)))
    painter.drawEllipse(rect)

    # Draw thumb
    thumbRadius = 10
    center = QPointF(self.width() / 2, self.height() / 2)
    thumbX = center.x() + (self.width() / 2 - thumbRadius - 10) * math.cos(
      math.radians(self.angle))
    thumbY = center.y() - (self.height() / 2 - thumbRadius - 10) * math.sin(
      math.radians(self.angle))
    thumbRect = QRectF(thumbX - thumbRadius,
                       thumbY - thumbRadius,
                       thumbRadius * 2,
                       thumbRadius * 2)
    painter.setBrush(QBrush(QColor("#FFFFFF")))
    painter.setPen(Qt.NoPen)
    painter.drawEllipse(thumbRect)

    painter.end()
