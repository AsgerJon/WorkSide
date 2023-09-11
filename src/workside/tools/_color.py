"""WorkSide - Tools - Color
Class representation of colors. Provides parsing and blending. Subclasses
can extend this behaviour as needed."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

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

  @F.getter
  def getColorF(self) -> FloatColor:
    """Getter-function for the rgba tuple with channels at unit scale."""
    red = self.red
    green = self.green
    blue = self.blue
    alpha = self.alpha
    rgba = [red, green, blue, alpha]
    rgbaF = [c / 255 for c in rgba]
    return tuple(*rgbaF, )

  @redF.getter
  def getRedF(self) -> float:
    """Getter-function for the unit scale of red"""
    return self.red / 255

  @greenF.getter
  def getGreenF(self) -> float:
    """Getter-function for the unit scale of green"""
    return self.green / 255

  @blueF.getter
  def getBlueF(self) -> float:
    """Getter-function for the unit scale of blue"""
    return self.blue / 255

  @alphaF.getter
  def getAlphaF(self) -> float:
    """Getter-function for the unit scale of alpha"""
    return self.alpha / 255

  @Q.getter
  def getQColor(self) -> QColor:
    """Getter-function for this color as an instance of QColor."""
    red, green, blue, alpha = self.red, self.green, self.blue, self.alpha
    return QColor(red, green, blue, alpha)

  @redF.getter
  def getRedF(self, *_) -> float:
    """Returns the floating point at unit scale"""

  @red.getter
  def getRed(self, *_) -> int:
    """Getter-function for red color"""
    return self.maybe(self._red, 0)

  @red.setter
  def setRed(self, newRed: int) -> None:
    """Setter-function for red color"""
    self._red = newRed

  @green.getter
  def getGreen(self) -> int:
    """Getter-function for green color"""
    return self.maybe(self._green, 0)

  @green.setter
  def setGreen(self, newGreen: int) -> None:
    """Setter-function for green color"""
    self._green = newGreen

  @blue.getter
  def getBlue(self) -> int:
    """Getter-function for blue color"""
    return self.maybe(self._blue, 0)

  @blue.setter
  def setBlue(self, newBlue: int) -> None:
    """Setter-function for blue color"""
    self._blue = newBlue

  @alpha.getter
  def getAlpha(self) -> int:
    """Getter-function for alpha color"""
    return self.maybe(self._alpha, 255)

  @alpha.setter
  def setAlpha(self, newAlpha: int) -> None:
    """Setter-function for alpha color"""
    self._alpha = newAlpha

  @redKeys.getter
  def getRedKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""red, Red, RED, r, R""")
    return [k for k in keys if isinstance(k, str)]

  @greenKeys.getter
  def getGreenKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""green, Green, GREEN, g, G""")
    return [k for k in keys if isinstance(k, str)]

  @blueKeys.getter
  def getBlueKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""blue, Blue, BLUE, b, B""")
    return [k for k in keys if isinstance(k, str)]

  @alphaKeys.getter
  def getAlphaKeys(self, *_) -> list[str]:
    """Getter-function for red keys"""
    keys = self.stringList("""alpha, Alpha, ALPHA, r, R, opacity, Opacity""")
    return [k for k in keys if isinstance(k, str)]

  @colorKeys.getter
  def getColorKeys(self, *_) -> list[str]:
    """Getter-function for color keys"""
    keys = self.stringList("""color, Color, QColor, RGB, rgb""")
    return [k for k in keys if isinstance(k, str)]

  def hexify(self, uint8: int) -> str:
    """Returns a string representation of the value given in HEX code."""
    H = self.stringList('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F')
    return '%s%s' % (H[int(uint8 // 16)], H[int(uint8 % 16)])

  def _floatArgParse(self, *args) -> NumColor:
    """Parses float valued positional arguments"""
    floatArgs = self.maybeTypes(float, *args)
    intArgs = []
    for arg in floatArgs:
      if 0 <= arg <= 1:
        intArgs.append(int(255 * arg))
    if len(intArgs) > 2:
      red, green, blue = intArgs[:3]
      alpha = 255
      if len(intArgs) > 3:
        alpha = intArgs[3]
      return red, green, blue, alpha

  def _intArgParse(self, *args) -> NumColor:
    """Parses positional arguments"""
    intArgs = self.maybeTypes(int, *args)
    intArgs = [i for i in intArgs if -1 < i < 256]
    intArgs = [i for i in intArgs if isinstance(i, int)]
    if len(intArgs) > 2:
      red, green, blue = intArgs[:3]
      alpha = 255
      if len(intArgs) > 3:
        alpha = intArgs[3]
      if all([i in [0, 1] for i in [red, green, blue]]):
        red *= 255
        green *= 255
        blue *= 255
        if alpha == 1:
          alpha = 255
      return red, green, blue, alpha

  def _intKwargParse(self, **kwargs) -> NumColor:
    """Parses keyword arguments"""
    redKwarg = self.searchKey(int, *self.redKeys, **kwargs)
    greenKwarg = self.searchKey(int, *self.greenKeys, **kwargs)
    blueKwarg = self.searchKey(int, *self.blueKeys, **kwargs)
    alphaKwarg = self.searchKey(int, *self.alphaKeys, **kwargs)
    if all([arg is not None for arg in [redKwarg, greenKwarg, blueKwarg]]):
      return redKwarg, greenKwarg, blueKwarg, self.maybe(alphaKwarg, 255)

  def _floatKwargParse(self, **kwargs) -> NumColor:
    """Parses keyword arguments"""
    redKwarg = self.searchKey(float, *self.redKeys, **kwargs)
    greenKwarg = self.searchKey(float, *self.greenKeys, **kwargs)
    blueKwarg = self.searchKey(float, *self.blueKeys, **kwargs)
    alphaKwarg = self.searchKey(int, *self.alphaKeys, **kwargs)
    floatArgs = [redKwarg, greenKwarg, blueKwarg]
    if all([i is not None for i in floatArgs]):
      intArgs = []
      for arg in floatArgs:
        if 0 <= arg <= 1:
          intArgs.append(int(arg * 255))
        elif 0 < int(arg) < 256:
          intArgs.append(int(arg))
        else:
          return
      if len(intArgs) > 2:
        red, green, blue = intArgs[:3]
        alpha = self.maybe(alphaKwarg, 255)
        if len(intArgs) > 3:
          alpha = intArgs[3]
        return red, green, blue, alpha

  def _parseNumeric(self, *args, **kwargs, ) -> dict[str, int]:
    intKwargs = self._intKwargParse(**kwargs)
    floatKwargs = self._floatKwargParse(**kwargs)
    intArgs = self._intArgParse(*args)
    floatArgs = self._floatArgParse(*args)
    dictIntArg = None
    dictFloatArg = None
    listIntArg = None
    listFloatArg = None
    dictArg = self.maybeType(dict, *args)
    listArg = self.maybeType(list, *args)
    if isinstance(dictArg, dict):
      dictIntArg = self._intKwargParse(**kwargs)
      dictFloatArg = self._floatKwargParse(**kwargs)
    if isinstance(listArg, list):
      listIntArg = self._intArgParse(*args)
      listFloatArg = self._floatArgParse(*args)
    rgbArgs = [intKwargs, floatKwargs, intArgs, floatArgs,
               dictIntArg, dictFloatArg, listIntArg, listFloatArg]
    numColor = self.maybe(*rgbArgs)
    if numColor is not None:
      r, g, b, a = numColor
      return dict(red=r, green=g, blue=b, alpha=a)

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    self._red, self._green, self._blue, self._alpha = 0, 0, 0, 255
    numColor = self._parseNumeric(*args, **kwargs)
    if isinstance(numColor, dict):
      self.red = numColor.get('red', None)
      self.blue = numColor.get('blue', None)
      self.green = numColor.get('green', None)
      self.alpha = numColor.get('alpha', None)

    argColor = self.maybeType(Color, *args)
    argQColor = self.maybeType(QColor, *args)
    colorKwarg = self.searchKeys(*self.colorKeys, **kwargs)
    colorArg = self.maybe(colorKwarg, argColor, argQColor)

    if isinstance(colorArg, QColor):
      self.red = colorArg.red()
      self.blue = colorArg.blue()
      self.green = colorArg.green()
      self.alpha = colorArg.alpha()

    if isinstance(colorArg, Color):
      self.red = colorArg.red
      self.green = colorArg.green
      self.blue = colorArg.blue
      self.alpha = colorArg.alpha

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
