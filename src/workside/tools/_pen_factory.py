"""WorkSide - Tools - PenFactory
Function creating instances of QPen."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen

from workside.tools import AbstractFactory, Color, LineStyle


class PenFactory(AbstractFactory):
  """WorkSide - Tools - PenFactory
  Function creating instances of QPen."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractFactory.__init__(self, *args, **kwargs)
    self._defaultStyle = Qt.PenStyle.SolidLine
    self._defaultColor = Color(0, 0, 0, 255)
    self._defaultWidth = 1

  def __call__(self, *args) -> QPen:
    """On calling the instance a new instance of QPen is created."""
    penStyle = None
    penColor = None
    penWidth = None
    names = self.stringList("""penStyle, penColor, penWidth""")
    for arg in args:
      if isinstance(arg, LineStyle) and penStyle is None:
        penStyle = arg
      if isinstance(arg, Color) and penColor is None:
        penColor = arg
      if isinstance(arg, int) and penWidth is None:
        penWidth = arg
    styles = [penStyle, penColor, penWidth]
    for name, style in zip(names, styles):
      if style is None:
        from worktoy.waitaminute import MissingArgumentException
        raise MissingArgumentException(name)
    pen = QPen()

    pen.setStyle(penStyle)
    pen.setColor(penColor)
    pen.setWidth(penWidth)
    return pen
