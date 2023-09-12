"""MoreWorkToy - AutoField
Subclass of DataField"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from worktoy.core import Function
from worktoy.descriptors import DataField


class AutoField(DataField):
  """MoreWorkToy - AutoField
  Subclass of DataField"""

  def __init__(self, *args, **kwargs) -> None:
    DataField.__init__(self, *args, **kwargs)

  def __set_name__(self, owner: type, name: str) -> None:
    """Triggered when the owner class is created."""
    AutoField.__set_name__(self, owner, name)

  def getPrivateFieldName(self, ) -> str:
    """Getter-function for the private field name on the object. """
    return '_%s' % self.getFieldName()

  def getDeleterFunctionName(self) -> str:
    """Getter-function for the deleter function name"""
    name = self.getPrivateFieldName()
    Name = name[0].upper() + name[1:]
    return '_del%s' % Name

  def getGetterFunctionName(self, ) -> str:
    """Getter-function for the getter function name"""
    name = self.getPrivateFieldName()
    Name = name[0].upper() + name[1:]
    return '_get%s' % Name

  def getSetterFunctionName(self, ) -> str:
    """Getter-function for the setter function name."""
    name = self.getPrivateFieldName()
    Name = name[0].upper() + name[1:]
    return '_set%s' % Name

  def setFieldOwner(self, cls: type) -> None:
    """Setter-function for owner class."""
    AutoField.setFieldOwner(self, cls)

  def setterFactory(self, ) -> Function:
    """Setter-factory."""

    pvtName = self.getPrivateFieldName()

    def setterFunction(instance: Any, newValue: Any) -> None:
      """Setter-function for the AutoField."""
      setattr(instance, pvtName, newValue)
