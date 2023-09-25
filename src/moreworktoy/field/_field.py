"""WorkToy - Descriptors - Attribute
Basic descriptor implementation providing explicit creator functions."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from worktoy.core import Function
from worktoy.descriptors import Attribute


class Field(Attribute):
  """WorkToy - Descriptors - Attribute
  Basic descriptor implementation providing explicit creator functions."""

  def __init__(self, *args, **kwargs) -> None:
    Attribute.__init__(self, *args, **kwargs)
    self._creatorFunctionName = None
    self.__explicit_creator__ = None

  def _getCreatorName(self) -> str:
    """Getter-function for the creator function."""
    if self._creatorFunctionName is None:
      return '_create%s' % self._getCapName()
    return self._creatorFunctionName

  def CREATE(self, creatorFunction: Function) -> Function:
    """Sets explicit creator function"""
    self._creatorFunctionName = creatorFunction.__name__
    return creatorFunction

  def __set_name__(self, cls: type, name: str) -> None:
    return Attribute.__set_name__(self, cls, name)

  def __get__(self, obj: Any, cls: type) -> Any:
    expGetter = getattr(obj, self._getGetterName(), None)
    if isinstance(expGetter, Function):
      return expGetter(obj, cls)  # Case 1a
    expGetter = getattr(obj, self._getGetterName(), None)
    if isinstance(expGetter, Function):
      return expGetter(obj, cls)  # Case 1b
    #   Case 1: The field does not refer to a private underlying variable,
    #   but instead exposes a function value of the current state, such as
    #   the area of a rectangle. The function must be decorated with 'GET'
    #   and the return value from it is returned as the 'value' of the
    #   field. (Please note that the simpler 'Attribute' class is fully
    #   capable of handling this use case. This subclass implements
    #   unnecessary features that may complicate debugging needlessly.)
    #   Case 2: The field refers to a private underlying variable whose
    #   value is defined at instance creation time. (This use case is fully
    #   implemented in the simpler 'Attribute' class).
    value = getattr(obj, self._getPrivateFieldName(), None)
    if value is not None:
      return value  # Case 2
    #   RECOMMENDED USE-CASE:
    #   Case 3: The field refers to a private underlying variable whose
    #   instantiation is deferred. This is the primary use case for this
    #   subclass. It requires a method decorated with 'CREATE' to create
    #   the instance when the getter is invoked.
    creator = self._getCreator(obj, cls)
    value = creator(obj, cls)  # Case 3a
    #     3a.  Return the instance value from the creator method and allow
    #     the Field instance to handle it. (RECOMMENDED)
    #     3b.  Implement the creator method to explicitly populate the
    #     private variable with the created value. (NOT RECOMMENDED)
    if value is None:
      value = getattr(obj, self._getPrivateFieldName(), None)
      if value is None:  # Requires error handling:
        from worktoy.waitaminute import RecursiveCreateGetError
        argType = self._getDefaultType()
        argName = self._getFieldName()
        raise RecursiveCreateGetError(creator, argType, argName)
      return value  # Case 3b
    return value  # Case 3a

  def _getCreator(self, obj: Any, cls: type) -> Function:
    """Getter-function for deferred creator. This getter returns the
    method decorated with 'CREATE'. If not such function is decorated,
    invoking this method getter method will raise
    'MissingArgumentException'. """
    if self.__explicit_creator__ is None:
      from worktoy.waitaminute import UnexpectedStateError
      raise UnexpectedStateError('__explicit_creator__')
    if isinstance(self.__explicit_creator__, Function):
      return self.__explicit_creator__(obj, cls)  # No error
    from worktoy.waitaminute import TypeSupportError
    expType = Function
    actualValue = self.__explicit_creator__
    argName = '__explicit_creator__'
    raise TypeSupportError(expType, actualValue, argName)
