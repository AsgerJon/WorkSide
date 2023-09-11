"""WorkSide - Tools - FontFamily
Symbolic class representation of font families."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
import os
from typing import Any, Optional

from PySide6.QtGui import QFont
from icecream import ic
from worktoy.descriptors import Field

from workside.tools import AbstractTools

ic.configureOutput(includeContext=True)


class FontFamily(AbstractTools):
  """WorkToy - SYM - FontFamily
  Symbolic class representing text families for use by QFont."""

  __font_names__ = None

  name = Field()

  familyKeys = Field()

  @classmethod
  def _loadFontNames(cls) -> None:
    """Loads the supported font names from the file"""
    here = os.path.dirname(__file__)
    fileName = 'families.txt'
    filePath = os.path.join(here, fileName)
    with open(filePath, 'r') as f:
      data = f.read()
    if isinstance(data, str):
      cls.__font_names__ = data.split('\n')

  @classmethod
  def getFontNames(cls, **kwargs) -> list[str]:
    """Getter-function for font names"""
    if cls.__font_names__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = cls._loadFontNames
        varType = list
        varName = '__font_names__'
        raise RecursiveCreateGetError(creator, varType, varName)
      cls._loadFontNames()
      return cls.getFontNames(_recursion=True)
    return cls.__font_names__

  @name.GET
  def getName(self) -> str:
    """Getter-function for the name of the underlying font family"""
    return self._familyName

  @familyKeys.GET
  def getFamilyKeys(self) -> list[str]:
    """Getter-function for list of names."""
    return self.stringList("""fontFamily, family, Family""")

  def _parseKwargs(self) -> Optional[str]:
    """Parses keyword arguments"""
    familyNames = self.getFontNames()
    for name in self.familyKeys:
      for key, val in self.getKeywordArgs().items():
        if key == name and isinstance(val, str):
          if val in familyNames:
            self.useArg(key)
            return val

  def _parseArgs(self) -> Optional[str]:
    """Parses positional arguments"""
    familyNames = self.getFontNames()
    for key, val in self.getPosArgs():
      if isinstance(val, str) and val in familyNames:
        self.useArg(key)
        return val

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    _defaultName = 'Modern No. 20'
    familyName = None
    parsers = [self._parseKwargs, self._parseArgs]
    for parser in parsers:
      if familyName is None:
        familyName = parser()
    self._familyName = self.maybe(familyName, _defaultName)

  def toolSupport(self, tool: type) -> bool:
    """Supports QFont"""
    return True if tool is QFont else False

  def applyTool(self, other: Any) -> Any:
    """Applies to QFont"""
    if isinstance(other, QFont, ):
      other.setFamily(self.name)
    return other

  @classmethod
  def saveToJson(cls, instance: FontFamily = None) -> str:
    """Implementation"""
    return json.dumps(dict(family=instance.name))

  @classmethod
  def loadFromJson(cls, data: str) -> FontFamily:
    """Implementation"""
    return FontFamily(**json.loads(data))
