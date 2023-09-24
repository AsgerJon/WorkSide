"""WorkSide - Windows - Menus - StatusBar
Provides the status bar at the bottom of the application window"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QStatusBar, QWidget
from icecream import ic

from workside.widgets import Template
from workside.specialwidgets import ClockWidget, LabelWidget
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


class StatusBar(QStatusBar, WorkToyClass):
  """WorkSide - Windows - Menus - StatusBar
  Provides the status bar at the bottom of the application window"""

  clockWidget = Attribute()
  labelWidget = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QStatusBar.__init__(self, parent)
    self.clockWidget = ClockWidget()
    self.labelWidget = LabelWidget()
    self.fontTemplate = Template(self.clockWidget)
    self.fontTemplate.addName('fontFamily')
    self.fontTemplate.addName('fontSize')
    self.fontTemplate.addName('paddingLeft')
    self.fontTemplate.addName('paddingRight')
    self.fontTemplate.addName('paddingTop')
    self.fontTemplate.addName('alignment')
    self.fontTemplate.addName('lineLength')
    self.labelWidget = self.fontTemplate(self.labelWidget)
    self.addPermanentWidget(self.clockWidget)
    self.addPermanentWidget(self.labelWidget)

  def showMessage(self, text: str, timeout: int = None) -> None:
    """Implementation showing the message in the label widget"""
    self.labelWidget.currentText = text
    self.labelWidget.update()

  def setStatusTip(self, text: str) -> None:
    """Same as above"""
    self.labelWidget.currentText = text
    self.labelWidget.update()

  def paintEvent(self, arg__1: QPaintEvent) -> None:
    """LMAO"""
    self.clockWidget.update()
    self.labelWidget.update()
