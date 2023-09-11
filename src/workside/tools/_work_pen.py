"""WorkSide - Tools - WorkPen
Subclass of QPen."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any, Optional

from PySide6.QtGui import QPen, QPainter
from worktoy.descriptors import Field

from workside.tools import Color, LineStyle, LineWidth
from workside.tools import AbstractTools


class WorkPen(QPen, AbstractTools):
  """WorkSide - Tools - WorkPen
  Subclass of QPen."""

  penKeys = Field()

  @penKeys.GET
  def getPenKeys(self) -> list[str]:
    """Getter-function for pen keys"""
    return self.stringList("""pen, Pen, QPen, line""")

  def parseKwargs(self, ) -> Optional[QPen]:
    """Parses keyword arguments"""
    for name in self.penKeys:
      for key, val in self.getKeywordArgs().items():
        if name == key and isinstance(val, QPen):
          self.useArg(key)
          return val

  def parseArgs(self, ) -> Optional[QPen]:
    """Parses positional arguments"""
    for key, val in self.getPosArgs().items():
      if isinstance(val, QPen):
        self.useArg(key)
        return val

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    QPen.__init__(self, )
    posArgs = args
    keyWordArgs = kwargs
    argPen = None
    parsers = [self.parseKwargs, self.parseArgs]
    for parser in parsers:
      if argPen is None:
        argPen = parser()
    if argPen is None:
      color = Color(*posArgs, **keyWordArgs)
      posArgs, keyWordArgs = color.getPosArgs(), color.getKeywordArgs()
      penStyle = LineStyle(*posArgs, **keyWordArgs)
      posArgs, keyWordArgs = penStyle.getPosArgs(), penStyle.getKeywordArgs()
      lineWidth = LineWidth(*posArgs, **keyWordArgs)
      posArgs, keyWordArgs = (lineWidth.getPosArgs(),
                              lineWidth.getKeywordArgs())
      self.setArgs(*posArgs)
      self.setKwargs(**keyWordArgs)
    else:
      color = Color(argPen.color())
      penStyle = LineStyle(argPen.style())
      lineWidth = LineWidth(argPen.widthF())
    color >> self
    penStyle >> self
    lineWidth >> self

  def fromJson(self, data: str) -> None:
    """Instantiates WorkPen from the json data."""
    raise NotImplementedError

  def toolSupport(self, tool: type) -> bool:
    """Supports QPainter"""
    return True if tool in [QPainter, QPen] else False

  def applyTool(self, other: Any) -> Any:
    """If other is QPainter, then sets its pen to self. If other is QPen,
    sets its values to those of self."""
    if isinstance(other, QPainter):
      other.setPen(self)
    if isinstance(other, QPen):
      other.setStyle(self.style())
      other.setColor(self.color())
      other.setWidthF(self.widthF())
    return other
