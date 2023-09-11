"""WorkSide - Tools - FontSize
Class representation of font size"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Optional, Any

from PySide6.QtGui import QFont
from worktoy.descriptors import Field

from workside.tools import AbstractTools


class FontSize(AbstractTools):
  """WorkSide - Tools - FontSize
  Class representation of font size"""

  __default_value__ = 16

  @classmethod
  def getDefaultValue(cls) -> int:
    """Getter-function for the default value"""
    return cls.__default_value__

  fontSizeKeys = Field()
  fontSize = Field()
  defaultValue = Field()

  @fontSizeKeys.GET
  def getFontSizeKeys(self) -> list[str]:
    """Getter-function for the list of font size keys"""
    return self.stringList("""size, pointSize, fontSize, ptSize, 
      pixelSize""")

  @fontSize.GET
  def getFontSize(self) -> int:
    """Getter-function for the font size"""
    return self._fontSize

  @defaultValue.GET
  def _getDefaultValue(self) -> int:
    """Instance getter function for default value."""
    return self.__default_value__

  def _parseKwargs(self) -> Optional[int]:
    """Parses keyword arguments"""
    for name in self.fontSizeKeys:
      for key, val in self.getKeywordArgs().items():
        if name == key and isinstance(val, int):
          self.useArg(key)
          return val

  def _parseArgs(self, ) -> Optional[int]:
    """Parses positional arguments"""
    for key, val in self.getPosArgs().items():
      if isinstance(val, int):
        self.useArg(key)
        return val

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    parsers = [self._parseKwargs, self._parseArgs]
    val = None
    for parser in parsers:
      if val is None:
        val = parser()
    self._fontSize = self.maybe(val, self.defaultValue)

  def toolSupport(self, tool: type) -> bool:
    """Supports the original QPen and the WorkPen"""
    return True if tool in [QFont] else False

  def applyTool(self, other: Any) -> Any:
    """Applies inner value as the width of the QPen."""
    if isinstance(other, QFont):
      other.setPointSize(self.fontSize)
    return other

  @classmethod
  def saveToJson(cls, instance: FontSize = None) -> str:
    """Implementation"""
    return json.dumps(dict(fontSize=instance.fontSize))

  @classmethod
  def loadFromJson(cls, data: str) -> FontSize:
    """Implementation"""
    return FontSize(**json.loads(data))
