"""WorkSide - Tools - LineWidth
Class representation of line width."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Any

from PySide6.QtGui import QPen
from icecream import ic
from worktoy.descriptors import Field

from workside.tools import AbstractTools

ic.configureOutput(includeContext=True)


class LineWidth(AbstractTools):
  """WorkSide - Tools - LineWidth
  Class representation of line width."""

  lineWidthKeys = Field()
  width = Field()

  @lineWidthKeys.GET
  def getLineWidthKeys(self) -> list[str]:
    """Getter-function for list of line width keys"""
    return self.stringList("""width, w, lineWidth, lineThickness,
      thickness""")

  @width.GET
  def getWidth(self) -> int:
    """Getter-function for width"""
    return self._innerValue

  def _parseKwargs(self) -> float:
    """Parses keyword arguments"""
    for name in self.lineWidthKeys:
      for key, val in self.getKeywordArgs().items():
        if name == key and isinstance(val, (float, int)):
          self.useArg(key)
          return val

  def _parseArgs(self, ) -> float:
    """Parses positional arguments"""
    for key, val in self.getPosArgs().items():
      if isinstance(val, (float, int)):
        self.useArg(key)
        return val

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    w = None
    parsers = [self._parseKwargs, self._parseArgs]
    for parser in parsers:
      if w is None:
        w = parser()
    self._innerValue = self.maybe(w, 1)
    self._innerType = int if isinstance(w, int) else float

  def toolSupport(self, tool: type) -> bool:
    """Supports the original QPen and the WorkPen"""
    return True if tool in [QPen] else False

  def applyTool(self, other: Any) -> Any:
    """Applies inner value as the width of the QPen."""
    if isinstance(other, QPen):
      if self._innerType is int:
        other.setWidth(self._innerValue)
      else:
        other.setWidthF(self._innerValue)
      return other

  @classmethod
  def saveToJson(cls, instance: LineWidth = None) -> str:
    """Implementation"""
    return json.dumps(dict(width=instance.width))
