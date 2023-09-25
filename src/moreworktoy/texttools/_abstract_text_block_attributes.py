"""WorkSide - Tools - TextTools - AbstractTextBlockAttributes
Provides the AbstractTextBlock attributes."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from icecream import ic
from typing import Never

from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


class AbstractTextBlockAttributes(WorkToyClass):
  """ WorkSide - Tools - TextTools - TextBoxAttributes Provides the
AbstractTextBlock attributes. """

  def __init_subclass__(cls, **kwargs) -> None:
    return object.__init_subclass__()

  rawText = Attribute()

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  rawText  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @rawText.GET
  def getRawText(self, ) -> str:
    """Getter-function for rawText"""
    return self.__raw_text__

  @rawText.SET
  def setRawText(self, newValue: str) -> None:
    """Setter-function for rawText"""
    self.__raw_text__ = newValue

  @rawText.DEL
  def delRawText(self, *_) -> Never:
    """Illegal deleter-function for rawText"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'rawText'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self.__raw_text__ = 'Hello World!'
