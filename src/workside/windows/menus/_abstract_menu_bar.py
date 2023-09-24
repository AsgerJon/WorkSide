"""WorkSide - Windows - Menus - AbstractMenuBar
Baseclass for menu bar"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMenuBar, QWidget

from worktoy.worktoyclass import WorkToyClass


class AbstractMenuBar(QMenuBar, WorkToyClass):
  """WorkSide - Windows - Menus - AbstractMenuBar
  Baseclass for menu bar"""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QMenuBar.__init__(self, parent)
