"""WorkSide - Tools - LineStyle
Parses a Qt.PenStyle"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
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
  penStyleKeys = Field()

  penStyle = Field(Qt.PenStyle.SolidLine)

  @penStyleKeys.GET
  def getPenStyleNames(self) -> list[str]:
    """Getter-function for list of pen style keys. """
    return self.stringList('penStyle, lineStyle')

  @classmethod
  def getNamedStyles(cls, ) -> dict[str, Qt.PenStyle]:
    """Getter-function for dictionary of named pen styles."""
    return cls._namedStyles

  def _parsePenStyleKwargs(self, ) -> Qt.PenStyle:
    """Parses keyword arguments"""
    for name in self.penStyleKeys:
      for key, val in self.getKeywordArgs().items():
        if name == key:
          if isinstance(val, Qt.PenStyle):
            self.useArg(key)
            return val
          if isinstance(val, str):
            style = self.getNamedStyles().get(val, None)
            if isinstance(style, Qt.PenStyle):
              self.useArg(key)
              return style

  def _parsePenStyleArgs(self, ) -> Qt.PenStyle:
    """Parses positional arguments"""
    for key, val in self.getPosArgs().items():
      if isinstance(val, Qt.PenStyle):
        self.useArg(key)
        return val
      if isinstance(val, str):
        style = self.getNamedStyles().get(val, None)
        if isinstance(style, Qt.PenStyle):
          self.useArg(key)
          return style

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    parsers = [self._parsePenStyleKwargs, self._parsePenStyleArgs]
    penStyle = None
    for parser in parsers:
      if penStyle is None:
        penStyle = parser()
    self.penStyle = self.maybe(penStyle, Qt.PenStyle.SolidLine)

  def toolSupport(self, tool: type) -> bool:
    """QBrush, QPen and QColor is supported. In the case of QColor,
    the color is replaced with this color."""
    return True if tool is QPen else False

  def applyTool(self, other: Any) -> Any:
    """Applies this color to the given tool."""
    if isinstance(other, QPen):
      other.setStyle(self.penStyle)
      return other

  @classmethod
  def saveToJson(cls, instance: LineStyle = None) -> str:
    """Implementation"""
    name = instance.penStyle.name
    value = instance.penStyle.value
    return json.dumps(dict(name=name, value=value))

  @classmethod
  def loadFromJson(cls, data: str) -> LineStyle:
    """Implementation"""
    data = json.loads(data)
    name, value = data['name'], data['value']
    for style in Qt.PenStyle:
      if style.name == name and style.value == value:
        return LineStyle(style)
    raise ValueError
