"""WorkSide - Windows - LayoutWindow
This part of the application window chain is responsible for layout of
widgets. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from time import ctime

from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton, QVBoxLayout
from icecream import ic

from workside.quickwidgets import TextLabel
from workside.widgets import VerticalSpacer, HorizontalSpacer, TextWidget
from workside.windows import BaseWindow

ic.configureOutput(includeContext=True)


class LayoutWindow(BaseWindow):
  """WorkSide - Windows - LayoutWindow
  This part of the application window chain is responsible for """

  def __init__(self, *args, **kwargs) -> None:
    BaseWindow.__init__(self, *args, **kwargs)
    self._baseLayout = QGridLayout()
    self._innerLayout = QVBoxLayout()
    self._innerWidget = QWidget()
    self._baseWidget = QWidget()
    self._label = TextLabel('KILL')
    self.topHSpacer = HorizontalSpacer()
    self.bottomHSpacer = HorizontalSpacer()
    self.leftVSpacer = VerticalSpacer()
    self.rightVSpacer = VerticalSpacer()

  def setupWidgets(self) -> None:
    """Sets up the widgets. Add widget is row and then column."""
    self._innerLayout = QVBoxLayout()
    self._innerLayout.addWidget(self._label)
    self._innerWidget.setLayout(self._innerLayout)
    self._baseLayout.addWidget(self.topHSpacer, 0, 1, 1, 1)
    self._baseLayout.addWidget(self.bottomHSpacer, 2, 1, 1, 1)
    self._baseLayout.addWidget(self.leftVSpacer, 1, 0, 1, 1)
    self._baseLayout.addWidget(self.rightVSpacer, 1, 2, 1, 1)
    self._baseLayout.addWidget(self._innerWidget, 1, 1, 1, 1)
    self._baseWidget.setLayout(self._baseLayout)
    self.setCentralWidget(self._baseWidget)

  def _getBaseWidget(self, **kwargs) -> QWidget:
    """Getter-function for base widget"""
    if self._baseWidget is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createBaseWidget
        varType = QWidget
        varName = '_baseWidget'
        raise RecursiveCreateGetError(creator, varType, varName)
      self._createBaseWidget()
      return self._getBaseWidget(_recursion=True)
    return self._baseWidget

  def _createBaseWidget(self) -> None:
    """Creator-function for base widget"""
    self._baseWidget = QWidget()

  def _getBaseLayout(self, **kwargs) -> QGridLayout:
    """Getter-function for base layout """
    if self._baseLayout is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self._createBaseLayout
        varType = QGridLayout
        varName = '_baseLayout'
        raise RecursiveCreateGetError(creator, varType, varName)
      self._createBaseLayout()
      return self._getBaseLayout(_recursion=True)
    return self._baseLayout

  def _createBaseLayout(self) -> None:
    """Creator-function for the base layout"""
    self._baseLayout = QGridLayout()

  def show(self, ) -> None:
    """Reimplementation invoking 'setupWidgets' before the call to parent
    method."""
    self.setupWidgets()
    return BaseWindow.show(self)

  def debugFunc01(self, *_) -> None:
    """Debugging function"""
    print('single click')

  def debugFunc02(self, *_) -> None:
    """Debugging function"""
    print('double click')

  def debugFunc03(self, *_) -> None:
    """Debugging function"""
    print('triple click')

  def debugFunc04(self, *_) -> None:
    """Debugging function"""
    print('single press hold')

  def debugFunc05(self, *_) -> None:
    """Debugging function"""
    print('double press hold')

  def debugFunc06(self, *_) -> None:
    """Debugging function"""
    self._label.currentText = ctime()

  def debugFunc07(self, *_) -> None:
    """Debugging function"""
    print(self._label.geometry())
