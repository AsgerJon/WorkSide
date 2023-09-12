"""WorkSide - Paint - ColorSpec
Dataclass specification for colors"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Any

from icecream import ic
from worktoy.descriptors import DataClass, DataField
from worktoy.worktoyclass import WorkToyClass

from workside.moreworktoy import CoreField, AutoField

ic.configureOutput(includeContext=True)


@DataClass()
class ColorSpec(WorkToyClass):
  """WorkSide - Paint - ColorSpec
  Dataclass specification for colors"""

  @classmethod
  def ORANGE(cls) -> ColorSpec:
    """Standard color"""
    return cls(255, 144, 0, 255)

  @classmethod
  def MINT(cls) -> ColorSpec:
    """Standard color"""
    return cls(0, 255, 144, 255)

  @classmethod
  def PURPLE(cls) -> ColorSpec:
    """Standard color"""
    return cls(144, 0, 255, 255)

  @classmethod
  def LIME(cls) -> ColorSpec:
    """Standard color"""
    return cls(144, 255, 0, 255)

  @classmethod
  def ROYALBLUE(cls) -> ColorSpec:
    """Standard color"""
    return cls(0, 144, 255, 255)

  @classmethod
  def PINK(cls) -> ColorSpec:
    """Standard color"""
    return cls(255, 0, 144, 255)

  @classmethod
  def RED(cls) -> ColorSpec:
    """Standard color"""
    return cls(255, 0, 0, 255)

  @classmethod
  def GREEN(cls) -> ColorSpec:
    """Standard color"""
    return cls(0, 255, 0, 255)

  @classmethod
  def BLUE(cls) -> ColorSpec:
    """Standard color"""
    return cls(0, 0, 255, 255)

  @classmethod
  def MAGENTA(cls) -> ColorSpec:
    """Standard color"""
    return cls(255, 0, 255, 255)

  @classmethod
  def CYAN(cls) -> ColorSpec:
    """Standard color"""
    return cls(0, 255, 255, 255)

  @classmethod
  def YELLOW(cls) -> ColorSpec:
    """Standard color"""
    return cls(255, 255, 0, 255)

  red = CoreField(0)
  green = CoreField(0)
  blue = CoreField(0)
  alpha = CoreField(0)

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    intArgs = self.maybeTypes(int, *args)
    redKwarg = kwargs.get('red', None)
    greenKwarg = kwargs.get('green', None)
    blueKwarg = kwargs.get('blue', None)
    alphaKwarg = kwargs.get('alpha', None)
    redArg, greenArg, blueArg, alphaArg = None, None, None, None
    if len(intArgs) > 2:
      redArg, greenArg, blueArg = intArgs[:3]
    if len(intArgs) > 3:
      alphaArg = intArgs[3]
    if not self.plenty(redKwarg, greenKwarg, blueKwarg):
      redKwarg, greenKwarg, blueKwarg = None, None, None
    if not self.plenty(redArg, greenArg, blueArg):
      redArg, greenArg, blueArg = None, None, None
    redDefault, greenDefault, blueDefault = 127, 127, 127
    self._red = self.maybe(redKwarg, redArg, redDefault)
    self._green = self.maybe(greenKwarg, greenArg, greenDefault)
    self._blue = self.maybe(blueKwarg, blueArg, blueDefault)
    self._alpha = self.maybe(alphaKwarg, alphaArg, 255)

  def encodeCore(self, ) -> str:
    """Encodes the color to a json string"""
    coreFields = getattr(self.__class__, '__core_fields__', {})
    out = {}
    for fieldName, field in coreFields.items():
      if isinstance(field, CoreField):
        value = field.encode(self)
        out |= {fieldName: value}
    return json.dumps(out)

  def encodeAuto(self) -> str:
    """Encodes the color to a json string"""
    autoFields = getattr(self.__class__, '__auto_fields__', {})
    out = {}
    for fieldName, field in autoFields.items():
      if isinstance(field, AutoField):
        value = field.encodeCore(self)
        out |= {fieldName: value}
    return json.dumps(out)

  @classmethod
  def decode(cls, encodedData: str) -> ColorSpec:
    """Decodes the json string to an instance of ColorSpec"""
    encodedData = json.loads(encodedData)
    obj = cls()
    coreFields = getattr(cls, '__core_fields__', {})
    for fieldName, data in encodedData.items():
      field = coreFields.get(fieldName, )
      field.decode(obj, data)
    return obj

  def hexify(self, uint8: int) -> str:
    """Returns a string representation of the value given in HEX code."""
    H = self.stringList('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F')
    if isinstance(uint8, int):
      return '%s%s' % (H[int(uint8 // 16)], H[int(uint8 % 16)])
    return 'LMAO'

  def __str__(self, ) -> str:
    """String representation."""
    red = self.hexify(self.red)
    green = self.hexify(self.green)
    blue = self.hexify(self.blue)
    alpha = self.hexify(self.alpha)
    if isinstance(self.alpha, int):
      if self.alpha < 255:
        return '#%s%s%s%s' % (red, green, blue, alpha)
      return '#%s%s%s' % (red, green, blue,)
    return 'YOLO!'

  def __repr__(self, ) -> str:
    """Code representation."""
    red = self.red
    green = self.green
    blue = self.blue
    alpha = self.alpha
    name = self.__class__.__qualname__
    return '%s(%d, %d, %d, %d)' % (name, red, green, blue, alpha)
