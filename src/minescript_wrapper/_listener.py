"""MinescriptWrapper - Listener
Class representation of chat listener callables."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Union, Optional

from mineside.minescript_wrapper import MetaListener
from mineside.worktoy.base import DefaultClass
from mineside.worktoy.core import Bases, Map, Function
from mineside.worktoy.fields import StrAttribute
from mineside.worktoy.metaclass import AbstractMetaClass


class Listener(MetaListener):
  """MinescriptWrapper - Listener
  Class representation of chat listener callables."""

  listenerIdentity = StrAttribute()

  def __init__(self, identity: str, *args, **kwargs) -> None:
    DefaultClass.__init__(self, *args, **kwargs)
    self.listenerIdentity = identity
    self._innerFunctions = []

  def invokeFunctions(self, chatMessage: str) -> None:
    """This method invokes the functions."""
    for func in self._innerFunctions:
      func(chatMessage)

  def appendFunction(self, func: Function) -> None:
    """Appends the callable to the list of inner functions. """
    self._innerFunctions.append(func)

  def __call__(self, arg: Union[str, Function, type]) -> Any:
    """If 'arg' is a str, it is understood as a chat message and is
    processed accordingly.

    If 'arg' is a function, it is understood as being a decorator
    application to an existing function.

    If 'arg' is a class, it should implement '__call__'. Instances of this
    class are then added to this listener instance. """

    if isinstance(arg, str):
      return self.invokeFunctions(arg)

    if isinstance(arg, Function):
      self.appendFunction(arg)
      return arg

    if isinstance(arg, type):
      raise NotImplementedError
