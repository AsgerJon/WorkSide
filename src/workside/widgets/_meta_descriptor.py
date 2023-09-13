"""WorkSide - Widgets - FontFamily
Enum class representation of common classes."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from icecream import ic
from worktoy.core import Bases
from worktoy.metaclass import AbstractMetaClass, AbstractNameSpace
from worktoy.worktoyclass import WorkToyClass


class MetaDescriptor(AbstractMetaClass, WorkToyClass):
  """Implementation of descriptors on the metaclass body"""

  @classmethod
  def __prepare__(mcls, name: str, bases: Bases,
                  **kwargs) -> AbstractNameSpace:
    return AbstractNameSpace()

  def __new__(mcls, name: str, bases: Bases, nameSpace: AbstractNameSpace,
              **kwargs) -> type:
    return AbstractMetaClass.__new__(mcls, name, bases, nameSpace, **kwargs)

  def __init__(cls, name: str, bases: Bases, nameSpace: AbstractNameSpace,
               **kwargs) -> None:
    AbstractMetaClass.__init__(cls, name, bases, nameSpace, **kwargs)
    cls._fieldName = None
    cls._fieldOwner = None

  def getFieldName(cls) -> str:
    """Getter-function for field name"""
    return cls._fieldName

  def setFieldName(cls, newValue: Any) -> None:
    """Setter-function for field name"""
    cls._fieldName = newValue

  def getFieldOwner(cls) -> type:
    """Setter-function for field owner"""
    return cls._fieldOwner

  def setFieldOwner(cls, fieldOwner: type) -> None:
    """Setter-function for field owner"""
    cls._fieldOwner = fieldOwner

  def __get__(cls, instance: Any, owner: type) -> Any:
    """Getter"""
    ic(instance)
    ic(type(instance))
    ic(owner)

  def __set__(cls, instance: Any, newValue: Any) -> Any:
    """Setter"""
    raise TypeError

  def __set_name__(cls, owner: type, name: str) -> None:
    cls.setFieldName(name)
    cls.setFieldOwner(owner)
