"""WorkSide - Window - BaseWindow
Lowest window class organising menus and actions. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QWidget

from worktoy.worktoyclass import WorkToyClass


class BaseWindow(QMainWindow, WorkToyClass):
  """WorkSide - Window - BaseWindow
  Lowest window class organising menus and actions. """

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QMainWindow.__init__(self, parent)

  def show(self) -> None:
    """Passes to super call"""
    QMainWindow.show(self)
