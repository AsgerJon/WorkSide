"""WorkSide - Paint - Color
Custom subclass of QColor"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QColor
from worktoy.descriptors import Field
from worktoy.worktoyclass import WorkToyClass


class Color(QColor, WorkToyClass):
  """WorkSide - Paint - Color
  Custom subclass of QColor"""

  Q = Field()
  red = Field()
  green = Field()
  blue = Field()
  alpha = Field()
  redF = Field()
  greenF = Field()
  blueF = Field()
  alphaF = Field()

  @Q.GET
  def getQColor(self) -> QColor:
    """Getter-function for QColor version."""
    return QColor(self.red, self.green, self.blue, self.alpha)

  @red.GET
  def getRed(self, ) -> int:
    """Getter function for red"""
    return self._red

  @red.SET
  def setRed(self, newValue: int) -> None:
    """Setter function for red"""
    self._red = newValue

  @green.GET
  def getGreen(self, ) -> int:
    """Getter function for green"""
    return self._green

  @green.SET
  def setGreen(self, newValue: int) -> None:
    """Setter function for green"""
    self._green = newValue

  @blue.GET
  def getBlue(self, ) -> int:
    """Getter function for blue"""
    return self._blue

  @blue.SET
  def setBlue(self, newValue: int) -> None:
    """Setter function for blue"""
    self._blue = newValue

  @alpha.GET
  def getAlpha(self, ) -> int:
    """Getter function for alpha"""
    return self._alpha

  @alpha.SET
  def setAlpha(self, newValue: int) -> None:
    """Setter function for alpha"""
    self._alpha = newValue

  @redF.GET
  def getRedF(self, ) -> float:
    """Getter function for redF"""
    return float(self._red) / 255

  @greenF.GET
  def getGreenF(self, ) -> float:
    """Getter function for greenF"""
    return float(self._green) / 255

  @blueF.GET
  def getBlueF(self, ) -> float:
    """Getter function for blueF"""
    return float(self._blue) / 255

  @alphaF.GET
  def getAlphaF(self, ) -> float:
    """Getter function for alphaF"""
    return float(self._alpha) / 255

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    QColor.__init__(self, )
    redKwarg = kwargs.get('red', None)
    greenKwarg = kwargs.get('green', None)
    blueKwarg = kwargs.get('blue', None)
    alphaKwarg = kwargs.get('alpha', None)
    intArgs = self.maybeTypes(int, *args)
    redArg, greenArg, blueArg = 0, 0, 0
    if len(intArgs) > 2:
      redArg, greenArg, blueArg = intArgs[:3]
    alphaArg = 255 if len(intArgs) < 4 else intArgs[3]
    self._red = self.maybe(redKwarg, redArg, )
    self._green = self.maybe(greenKwarg, greenArg, )
    self._blue = self.maybe(blueKwarg, blueArg, )
    self._alpha = self.maybe(alphaKwarg, alphaArg, )

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
