"""WorkSide - Tools - Color
Class representation of colors. Provides parsing and blending. Subclasses
can extend this behaviour as needed."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Optional

from PySide6.QtGui import QColor
from icecream import ic
from worktoy.descriptors import IntAttribute, Field
from worktoy.worktoyclass import WorkToyClass

NumColor = Optional[tuple[int, int, int, int]]

ic.configureOutput(includeContext=True)


class Color(WorkToyClass):
  """WorkSide - Utilities - Color
  Class representation of colors. Provides parsing and blending. Subclasses
  can extend this behaviour as needed."""

  red = Field()
  green = Field()
  blue = Field()
  alpha = Field()

  redKeys = Field()
  greenKeys = Field()
  blueKeys = Field()
  alphaKeys = Field()
  colorKeys = Field()

  @red.getter
  def getRed(self, *args) -> int:
    """Getter-function for red color"""
    ic(args)
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
    self._red, self._green, self._blue, self._alpha = 0, 0, 0, 255
    ic(self)
    WorkToyClass.__init__(self, *args, **kwargs)
    numColor = self._parseNumeric(*args, **kwargs)
    ic(numColor)
    if isinstance(numColor, dict):
      ic(numColor)
      ic(numColor.get('red', None))
      ic(numColor.get('green', None))
      ic(numColor.get('blue', None))
      ic(numColor.get('alpha', None))
      ic(self)
      self.red = numColor.get('red', None)
      self.blue = numColor.get('blue', None)
      self.green = numColor.get('green', None)
      self.alpha = numColor.get('alpha', None)
      ic(self)

    argColor = self.maybeType(Color, *args)
    argQColor = self.maybeType(QColor, *args)
    colorKwarg = self.searchKeys(*self.colorKeys, **kwargs)
    colorArg = self.maybe(colorKwarg, argColor, argQColor)
    ic(colorArg)
    ic(self)

    if isinstance(colorArg, QColor):
      self.red = colorArg.red()
      self.blue = colorArg.blue()
      self.green = colorArg.green()
      self.alpha = colorArg.alpha()
    ic(self)

    if isinstance(colorArg, Color):
      ic(type(colorArg))
      ic(colorArg.red)
      ic(self.red)
      self.red = colorArg.red
      ic(self.red)
      ic(self.green)
      self.green = colorArg.green
      ic(self.green)
      ic(self.blue)
      self.blue = colorArg.blue
      ic(self.blue)
      ic(self.alpha)
      self.alpha = colorArg.alpha
      ic(self.alpha)
    ic(self)

  def __str__(self, ) -> str:
    """String representation."""
    ic(type(self))
    ic(self.red)
    ic(self.green)
    ic(self.blue)
    ic(self.alpha)
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
