"""LayoutWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from typing import NoReturn

from PySide6.QtGui import QKeyEvent, QTextCursor
from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout
from PySide6.QtWidgets import QWidget
from worktoy.core import maybe

from workside.widgets import CoreWidget
from workside.widgets import Label
from workside.windows import BaseWindow
from workside.styles import headerStyle

wordStart = QTextCursor.MoveOperation.StartOfWord
wordEnd = QTextCursor.MoveOperation.EndOfWord
move = QTextCursor.MoveMode.MoveAnchor
mark = QTextCursor.MoveMode.KeepAnchor


class LayoutWindow(BaseWindow):
  """A subclass of BaseWindow that provides layouts and widgets for a simple
  word processing application.

  This class adds a vertical layout to the QMainWindow and populates it
  with a QLabel, a QLineEdit, and a QTextEdit.
  The QLabel displays the current file name, the QLineEdit is used for
  entering search terms, and the QTextEdit is used for editing text."""

  def __init__(self, parent: QWidget = None) -> None:
    BaseWindow.__init__(self, parent)
    self._logWidget = None
    self._baseHeaderWidget = None
    self._baseWidget = None
    self._fileLabel = None
    self._centralWidget = None
    self._baseGridLayout = None
    self._baseVerticalBoxLayout = None
    self._baseHorizontalBoxLayout = None

  def _createBaseVerticalLayout(self) -> NoReturn:
    """Creator-function for the vertical base layout"""
    self._baseVerticalBoxLayout = QVBoxLayout()

  def getBaseVerticalBoxLayout(self) -> QVBoxLayout:
    """Getter-function for the vertical base layout"""
    if self._baseVerticalBoxLayout is None:
      self._createBaseVerticalLayout()
      return self.getBaseVerticalBoxLayout()
    if isinstance(self._baseVerticalBoxLayout, QVBoxLayout):
      return self._baseVerticalBoxLayout
    raise TypeError

  def _createHorizontalBoxLayout(self) -> NoReturn:
    """Creator function for the horizontal layout"""
    self._baseHorizontalBoxLayout = QHBoxLayout()

  def getBaseHorizontalBoxLayout(self) -> QHBoxLayout:
    """Getter function for the horizontal layout"""
    if self._baseHorizontalBoxLayout is None:
      self._createHorizontalBoxLayout()
      return self.getBaseHorizontalBoxLayout()
    if isinstance(self._baseHorizontalBoxLayout, QHBoxLayout):
      return self._baseHorizontalBoxLayout
    raise TypeError

  def _createBaseLayout(self) -> NoReturn:
    """Creator-function for the base layout"""
    self._baseGridLayout = QGridLayout()

  def getBaseLayout(self) -> QGridLayout:
    """Getter-function for the base layout"""
    if self._baseGridLayout is None:
      self._createBaseLayout()
      return self.getBaseLayout()
    if isinstance(self._baseGridLayout, QGridLayout):
      return self._baseGridLayout

  def _createBaseHeaderWidget(self) -> NoReturn:
    """Creator-function for the header widget"""
    self._baseHeaderWidget = Label()
    headerStyle @ self._baseHeaderWidget

  def _getBaseHeaderWidget(self) -> CoreWidget:
    """Getter-function for the header widget"""
    if self._baseHeaderWidget is None:
      self._createBaseHeaderWidget()
      return self._getBaseHeaderWidget()
    if isinstance(self._baseHeaderWidget, CoreWidget):
      return self._baseHeaderWidget

  def _createBaseWidget(self) -> NoReturn:
    """Creator-function for the base widget"""
    self._baseWidget = CoreWidget()

  def getBaseWidget(self) -> CoreWidget:
    """Getter-function for the base widget"""
    if self._baseWidget is None:
      self._createBaseWidget()
      return self.getBaseWidget()
    if isinstance(self._baseWidget, CoreWidget):
      return self._baseWidget

  @abstractmethod
  def setupWidgets(self) -> NoReturn:
    """Sets up the widgets"""

  def show(self) -> NoReturn:
    """Sets up the widgets before invoking the show super call"""
    BaseWindow.show(self)

  def tellMe(self, msg: str) -> NoReturn:
    """Transmits the message to the log widget"""
    if maybe(msg):
      self._logWidget.tellMe(msg)

  def keyReleaseEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    BaseWindow.keyReleaseEvent(self, event)

  def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    BaseWindow.keyPressEvent(self, event)
