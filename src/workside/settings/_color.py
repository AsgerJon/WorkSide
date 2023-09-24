"""WorkSide - Settings - Color
Implementation of color specification"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Never

from PySide6.QtGui import QColor, QBrush, QPen

from workside.settings import Fill, Line
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class Color(WorkToyClass):
  """WorkSide - Settings - Color
  Implementation of color specification"""

  red = Attribute(255)
  green = Attribute(255)
  blue = Attribute(255)
  alpha = Attribute(255)
  Q = Attribute(QColor())
  brush = Attribute(QBrush())
  pen = Attribute(QPen())

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    intArgs = self.maybeTypes(int, *args, pad=4, padChar=255)
    self.red, self.green, self.blue, self.alpha = intArgs[:4]

  def __str__(self) -> str:
    """Provides a HEX code representation of the color. Please note that
    the alpha channel is omitted if it is 255, meaning full opacity."""
    RR = self.hexify(self.red)
    GG = self.hexify(self.green)
    BB = self.hexify(self.blue)
    AA = self.hexify(self.alpha) if self.alpha < 255 else ''
    return '#%s%s%s%s' % (RR, GG, BB, AA)

  def __repr__(self) -> str:
    """Provides a code representation. """
    r, g, b, a = self.red, self.green, self.blue, self.alpha
    clsName = self.__class__.__qualname__
    return '%s(%s, %s, %s, %s)' % (clsName, r, g, b, a)

  @Q.GET
  def _getQColor(self) -> QColor:
    """Getter function for QColor version"""
    return QColor(self.red, self.green, self.blue, self.alpha)

  @Q.SET
  def _setQColor(self, colorQ: QColor) -> None:
    """Setter function for QColor version"""
    self.red = colorQ.red()
    self.green = colorQ.green()
    self.blue = colorQ.blue()
    self.alpha = colorQ.alpha()

  @Q.DEL
  def _delQColor(self, ) -> Never:
    """Illegal deleter function"""
    raise TypeError

  @brush.GET
  def _getBrush(self) -> QBrush:
    """Getter-function for QBrush at this color with solid pattern"""
    out = QBrush()
    out.setStyle(Fill)
    out.setColor(self.Q)
    return out

  @brush.SET
  def _setBrush(self, brush: QBrush) -> None:
    """Setter-function for brush works by applying the color channels
    found in the brush color"""
    self.red = brush.color().red()
    self.green = brush.color().green()
    self.blue = brush.color().blue()
    self.alpha = brush.color().alpha()

  @brush.DEL
  def _delBrush(self) -> Never:
    """Illegal deleter function"""
    raise TypeError

  @pen.GET
  def _getPen(self) -> QPen:
    """Getter-function for QBrush at this color with solid pattern"""
    out = QPen()
    out.setStyle(Line)
    out.setColor(self.Q)
    return out

  @pen.SET
  def _setPen(self, pen: QPen) -> None:
    """Setter-function for brush works by applying the color channels
    found in the brush color"""
    self.red = pen.color().red()
    self.green = pen.color().green()
    self.blue = pen.color().blue()
    self.alpha = pen.color().alpha()

  @pen.DEL
  def _delPen(self) -> Never:
    """Illegal deleter function"""
    raise TypeError


White = Color(255, 255, 255, 255)
Platinum = Color(223, 223, 223, 255)
LightGray = Color(211, 211, 211, 255)
Silver = Color(192, 192, 192, 255)
DarkGray = Color(169, 169, 169, 255)
Gray = Color(128, 128, 128, 255)
DimGray = Color(105, 105, 105, 255)
Black = Color(0, 0, 0, 255)

Red = Color(255, 0, 0, 255)
Green = Color(0, 255, 0, 255)
Blue = Color(0, 0, 255, 255)

Yellow = Color(255, 255, 0, 255)
Magenta = Color(255, 0, 255, 255)
Cyan = Color(0, 255, 255, 255)

Orange = Color(255, 144, 0, 255)
Mint = Color(0, 255, 144, 255)
VividPurple = Color(144, 0, 255, 255)
Lime = Color(144, 255, 0, 255)
Azure = Color(0, 144, 255)
Pink = Color(255, 0, 144)
