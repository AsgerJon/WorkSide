"""BaseWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence

from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QWidget


class BaseWindow(QMainWindow):
  """BaseWindow subclasses QMainWindow and provides the application window
  with a menu bar and a status bar."""

  def __init__(self, parent: QWidget = None) -> None:
    QMainWindow.__init__(self, parent)
    self.setMouseTracking(True)
