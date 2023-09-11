"""WorkSide - Tools - LineStyle
Parses a Qt.PenStyle"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen
from worktoy.descriptors import Field

from workside.tools import AbstractTools


class LineStyle(AbstractTools):
  """WorkSide - Tools - LineStyle
  Parses a Qt.PenStyle"""

  penStyle = Field(Qt.PenStyle.SolidLine)

  @penStyle.getter
  def getPenStyle(self, *_) -> Qt.PenStyle:
    """Getter-function for pen style"""
    return self._penStyle

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    penStyleKeys = self.stringList("""penStyle, lineStyle""")
    kwargPenStyle = self.searchKey(penStyleKeys, **kwargs)
    argPenStyle = self.maybeType(Qt.PenStyle, *args)
    defaultPenStyle = Qt.PenStyle.SolidLine
    self._penStyle = self.maybe(kwargPenStyle, argPenStyle, defaultPenStyle)

  def toolSupport(self, tool: type) -> bool:
    """QBrush, QPen and QColor is supported. In the case of QColor,
    the color is replaced with this color."""
    return True if tool is QPen else False

  def applyTool(self, other: Any) -> Any:
    """Applies this color to the given tool."""
    if isinstance(other, QPen):
      other.setStyle(self.penStyle)
      return other
