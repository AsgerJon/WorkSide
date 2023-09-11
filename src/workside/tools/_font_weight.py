"""WorkSide - Tools - FontWeight
Class representation of font weight."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Any, Optional

from PySide6.QtGui import QFont
from worktoy.descriptors import Field

from workside.tools import AbstractTools


class FontWeight(AbstractTools):
  """WorkSide - Tools - FontWeight
  Class representation of font weight."""

  @staticmethod
  def weightFromValue(value: int) -> Optional[QFont.Weight]:
    """Get weight from value"""
    if value % 100 or value > 900 or value < 100:
      return
    for item in QFont.Weight:
      if item.value == value:
        return item

  @staticmethod
  def weightFromName(name: str) -> Optional[QFont.Weight]:
    """Get weight from name"""
    for item in QFont.Weight:
      if item.name == name:
        return item

  __default_value__ = 16

  @classmethod
  def getDefaultValue(cls) -> int:
    """Getter-function for the default value"""
    return cls.__default_value__

  weight = Field()
  defaultValue = Field()
  weightKeys = Field()

  @defaultValue.GET
  def _getDefaultValue(self) -> int:
    """Instance getter function for default value."""
    return self.__default_value__

  @weightKeys.GET
  def getWeightKeys(self) -> list[str]:
    """Getter-function for keys pointing to the weights"""
    return self.stringList("""weight, fontWeight, boldness, bold""")

  @weight.GET
  def getWeight(self) -> QFont.Weight:
    """Getter-function for the font weight."""

  def _parseKwargs(self) -> Optional[QFont.Weight]:
    """Parses keyword arguments"""
    for name in self.weightKeys:
      for key, val in self.getKeywordArgs().items():
        if name == key:
          if isinstance(val, QFont.Weight):
            self.useArg(key)
            return val
          if isinstance(val, bool):
            self.useArg(key)
            return QFont.Weight.Bold if val else QFont.Weight.Normal
          if isinstance(val, int):
            weight = self.weightFromValue(val)
            if isinstance(weight, QFont.Weight):
              self.useArg(key)
              return weight
          if isinstance(val, str):
            weight = self.weightFromName(val)
            if isinstance(weight, QFont.Weight):
              self.useArg(key)
              return weight

  def _parseArgs(self) -> Optional[QFont.Weight]:
    """Parses positional arguments"""
    for key, val in self.getPosArgs().items():
      if isinstance(val, QFont.Weight):
        self.useArg(key)
        return val
      if isinstance(val, bool):
        self.useArg(key)
        return QFont.Weight.Bold if val else QFont.Weight.Normal
      if isinstance(val, int):
        weight = self.weightFromValue(val)
        if isinstance(weight, QFont.Weight):
          self.useArg(key)
          return weight
      if isinstance(val, str):
        weight = self.weightFromName(val)
        if isinstance(weight, QFont.Weight):
          self.useArg(key)
          return weight

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    w = None
    parsers = [self._parseKwargs, self._parseArgs]
    for parser in parsers:
      if w is None:
        w = parser()
    self._innerValue = self.maybe(w, self.defaultValue)

  def toolSupport(self, tool: type) -> bool:
    """Supports the original QPen and the WorkPen"""
    return True if tool in [QFont] else False

  def applyTool(self, other: Any) -> Any:
    """Applies inner value as the width of the QPen."""
    if isinstance(other, QFont):
      other.setWeight(self.weight)
    return other

  @classmethod
  def saveToJson(cls, instance: Any = None) -> str:
    """Implementation"""
    return json.dumps(dict(fontSize=instance.weight))

  @classmethod
  def loadFromJson(cls, data: str) -> FontWeight:
    """Implementation"""
    return FontWeight(**json.loads(data))
