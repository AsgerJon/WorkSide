"""WorkSide - Paint - ColorSpec
Dataclass specification for colors"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json

from icecream import ic
from worktoy.worktoyclass import WorkToyClass

from workside.moreworktoy import DataField, DataClass

ic.configureOutput(includeContext=True)


@DataClass()
class ColorSpec(WorkToyClass):
  """WorkSide - Paint - ColorSpec
  Dataclass specification for colors"""
  red = DataField()
  green = DataField()
  blue = DataField()
  alpha = DataField()

  @red.GET
  def getRed(self, ) -> int:
    """Getter-function for red"""
    return self._red

  @red.SET
  def setRed(self, newValue: int) -> None:
    """Getter-function for red"""
    self._red = newValue

  @red.ENCODER
  def encoderRed(self, ) -> str:
    """Encoder-function for red"""
    return json.dumps(self.red)

  @red.DECODER
  def decoderRed(self, data: str) -> int:
    """Decoder-function for red"""
    value = json.loads(data).get('red', '0')
    if isinstance(value, str):
      return int(value)

  @green.GET
  def getGreen(self, ) -> int:
    """Getter-function for green"""
    return self._green

  @green.SET
  def setGreen(self, newValue: int) -> None:
    """Getter-function for green"""
    self._green = newValue

  @green.ENCODER
  def encoderGreen(self, ) -> str:
    """Encoder-function for green"""
    return json.dumps(self.green)

  @green.DECODER
  def decoderGreen(self, data: str) -> int:
    """Decoder-function for green"""
    value = json.loads(data).get('green', '0')
    if isinstance(value, str):
      return int(value)

  @blue.GET
  def getBlue(self, ) -> int:
    """Getter-function for blue"""
    return self._blue

  @blue.SET
  def setBlue(self, newValue: int) -> None:
    """Getter-function for blue"""
    self._blue = newValue

  @blue.ENCODER
  def encoderGreen(self, ) -> str:
    """Encoder-function for blue"""
    return json.dumps(self.blue)

  @blue.DECODER
  def decoderBlue(self, data: str) -> int:
    """Decoder-function for blue"""
    value = json.loads(data).get('blue', '0')
    if isinstance(value, str):
      return int(value)

  @alpha.GET
  def getAlpha(self, ) -> int:
    """Getter-function for alpha"""
    return self._alpha

  @alpha.SET
  def setAlpha(self, newValue: int) -> None:
    """Getter-function for alpha"""
    self._alpha = newValue

  @alpha.ENCODER
  def encoderAlpha(self, ) -> str:
    """Encoder-function for alpha"""
    return json.dumps(self.alpha)

  @alpha.DECODER
  def decoderAlpha(self, data: str) -> int:
    """Decoder-function for alpha"""
    value = json.loads(data).get('alpha', '0')
    if isinstance(value, str):
      return int(value)

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

  def encode(self, ) -> str:
    """Encodes the color to a json string"""
    return json.dumps(dict(red=self.red, green=self.green, blue=self.blue,
                           alpha=self.alpha))

  @classmethod
  def decode(cls, data: str) -> ColorSpec:
    """Decodes the json string to an instance of ColorSpec"""
    return cls(json.loads(data))

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
