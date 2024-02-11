"""MinescriptWrapper - MetaListener
Metaclass for chat listeners."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen

from __future__ import annotations

from typing import Any, Union, Optional

from mineside.worktoy.base import DefaultClass
from mineside.worktoy.core import Bases, Map, Function
from mineside.worktoy.fields import StrAttribute
from mineside.worktoy.metaclass import AbstractMetaClass


class _MetaListener(AbstractMetaClass):
  """Metaclass for chat listeners."""

  @classmethod
  def __prepare__(mcls, name: str, bases: Bases, **kwargs) -> Map:
    """Implementation of prepare method."""
    return {}

  def __new__(mcls, name: str, bases: Bases, nameSpace: Map,
              **kwargs) -> Map:
    """Implementation of the class creation."""
    cls = AbstractMetaClass.__new__(
      mcls, name, bases, nameSpace, **kwargs)
    return cls

  def __init__(cls, name: str, bases: Bases, nameSpace: Map,
               **kwargs) -> None:
    """Implementation of the class initialization."""
    type.__init__(cls, name, bases, nameSpace, **kwargs)
    setattr(cls, '__listener_instances__', {})

  def __call__(cls, listenerIdentity: str, *args, **kwargs) -> Any:
    """Implementation of instance creation ensuring that an existing
    instance is returned when the same identity is created."""
    instanceDictionary = getattr(cls, '__listener_instances__')
    self = instanceDictionary.get(listenerIdentity, None)
    if self is None:
      self = AbstractMetaClass.__call__(
        cls, listenerIdentity, *args, **kwargs)
      instanceDictionary |= {listenerIdentity: self}
      setattr(cls, '__listener_instances__', instanceDictionary)
    return self


class MetaListener(DefaultClass, metaclass=_MetaListener):
  """In between class exposing the metaclass."""
  pass
