"""WorkSide - Paint - FontFamily
Class representation of font family."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import os

from PySide6.QtGui import QFont
from worktoy.descriptors import Field
from worktoy.worktoyclass import WorkToyClass


class FontFamily(str, WorkToyClass):
  """WorkSide - Paint - FontFamily
  Class representation of font family."""

  __supported_families__ = None

  __default_family__ = 'Modern'

  defaultFamily = Field()

  @classmethod
  def _getDefaultFamily(cls) -> str:
    """Getter function for default family (class version)"""
    if cls.__default_family__ in cls.getFamilies():
      return cls.__default_family__

  @defaultFamily.GET
  def getDefaultFamily(self) -> str:
    """Getter function for default family (instance version)"""
    return self._getDefaultFamily()

  @classmethod
  def loadFamilies(cls) -> None:
    """Loads the list of supported families"""
    here = os.path.dirname(__file__)
    fileName = 'families.txt'
    filePath = os.path.join(here, fileName)
    with open(filePath, 'r') as f:
      families = f.read()
    cls.__supported_families__ = families.split('\n')

  @classmethod
  def getFamilies(cls, **kwargs) -> list[str]:
    """Getter-function for list of supported families"""
    if cls.__supported_families__ is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = cls.loadFamilies
        varType = list
        varName = '__supported_families__'
        raise RecursiveCreateGetError(creator, varType, varName)
      cls.loadFamilies()
      return cls.getFamilies(_recursion=True)
    return cls.__supported_families__

  def __new__(cls, family: str = None) -> str:
    """Creates the string subclass"""
    if family is None:
      family = cls._getDefaultFamily()
    if family in cls.getFamilies():
      instance = str.__new__(cls, family)
      return instance
    raise ValueError

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

  def __rshift__(self, other: QFont) -> QFont:
    """Changes family on other to self"""
    if isinstance(other, QFont):
      other.setFamily(self)
    return other

  def __rlshift__(self, other: QFont) -> QFont:
    """Invokes self >> other"""
    return self >> other

  def __str__(self) -> str:
    """String representation"""
    return self

  def __repr__(self, ) -> str:
    """Code representation"""
    return '%s(%s)' % (self.__class__.__qualname__, self)
