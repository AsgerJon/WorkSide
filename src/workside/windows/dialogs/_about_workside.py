"""WorkSide - Windows - Dialogs
Opens workside information dialogue"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel

from workside.settings import Mouse
from workside.specialwidgets import LabelWidget
from worktoy.descriptors import Attribute
# from workside.widgets import TextWidget
from worktoy.worktoyclass import WorkToyClass


class AboutWorkSide(QWidget, WorkToyClass):
  """WorkSide - Windows - Dialogs
  Opens workside information dialogue"""

  header = Attribute()
  intro = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QWidget.__init__(self, parent)
    self.header = QLabel('Welcome to WorkSide!')
    self.intro = QLabel(self.monoSpace("""WorkSide is an extension 
    of the WorkToy utility package providing utility classes 
    specifically for use with PySide6."""))
    self.header = LabelWidget()
    self.header.currentText = 'Welcome to WorkSide'
    self.intro = LabelWidget()
    self.intro.currentText = self.monoSpace(
      """WorkSide is an extension of the WorkToy utility package providing 
      utility classes specifically for use with PySide6.""")
    self._baseLayout = QVBoxLayout()
    self.okButton = QPushButton('Exit')
    self.okButton.clicked.connect(self.closeFunction)
    self.setWindowTitle('Welcome to WorkSide!')

  def setupWidgets(self) -> None:
    """Sets up the widgets"""
    self._baseLayout.addWidget(self.header)
    self._baseLayout.addWidget(self.intro)
    self._baseLayout.addWidget(self.okButton)
    self.setLayout(self._baseLayout)

  def show(self) -> None:
    """Implements a call to set up widgets before the super call"""
    self.setupWidgets()
    return QWidget.show(self)

  def closeFunction(self, mouseButton: Mouse = None) -> None:
    """Closes the dialog"""
    self.close()
