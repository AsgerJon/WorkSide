"""MenuBar subclasses QMenuBar providing the menu bar for the main window
of the application. Menus and actions should be defined on this class."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from PySide6.QtWidgets import QMenuBar, QWidget
from worktoy.parsing import extractArg
from worktoy.stringtools import stringList, monoSpace


class MenuBar(QMenuBar):
  """MenuBar subclasses QMenuBar providing the menu bar for the main window
  of the application. Menus and actions should be defined on this class."""

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParent(*args, **kwargs)
    QMenuBar.__init__(self, parent)
    self._parent = parent
    self._fileMenu = None
    self._editMenu = None
    self._helpMenu = None

  def _createFileMenu(self) -> None:
    """Creator-function for the file menu"""

  def getFileMenu(self, **kwargs) -> FileMenu:
    """Getter-function for file menu"""

  def _createEditMenu(self) -> None:
    """Creator-function for the edit menu"""

  def getEditMenu(self) -> EditMenu:
    """Getter-function for the edit menu"""

  def _createHelpMenu(self) -> None:
    """Creator-function for the help menu"""

  def getHelpMenu(self) -> HelpMenu:
    """Getter-function for the help menu"""
