"""MainWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from icecream import ic

from workside.windows import InputWindow

ic.configureOutput(includeContext=True)


class MainWindow(InputWindow):
  """MainWindow
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, ) -> None:
    InputWindow.__init__(self)
    self.setMinimumWidth(640)
    self.setMinimumHeight(480)
    self._logWidget = None

  def setupWidgets(self) -> NoReturn:
    """Sets up the widgets"""

    self.getBaseWidget().setLayout(self.getBaseLayout())
    self.setCentralWidget(self.getBaseWidget())

  def show(self, ) -> NoReturn:
    """Implementation"""
    self.setupWidgets()
    InputWindow.show(self)

  def debugFunc01(self) -> NoReturn:
    """omg"""

  def debugFunc02(self) -> NoReturn:
    """omg"""

  def debugFunc03(self) -> NoReturn:
    """omg"""

  def debugFunc04(self) -> NoReturn:
    """omg"""
