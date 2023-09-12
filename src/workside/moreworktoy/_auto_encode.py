"""MoreWorkToy - AutoEncode
Instance method decorator allowing a custom class to inform the auto class
system how it should be encoded."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from icecream import ic
from worktoy.core import Function
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


class AutoEncode(WorkToyClass):
  """MoreWorkToy - AutoEncode
  Instance method decorator allowing a custom class to inform the auto class
  system how it should be encoded."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self._innerFunction = None
    self._innerInstance = None
    self._innerClass = None
    self._fieldName = None
    self._fieldOwner = None

  def __call__(self, *args, **kwargs) -> Function:
    """First call sets the inner function. Subsequent calls invokes the
    function."""
    self.setInnerFunction(args[0])
    args[0].__set_name__ = self.__set_name__
    return args[0]

  def __set_name__(self, cls: type, name: str) -> None:
    self.setFieldName(name)
    self.setFieldOwner(cls)

  def getInnerFunction(self) -> Function:
    """Getter-function for the inner function"""
    return self._innerFunction

  def setInnerFunction(self, innerFunction: Function) -> None:
    """Setter-function for the inner function"""
    self._innerFunction = innerFunction

  def getInnerInstance(self) -> Any:
    """Getter-function for the inner instance"""
    return self._innerInstance

  def setInnerInstance(self, innerInstance: Any) -> None:
    """Setter-function for the inner instance"""
    ic(innerInstance)
    self._innerInstance = innerInstance

  def getInnerClass(self) -> type:
    """Getter-function for the inner class"""
    return self._innerClass

  def setInnerClass(self, innerClass: type) -> None:
    """Setter-function for the inner class"""
    ic(innerClass)
    self._innerClass = innerClass

  def getFieldName(self) -> str:
    """Getter-function for field name"""
    return self._fieldName

  def setFieldName(self, fieldName: str) -> None:
    """Setter-function for the field name"""
    ic(fieldName)
    self._fieldName = fieldName

  def getFieldOwner(self) -> type:
    """Getter-function for the field owner"""
    return self._fieldOwner

  def setFieldOwner(self, fieldOwner: type) -> None:
    """Setter-function for the field owner"""
    ic(fieldOwner)
    self._fieldOwner = fieldOwner
