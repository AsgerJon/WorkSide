"""WorkSide - Settings - FontFamilies
Implementation of support for font families. """
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

import os
from typing import Any

from PySide6.QtGui import QFont
from icecream import ic

from worktoy.core import Bases
from worktoy.metaclass import AbstractMetaClass, AbstractNameSpace, \
  WorkToyMeta
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


def _getFontWeight(key: Any) -> QFont.Weight:
  """Lookup function for QFont Weight instances"""
  for item in QFont.Weight:
    if key in [item.name, item.value]:
      return item


def getNamedFontWeight(name: str) -> QFont.Weight:
  """Getter-function for the font weight named"""
  return _getFontWeight(name)


def getValuedFontWeight(value: int) -> QFont.Weight:
  """Getter-function for the font weight with the indicated value"""
  return WorkToyClass().maybe(_getFontWeight(value), QFont.Weight(value))


class FontFamilies(WorkToyClass, metaclass=WorkToyMeta):
  """Class providing available font families"""

  _families = None

  @classmethod
  def _loadFamilies(cls, ) -> None:
    """Loads the list of font families from the file."""
    here = os.path.dirname(__file__)
    fileName = 'font_families.txt'
    filePath = os.path.join(here, fileName, )
    with open(filePath, 'r', encoding='utf8') as f:
      cls._families = [i for i in f.read().split('\n') if i]

  @classmethod
  def getFontFamilies(cls, **kwargs) -> list[str]:
    """Getter-function for list of font families"""
    if cls._families is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = cls._loadFamilies
        varType = list
        varName = 'fontFamilies'
        raise RecursiveCreateGetError(creator, varType, varName)
      cls._loadFamilies()
      return cls.getFontFamilies(_recursion=True)
    return cls._families

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

  @classmethod
  def __cls_iter__(cls) -> type:
    setattr(cls, '__current_index__', 0)
    setattr(cls, '__iterable_contents__', [f for f in cls.getFontFamilies()])
    return cls

  @classmethod
  def __cls_next__(cls) -> Any:
    index = getattr(cls, '__current_index__')
    setattr(cls, '__current_index__', index + 1)
    iterContents = getattr(cls, '__iterable_contents__', )
    if index < len(iterContents):
      return iterContents[index]
    raise StopIteration

  @classmethod
  def __cls_len__(cls) -> int:
    return len(getattr(cls, '__iterable_contents__', []))

  def __iter__(self) -> Any:
    return self.__cls_iter__()

  def __next__(self, ) -> Any:
    return self.__cls_next__()

  def __cls_contains__(self, family: Any) -> bool:
    if isinstance(family, str):
      other = family.lower().replace(' ', '')
      for item in self:
        if item.lower().replace(' ', '') == other:
          return True
      return False
    if isinstance(family, QFont):
      return family.family() in FontFamilies

  def __cls_str__(self) -> str:
    """String representation of the class"""
    return 'FontFamilies - Provides a list of recognized font names'

  def __cls_repr__(self) -> str:
    """String representation of the class"""
    if getattr(self, '__qualname__', None) is not None:
      return '%s' % self.__qualname__
    return '%s' % self.__class__.__qualname__
