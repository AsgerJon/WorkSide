"""WorkToy - Window - LayoutWindow
This class is responsible for painting the window. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QGridLayout, QWidget, QLabel

from workside.widgets import LabelWidget
# from workside.widgets import StyledToggle
from workside.window import BaseWindow


class LayoutWindow(BaseWindow):
  """WorkToy - Window - LayoutWindow
  This class is responsible for painting the window. """

  def __init__(self, *args, **kwargs) -> None:
    BaseWindow.__init__(self, *args, **kwargs)
    self.setMinimumSize(QSize(480, 320))
    self._baseLayout = QGridLayout()
    self._baseWidget = QWidget()
    self._canvas = LabelWidget()

  def setupWidgets(self) -> None:
    """Sets up widgets"""

    self._baseLayout.addWidget(self._canvas, 0, 0)
    self._baseWidget.setLayout(self._baseLayout)
    self.setCentralWidget(self._baseWidget)

  def show(self) -> None:
    """Sets up widgets before super call"""
    self.setupWidgets()
    BaseWindow.show(self)
