"""WorkSide - Draw - Color"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QColor
from icecream import ic

from worktoy.worktoyclass import WorkToyClass
from worktoy.descriptors import IntAttribute


class Color(WorkToyClass):
  """WorkSide - Settings - Styles - Color"""

  alpha = IntAttribute(255)
  red = IntAttribute(255)
  green = IntAttribute(255)
  blue = IntAttribute(255)

  def hexify(self, uint8: int) -> str:
    """Returns a string representation of the value given in HEX code."""
    H = self.stringList('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F')
    return '%s%s' % (H[int(uint8 // 16)], H[int(uint8 % 16)])

  @classmethod
  def getDefaultInstance(cls) -> Color:
    """Getter-function for default instance"""
    defaultInstance = cls(255, 255, 255, 255)
    return defaultInstance

  def __init__(self, *args, **kwargs) -> None:
    if kwargs.get('_recursion', False):
      return
    ic(args)
    WorkToyClass.__init__(self, *args, **kwargs)
    redKwarg = self.maybeKey(int, 'red', **kwargs)
    greenKwarg = self.maybeKey(int, 'green', **kwargs)
    blueKwarg = self.maybeKey(int, 'blue', **kwargs)
    alphaKwarg = self.maybeKey(int, 'alpha', **kwargs)
    rgba = self.maybeTypes(int, *args, padChar=None, pad=4)
    redArg, greenArg, blueArg, alphaArg = rgba
    defaultValues = 255, 255, 255, 0
    redDefault, greenDefault, blueDefault, alphaDefault = defaultValues
    self.red = self.maybe(redKwarg, redArg, redDefault)
    ic(redKwarg, redArg, redDefault, self.red)
    self.green = self.maybe(greenKwarg, greenArg, greenDefault)
    self.blue = self.maybe(blueKwarg, blueArg, blueDefault)
    self.alpha = self.maybe(alphaKwarg, alphaArg, alphaDefault)
    ic(self.red, self.green, self.blue, self.alpha, )
    ic(self)
    return self.__init__(*args, **kwargs, _recursion=True)

  def asQColor(self) -> QColor:
    """Returns QColor representation"""
    return QColor(self.red, self.green, self.blue, self.alpha)

  def __str__(self, ) -> str:
    """String representation."""
    red = self.hexify(self.red)
    green = self.hexify(self.green)
    blue = self.hexify(self.blue)
    return '#%s%s%s' % (red, green, blue)

  def __repr__(self, ) -> str:
    """Code representation."""
    return 'RBG(%d, %d, %d)' % (self.red, self.green, self.blue)
