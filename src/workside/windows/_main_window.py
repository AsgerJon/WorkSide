"""WorkSide - Windows - MainWindow
The final class of the application window chain. This class should
organize the business logic."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMainWindow

from workside.windows import LayoutWindow


class MainWindow(LayoutWindow):
  """WorkSide - Windows - MainWindow
  The final class of the application window chain. This class should
  organize the business logic."""

  def __init__(self, *args, **kwargs) -> None:
    LayoutWindow.__init__(self, *args, **kwargs)
    self.setWindowTitle('WorkSide - MainWindow')

  def show(self) -> None:
    """Implementation"""
    LayoutWindow.show(self)
    self.update()
