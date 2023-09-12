"""Testing"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json

from worktoy.worktoyclass import WorkToyClass

from workside.moreworktoy import AutoEncode, AutoClass, AutoField


@AutoClass()
class RGB(WorkToyClass):
  """COLOR"""

  red = AutoField(0)
  green = AutoField(0)
  blue = AutoField(0)
  alpha = AutoField(255)

  def hexify(self, uint8: int) -> str:
    """Returns a string representation of the value given in HEX code."""
    H = self.stringList('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F')
    return '%s%s' % (H[int(uint8 // 16)], H[int(uint8 % 16)])

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

  def getNew(self, *args, **kwargs) -> RGB:
    """Creates a new instance"""
    return self.__class__(*args, **kwargs)

  def decode(self, encodedData: str) -> RGB:
    """Tries to decode encoded data"""
    return self.getNew(**json.loads(encodedData))

  @AutoEncode()
  def encode(self, ) -> str:
    """Tries to encode self"""
    encodedData = dict(red=self.red, green=self.green, blue=self.blue,
                       alpha=self.alpha)
    return json.dumps(encodedData)


@AutoClass()
class Canvas(WorkToyClass):
  """LMAO"""

  fillColor = AutoField(RGB(255, 191, 127, 255))
  borderColor = AutoField(RGB(191, 127, 31, 255))
  fontColor = AutoField(RGB(0, 0, 0, 255))

  def __str__(self) -> str:
    fillText = '%16s: %s' % ('Fill color', self.fillColor)
    borderText = '%16s: %s' % ('Border color', self.borderColor)
    fontText = '%16s: %s' % ('Font color', self.fontColor)
    return '\n--> '.join(['', fillText, borderText, fontText])
