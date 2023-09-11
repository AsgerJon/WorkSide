"""WorkSide - Widgets - StyledSlider"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Qt, QRect, Signal
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtWidgets import QWidget
from worktoy.worktoyclass import WorkToyClass


class StyledSlider(QWidget, WorkToyClass):
  """Custom slider implemented as a QWidget subclass."""

  valueChanged = Signal(int)

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args, )
    direction = self.maybeType(Qt.Orientation, *args)
    strArgs = self.maybeTypes(str, *args)
    if direction is None:
      if 'vertical' in [word.lower() for word in strArgs]:
        direction = Qt.Orientation.Vertical
      if 'horizontal' in [word.lower() for word in strArgs]:
        if direction is not None:
          raise ValueError
        direction = Qt.Orientation.Horizontal
    if parent is None:
      QWidget.__init__(self, )
    else:
      QWidget.__init__(self, parent)
    self.setMouseTracking(True)
    self.isUnderMouse = False
    self.isMouseDown = False
    self.value = 10  # Initialize to avoid thumb cut-off
    self.direction = direction
    if self.direction == Qt.Orientation.Horizontal:
      self.setMaximumSize(300, 50)
    else:
      self.setMaximumSize(50, 300)

  def mousePressEvent(self, event) -> None:
    self.isMouseDown = True
    self.updateValue(event)
    self.update()

  def mouseReleaseEvent(self, event) -> None:
    self.isUnderMouse = True
    self.isMouseDown = False
    self.updateValue(event)
    self.update()

  def mouseMoveEvent(self, event) -> None:
    if self.isMouseDown:
      self.updateValue(event)
    self.update()

  def enterEvent(self, event) -> None:
    self.isUnderMouse = True
    self.update()

  def leaveEvent(self, event) -> None:
    self.isUnderMouse = False
    self.update()

  def updateValue(self, event) -> None:
    if self.direction == Qt.Orientation.Horizontal:
      self.value = min(max(10, event.x()), self.width() - 10)
    else:
      self.value = min(max(10, event.y()), self.height() - 10)
    self.valueChanged.emit(self.value)

  def getThumbColor(self) -> QColor:
    if self.isMouseDown:
      return QColor("#008000")
    elif self.isUnderMouse:
      return QColor("#00FF00")
    else:
      return QColor("#004000")

  def paintEvent(self, event) -> None:
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing, True)

    if self.direction == Qt.Orientation.Horizontal:
      # Draw horizontal track
      trackRect = QRect(0, self.height() // 2 - 5, self.width(), 10)
      thumbRect = QRect(self.value - 10, self.height() // 2 - 10, 20, 20)
    else:
      # Draw vertical track
      trackRect = QRect(self.width() // 2 - 5, 0, 10, self.height())
      thumbRect = QRect(self.width() // 2 - 10, self.value - 10, 20, 20)

    # Draw track
    painter.setBrush(QBrush(QColor("#CCCCCC")))
    painter.setPen(Qt.NoPen)
    painter.drawRect(trackRect)

    # Draw thumb
    thumbColor = self.getThumbColor()
    painter.setBrush(QBrush(thumbColor))
    painter.setPen(QPen(thumbColor.darker(120)))
    painter.drawEllipse(thumbRect)

    painter.end()
