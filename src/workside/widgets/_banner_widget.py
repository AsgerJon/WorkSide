"""WorkSide - Widgets - Banner
Constant colored banner widgets"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QPaintEvent

from workside.widgets import CoreWidget, WorkPainter


class Banner(CoreWidget):
  """WorkSide - Widgets - Banner
  Constant colored banner widgets"""

  def __init__(self, vertical: bool = None, horizontal: bool = None,
               *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)
    self.drawText = False
    if vertical:
      self.setFixedWidth(16)
    if horizontal:
      self.setFixedHeight(16)

  def __str__(self, ) -> str:
    """String representation"""
    return 'Banner'

  def __repr__(self) -> str:
    """Code representation"""
    return self.__class__.__qualname__
