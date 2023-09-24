"""WorkSide - StyleStates - MonoColorMapping
Creates a mapping from: ('val0', 'col0') to ('val0', 'col0') based on an
arbitrary numerical function. """
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from math import tanh
from typing import Any

from PySide6.QtGui import QColor
from icecream import ic

from workside.settings import Color, White, Black
from worktoy.core import Function
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


class MonoColorMapping(WorkToyClass):
  """WorkSide - StyleStates - MonoColorMapping
  Creates a mapping from: ('val0', 'col0') to ('val1', 'col1') based on an
  arbitrary numerical function. Each instance is a function factory
  allowing for use as a decorator. Alternatively, the instance may be
  called on existing functions.




  """

  startValue = Attribute()
  endValue = Attribute()
  startColor = Attribute()
  startColor.GET(lambda self: getattr(self, '__start_color__'))
  endColor = Attribute()
  endColor.GET(lambda self: getattr(self, '__end_color__'))

  startRed = Attribute()
  startRed.GET(lambda self: self.startColor.red)
  endRed = Attribute()
  startGreen = Attribute()
  endGreen = Attribute()
  startBlue = Attribute()
  endBlue = Attribute()
  startAlpha = Attribute()
  endAlpha = Attribute()

  slopeRed = Attribute()
  slopeGreen = Attribute()
  slopeBlue = Attribute()
  slopeAlpha = Attribute()

  dRed = Attribute()
  dGreen = Attribute()
  dBlue = Attribute()
  dAlpha = Attribute()

  y0 = Attribute()
  y1 = Attribute()
  dy = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    ic(args, kwargs)
    WorkToyClass.__init__(self, *args, **kwargs)
    floatArgs = self.maybeTypes(float, *args, pad=2, padChar=None)
    colorArgs = self.maybeTypes(Color, *args, pad=2, padChar=None)
    qColorArgs = self.maybeTypes(QColor, *args, pad=2, padChar=None)
    startColorKeys = self.stringList("""color0, startColor, firstColor""")
    endColorKeys = self.stringList("""color1, endColor, lastColor""")
    startValKeys = self.stringList("""startVal, val0, firstVal""")
    endValKeys = self.stringList("""endVal, val1, lastVal""")
    startColorKwarg = self.searchKey(*startColorKeys, **kwargs)
    endColorKwarg = self.searchKey(*endColorKeys, **kwargs)
    startValKwarg = self.stringList(*startValKeys, **kwargs)
    endValKwarg = self.stringList(*endValKeys, **kwargs)

    startValDefault, endValDefault = 0, 1
    startColorDefault, endColorDefault = Black, White
    startValFloat, endValFloat = floatArgs[:2]
    startColor, endColor = colorArgs[:2]
    startQColor, endQColor = qColorArgs[:2]
    startArgs = [startColor, startQColor]
    endArgs = [endColor, endQColor]
    ic(startArgs, endArgs)
    startColors = [startColorKwarg, startColor, startQColor]
    endColors = [endColorKwarg, endColor, endQColor]

    self.__start_value__ = floatArgs[0]
    self.__end_value__ = floatArgs[1]
    self.__start_color__ = self.maybe(*startColors)
    self.__end_color__ = self.maybe(*endColors)

    self.__start_red__ = self.__start_color__.red
    self.__start_green__ = self.__start_color__.green
    self.__start_blue__ = self.__start_color__.blue
    self.__start_alpha__ = self.__start_color__.alpha

    self.__inner_function__ = None
    self.__inner_value_start__ = None
    self.__inner_value_end__ = None
    self.__inner_value_diff__ = None

  def __call__(self, funcVal: Any) -> Any:
    if self.__inner_function__ is None:
      self._setInnerFunction(funcVal)
      return self
    return self._applyMapping(funcVal)

  def _getInnerFunction(self) -> Function:
    """Getter-function for inner function"""
    return self.functionGuard(self.__inner_function__)

  def _setInnerFunction(self, innerFunction: Function) -> None:
    """Setter-function for inner function"""
    self.__inner_function__ = self.functionGuard(innerFunction)

  @y0.GET
  def _getY0(self) -> float:
    """Getter-function for the mapped start value"""
    if self.__inner_value_start__ is None:
      innerFunction = self._getInnerFunction()
      self.__inner_value_start__ = innerFunction(self.startValue)
      return self._getY0()
    return self.__inner_value_start__

  @y1.GET
  def _getY1(self) -> float:
    """Getter-function for the mapped start value"""
    if self.__inner_value_end__ is None:
      innerFunction = self._getInnerFunction()
      self.__inner_value_end__ = innerFunction(self.endValue)
      return self._getY1()
    return self.__inner_value_end__

  @dy.GET
  def _getDy(self, ) -> float:
    """Getter-function for difference between 'y'-values. """
    return self.__end_value__ - self.__start_value__

  @slopeRed.GET
  def _getSlopeRed(self) -> float:
    """Getter-function for red slope"""
    return self.dRed / self.dy

  def _getSlopeGreen(self) -> float:
    """Getter-function for red slope"""
    return self.dGreen / self.dy

  def _getSlopeBlue(self) -> float:
    """Getter-function for red slope"""
    return self.dBlue / self.dy

  def _getSlopeAlpha(self) -> float:
    """Getter-function for red slope"""
    return self.dAlpha / self.dy

  def _getY(self, value: float) -> float:
    """Getter-function for the y value associated with given value."""
    innerFunction = self._getInnerFunction()
    return innerFunction(value)

  def _applyMapping(self, value: float) -> Color:
    """Applies the mapping to the given value"""
    innerFunction = self._getInnerFunction()
    y = innerFunction(value)
    red = int(self.startRed + (y - self.y0) / self.dy * self.dRed)
    green = int(self.startGreen + (y - self.y0) / self.dy * self.dGreen)
    blue = int(self.startBlue + (y - self.y0) / self.dy * self.dBlue)
    alpha = int(self.startAlpha + (y - self.y0) / self.dy * self.dAlpha)
    return Color(red, green, blue, alpha)
