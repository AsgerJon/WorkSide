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

  _namedStyles = dict(
    solid=Qt.PenStyle.SolidLine,
    dash=Qt.PenStyle.DashLine,
    dot=Qt.PenStyle.DotLine,
    dashDot=Qt.PenStyle.DashDotLine,
    dashDotDot=Qt.PenStyle.DashDotDotLine,
  )
  penStyle = Field(Qt.PenStyle.SolidLine)

  @penStyle.GET
  def getPenStyles(self, *_) -> Qt.PenStyle:
    """Getter-function for pen style"""
    return self.penStyle

  @classmethod
  def getNamedStyles(cls, ) -> dict[str, Qt.PenStyle]:
    """Getter-function for dictionary of named pen styles."""
    return cls._namedStyles

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    penStyleKeys = self.stringList("""penStyle, lineStyle""")
    kwargPenStyle = self.searchKey(penStyleKeys, **kwargs)
    argPenStyle = self.maybeType(Qt.PenStyle, *args)
    argStr = self.maybeTypes(str, *args)
    strArgStyle = None
    for name in argStr:
      style = self.getNamedStyles().get(name, None)
      if strArgStyle is None and style is not None:
        strArgStyle = style
    if not isinstance(kwargPenStyle, Qt.PenStyle):
      if isinstance(kwargPenStyle, str):
        kwargPenStyle = self.getNamedStyles().get(kwargPenStyle, None)
    defaultPenStyle = Qt.PenStyle.SolidLine
    candidates = [kwargPenStyle, argPenStyle, strArgStyle, defaultPenStyle, ]
    self._penStyle = self.maybe(candidates)

  def toolSupport(self, tool: type) -> bool:
    """QBrush, QPen and QColor is supported. In the case of QColor,
    the color is replaced with this color."""
    return True if tool is QPen else False

  def applyTool(self, other: Any) -> Any:
    """Applies this color to the given tool."""
    if isinstance(other, QPen):
      other.setStyle(self.penStyle)
      return other
