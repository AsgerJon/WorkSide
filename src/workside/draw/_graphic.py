"""WorkSide - Draw - Graphic
Settings used by WorkPainter to perform a particular drawing operation."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QFont, QPen, QBrush

from worktoy.worktoyclass import WorkToyClass
from worktoy.descriptors import Field


class Graphic(WorkToyClass):
  """WorkSide - Draw - Graphic
  Settings used by WorkPainter to perform a particular drawing operation."""

  font = Field()
  pen = Field()
  brush = Field()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

  @font.getter
  def getFont(self, obj: object, *args) -> QFont:
    """Getter-function for the font."""

  @pen.getter
  def getPen(self, *args, ) -> QPen:
    """Getter-function for the pen."""

  @brush.getter
  def getPen(self, *args, ) -> QBrush:
    """Getter-function for the brush."""
