"""MainWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt
from icecream import ic

from workside.windows import LayoutWindow

ic.configureOutput(includeContext=True)


class MainWindow(LayoutWindow):
  """MainWindow
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, ) -> None:
    LayoutWindow.__init__(self)
    self.setMinimumWidth(640)
    self.setMinimumHeight(480)
    self.setWindowTitle('Welcome to WorkSide!')

  def debugFunc01(self) -> NoReturn:
    """omg"""
    for button in Qt.MouseButton:
      buttonName = ('%s' % button).split('.')[-1]
      print(buttonName)

  def debugFunc02(self) -> NoReturn:
    """omg"""

  def debugFunc03(self) -> NoReturn:
    """omg"""

  def debugFunc04(self) -> NoReturn:
    """omg"""
