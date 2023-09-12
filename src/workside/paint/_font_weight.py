"""WorkSide - Paint - FontWeight
Class representation of FontWeight"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Union, Any

from PySide6.QtGui import QFont
from worktoy.descriptors import Field
from worktoy.worktoyclass import WorkToyClass


class FontWeight(WorkToyClass):
  """WorkSide - Paint - FontWeight
  Class representation of FontWeight"""

  __default_weight__ = QFont.Weight.Normal
  defaultWeight = Field()
  weight = Field()

  @classmethod
  def _getDefaultWeight(cls) -> QFont.Weight:
    """Getter-function for default weight (class version)."""
    return cls.__default_weight__

  @defaultWeight.GET
  def getDefaultWeight(self) -> QFont.Weight:
    """Getter-function for default weight (instance version)."""
    return self._getDefaultWeight()

  @weight.GET
  def getWeight(self) -> QFont.Weight:
    """Getter-function for weight"""
    return self._weight

  @weight.SET
  def setWeight(self, weight: Any) -> None:
    """Setter-function for weight"""
    if isinstance(weight, QFont.Weight):
      self._weight = weight
      return
    elif isinstance(weight, (str, int)):
      return self.setWeight(self.identifyWeight(weight))
    elif isinstance(weight, FontWeight):
      return self.setWeight(weight.weight)

  def identifyWeight(self, weight: Union[int, str]) -> QFont.Weight:
    """Identifies the weight associated with the weight argument,
    which may be of 'str', 'int' or 'QFont.Weight' type."""
    for item in QFont.Weight:
      if weight in [item.name, item.value, item.name.lower()]:
        return item
    return self.defaultWeight

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self._weight = None
    strArgs = self.maybeTypes(str, *args)
    for arg in strArgs:
      if self._weight is None:
        self._weight = self.identifyWeight(arg)
    if self._weight is None:
      intArgs = self.maybeTypes(int, *args)
      for arg in intArgs:
        if self._weight is None:
          self._weight = self.identifyWeight(arg)
    self._weight = self.maybe(self._weight, self.defaultWeight)
