"""From WorkSide - Widgets - Painter
Automatic colour choices."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QPainter
from worktoy.worktoyclass import WorkToyClass

from workside.draw import Color


class Painter(QPainter, WorkToyClass):
  """From WorkSide - Widgets - Painter
  Automatic colour choices."""

  def __init__(self, color: Color, *args, **kwargs) -> None:
    QPainter.__init__(self, )
    WorkToyClass.__init__(self, *args, **kwargs)
    self._baseColor = color
