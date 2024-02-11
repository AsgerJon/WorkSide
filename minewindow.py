"""workside - Core - MineWindow
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from worktoy.core import Function
from worktoy.worktoyclass import WorkToyClass

from struc_widget import StrucWidget


class MineWindow(QMainWindow):
  """MineWindow"""

  def __init__(self, *args, **kwargs) -> None:
    QMainWindow.__init__(self, *args, **kwargs)
    self._baseLayout = QVBoxLayout()
    self._baseWidget = QWidget()
    self._structureWidget = StrucWidget()
    self._statusBar = self.statusBar()
    self.setWindowTitle('MineSide | Qt for MineScript')
    self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
    self.setWindowOpacity(0.5)

  def chatListenerFactory(self) -> Function:
    """Factory for chat listeners"""

    def chatListeners(chat: str) -> None:
      """Chat listener"""
      self.receiveChat(chat)

    return chatListeners

  def receiveChat(self, chat: str) -> None:
    """Chat reception slot"""
    self._statusBar.showMessage(chat)

  def setupWidgets(self) -> None:
    """Sets up the widgets"""
    self._baseLayout.addWidget(self._structureWidget)
    self._baseWidget.setLayout(self._baseLayout)
    self.setCentralWidget(self._baseWidget)

  def structureQuery(self) -> None:
    """Transmits the chat command"""
    print('/wits')

  def show(self) -> None:
    """Reimplementation invoking the 'setupWidgets' method before invoking
    the super call."""
    self.setupWidgets()
    super().show()
