"""WorkSide - Tools - Color
Class representation of colors. Provides parsing and blending. Subclasses
can extend this behaviour as needed."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Optional, Any

from PySide6.QtGui import QColor, QPen, QBrush
from icecream import ic
from worktoy.descriptors import Field

from workside.tools import AbstractTools

NumColor = Optional[tuple[int, int, int, int]]
FloatColor = tuple[float, float, float, float]

ic.configureOutput(includeContext=True)


class Color(AbstractTools):
  """WorkSide - Utilities - Color
  Class representation of colors. Provides parsing and blending. Subclasses
  can extend this behaviour as needed."""

  Q = Field()
  F = Field()

  red = Field()
  green = Field()
  blue = Field()
  alpha = Field()

  redF = Field()
  greenF = Field()
  blueF = Field()
  alphaF = Field()

  redKeys = Field()
  greenKeys = Field()
  blueKeys = Field()
  alphaKeys = Field()
  colorKeys = Field()

  @F.GET
  def getColorF(self) -> FloatColor:
    """Getter-function for the rgba tuple with channels at unit scale."""
    red = self.red
    green = self.green
    blue = self.blue
    alpha = self.alpha
    rgba = [red, green, blue, alpha]
    rgbaF = [c / 255 for c in rgba]
    return tuple(*rgbaF, )

  @redF.GET
  def getRedF(self) -> float:
    """Getter-function for the unit scale of red"""
    return self.red / 255

  @greenF.GET
  def getGreenF(self) -> float:
    """Getter-function for the unit scale of green"""
    return self.green / 255

  @blueF.GET
  def getBlueF(self) -> float:
    """Getter-function for the unit scale of blue"""
    return self.blue / 255

  @alphaF.GET
  def getAlphaF(self) -> float:
    """Getter-function for the unit scale of alpha"""
    return self.alpha / 255

  @Q.GET
  def getQColor(self) -> QColor:
    """Getter-function for this color as an instance of QColor."""
    red, green, blue, alpha = self.red, self.green, self.blue, self.alpha
    return QColor(red, green, blue, alpha)

  @red.GET
  def getRed(self, *_) -> int:
    """Getter-function for red color"""
    return self.maybe(self._red, 0)

  @red.SET
  def setRed(self, newRed: int) -> None:
    """Setter-function for red color"""
    self._red = newRed

  @green.GET
  def getGreen(self) -> int:
    """Getter-function for green color"""
    return self.maybe(self._green, 0)

  @green.SET
  def setGreen(self, newGreen: int) -> None:
    """Setter-function for green color"""
    self._green = newGreen

  @blue.GET
  def getBlue(self) -> int:
    """Getter-function for blue color"""
    return self.maybe(self._blue, 0)

  @blue.SET
  def setBlue(self, newBlue: int) -> None:
    """Setter-function for blue color"""
    self._blue = newBlue

  @alpha.GET
  def getAlpha(self) -> int:
    """Getter-function for alpha color"""
    return self.maybe(self._alpha, 255)

  @alpha.SET
  def setAlpha(self, newAlpha: int) -> None:
    """Setter-function for alpha color"""
    self._alpha = newAlpha

  @redKeys.GET
  def getRedKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""red, Red, RED, r, R""")
    return [k for k in keys if isinstance(k, str)]

  @greenKeys.GET
  def getGreenKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""green, Green, GREEN, g, G""")
    return [k for k in keys if isinstance(k, str)]

  @blueKeys.GET
  def getBlueKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""blue, Blue, BLUE, b, B""")
    return [k for k in keys if isinstance(k, str)]

  @alphaKeys.GET
  def getAlphaKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""alpha, Alpha, ALPHA, r, R, opacity, Opacity""")
    return [k for k in keys if isinstance(k, str)]

  @colorKeys.GET
  def getColorKeys(self, *_) -> list[str]:
    """Getter-function for color keys"""
    keys = self.stringList("""color, Color, QColor, RGB, rgb""")
    return [k for k in keys if isinstance(k, str)]

  def hexify(self, uint8: int) -> str:
    """Returns a string representation of the value given in HEX code."""
    H = self.stringList('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F')
    return '%s%s' % (H[int(uint8 // 16)], H[int(uint8 % 16)])

  def _parseNumKwarg(self, ) -> NumColor:
    """Parses keyword arguments"""
    kwarg = dict(red=None, green=None, blue=None, alpha=255)
    _temp = []
    keys = [self.redKeys, self.greenKeys, self.blueKeys, self.alphaKeys]
    names = self.stringList('red, green, blue, alpha')
    for kw, color in zip(keys, names):
      for name in kw:
        for key, val in self.getKeywordArgs().items():
          if name == key and kwarg[color] is None:
            if isinstance(val, int):
              if -1 < val < 256:
                kwarg[color] = val
                _temp.append((key, val))
            elif isinstance(val, float):
              if 1 < val < 256:
                kwarg[color] = int(val)
                _temp.append((key, val))
              if 0 <= val <= 1:
                kwarg[color] = int(255 * val)
                _temp.append((key, val))
    if all([kwarg[key] is not None for key in names]):
      colors = []
      for key, val in kwarg.items():
        self.useArg(key)
        if isinstance(val, int):
          colors.append(val)
      red, green, blue, alpha = colors
      return red, green, blue, alpha

  def _parseNumArg(self, ) -> NumColor:
    """Parses positional arguments"""
    intArgs = []
    unitArgs = []
    _temp = []
    for key, val in self.getPosArgs().items():
      if isinstance(val, int):
        if -1 < val < 256:
          intArgs.append(val)
          if val in [0, 1]:
            unitArgs.append(val)
          _temp.append((key, val))
      elif isinstance(val, float):
        if 1 < val < 256:
          intArgs.append(int(val))
          _temp.append((key, val))
        if 0 <= val <= 1:
          intArgs.append(int(255 * val))
          unitArgs.append(val)
          _temp.append((key, val))
    if len(intArgs) == 3:
      if len(unitArgs) == 3:
        unitArgs.append(1)
        intArgs = [255 * i for i in unitArgs]
      else:
        intArgs.append(255)
      red, green, blue, alpha = intArgs
      self.useArgs(_temp)
      return red, green, blue, alpha
    if len(intArgs) > 3:
      if len(unitArgs) > 3:
        intArgs = [255 * i for i in unitArgs[:4]]
      red, green, blue, alpha = intArgs[:4]
      self.useArgs(_temp)
      return red, green, blue, alpha

  def _parseColorKwarg(self) -> NumColor:
    """Parses keyword arguments for instances of Color or QColor"""
    for name in self.colorKeys:
      col = self.getKeywordArgs().get(name, None)
      if isinstance(col, Color):
        self.useArg(name)
        return col.red, col.green, col.blue, col.alpha
      if isinstance(col, QColor):
        self.useArg(name)
        return col.red(), col.green(), col.blue(), col.alpha()

  def _parseColorArg(self, ) -> NumColor:
    """Parses positional arguments for instances of Color or QColor"""
    for (key, col) in self.getPosArgs().items():
      if isinstance(col, Color):
        self.useArg(key)
        return col.red, col.green, col.blue, col.alpha
      if isinstance(col, QColor):
        self.useArg(key)
        return col.red(), col.green(), col.blue(), col.alpha()

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    parsers = [
      self._parseColorKwarg,
      self._parseColorArg,
      self._parseNumKwarg,
      self._parseNumArg,
    ]
    rgba = None
    for parser in parsers:
      if rgba is None:
        rgba = parser()

    rgba = self.maybe(rgba, (0, 0, 0, 255))
    self.red, self.green, self.blue, self.alpha = rgba

  def toolSupport(self, tool: type) -> bool:
    """QBrush, QPen and QColor is supported. In the case of QColor,
    the color is replaced with this color."""
    supportedTools = [QBrush, QPen, QColor]
    return True if tool in supportedTools else False

  def applyTool(self, other: Any) -> Any:
    """Applies this color to the given tool."""
    if isinstance(other, (QBrush, QPen)):
      other.setColor(self.Q)
      return other
    if isinstance(other, QColor):
      return self.Q

  def __str__(self, ) -> str:
    """String representation."""
    red = self.hexify(self.red)
    green = self.hexify(self.green)
    blue = self.hexify(self.blue)
    alpha = self.hexify(self.alpha)
    if self.alpha < 255:
      return '#%s%s%s%s' % (red, green, blue, alpha)
    return '#%s%s%s' % (red, green, blue,)

  def __repr__(self, ) -> str:
    """Code representation."""
    red = self.red
    green = self.green
    blue = self.blue
    alpha = self.alpha
    return 'Color(%d, %d, %d, %d)' % (red, green, blue, alpha)

  def __bool__(self, ) -> bool:
    """The boolean checks if the alpha channel is zero"""
    return True if self.alpha else False

  def __eq__(self, other: Any) -> bool:
    """Ignores the alpha channel."""
    if isinstance(other, Color):
      if self.red - other.red:
        return False
      if self.green - other.green:
        return False
      if self.blue - other.blue:
        return False
      return True
    if isinstance(other, QColor):
      return self == Color(other)

  def __abs__(self) -> float:
    """The absolute value is understood to be the length of the rgb vector:
    RGB = <red, green, blue>
    abs(RGB) * alpha / 255"""
    red, green, blue, alpha = self.red, self.green, self.blue, self.alpha
    return (red ** 2 + green ** 2 + blue ** 2) ** 0.5 * alpha / 255

  def __pos__(self, ) -> Color:
    """Creates a copy of this color with full opacity"""
    newColor = Color(self)
    newColor.alpha = 255
    return newColor

  def __sub__(self, other: Color) -> float:
    """Estimates the difference between self and other"""
    redMean = 0.5 * self.redF + 0.5 * other.redF
    dRed = self.redF - other.redF
    dGreen = self.greenF - other.greenF
    dBlue = self.blueF - other.blueF
    d2red = (2 + redMean) * dRed ** 2
    d2green = 4 * dGreen ** 2
    d2blue = (3 - redMean) * dBlue ** 2
    return (d2red + d2green + d2blue) ** 0.5

  @classmethod
  def saveToJson(cls, instance: Color = None) -> str:
    """Implementation."""
    data = dict(red=instance.red, green=instance.green,
                blue=instance.blue, alpha=instance.alpha)
    return json.dumps(data)

  @classmethod
  def loadToJson(cls, data: str) -> Color:
    """Implementation"""
    rgb = json.loads(data)
    return cls(rgb['red'], rgb['green'], rgb['blue'], rgb['alpha'])
