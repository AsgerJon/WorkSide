"""workside - Core - TextLabel
Simplest label implementation"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QWidget
from worktoy.descriptors import Attribute


class TextLabel(QWidget):
  """Simplest label implementation"""

  currentText = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    QWidget.__init__(self, *args, **kwargs)

  def paintEvent(self, event: QPaintEvent) -> None:
    """The paintevent uses the printer painter"""
