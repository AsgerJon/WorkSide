"""WorkSide - Tools - AbstractTools
Baseclass for tools applied to styles"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from typing import Union, Any

from PySide6.QtGui import QPen, QBrush
from icecream import ic
from worktoy.worktoyclass import WorkToyClass

PaintTools = Union[tuple[QBrush, QPen]]

ic.configureOutput(includeContext=True)


class _USED:
  """Instances of this class indicate an argument already used."""

  def __init__(self, oldValue: Any) -> None:
    self._oldValue = oldValue


class AbstractTools(WorkToyClass):
  """WorkSide - Tools - AbstractTools
  Baseclass for tools applied to styles"""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self._args = {k: v for (k, v) in enumerate(args)}
    self._kwargs = kwargs

  def useArgs(self, *args) -> None:
    """Indicate that the items at the indices are now used."""
    for arg in args:
      self.useArg(arg[0])

  def useArg(self, index: Union[int, str]) -> None:
    """Indicate that item at index has been used"""
    if isinstance(index, int) and index < len(self._args):
      old = _USED(self._args[index])
      self._args[index] = old
    if isinstance(index, str) and index in self._kwargs.keys():
      old = _USED(self._kwargs[index])
      self._kwargs[index] = old

  def getPosArgs(self) -> dict:
    """Getter-function for positional arguments."""
    out = {}
    for key, val in self._args.items():
      if not isinstance(val, _USED):
        out |= {key: val}
    return out

  def getKeywordArgs(self) -> dict:
    """Getter-function for keyword arguments."""
    out = {}
    for key, val in self._kwargs.items():
      if not isinstance(val, _USED):
        out |= {key: val}
    return out

  def __rshift__(self, other: Any) -> Any:
    """Applies this color to other"""
    if self.toolSupport(other):
      return self.applyTool(other)

  def __rlshift__(self, other: Any) -> Any:
    """Applies this color to other"""
    return self >> other

  @abstractmethod
  def toolSupport(self, tool: type) -> bool:
    """Defines if the subclass can be applied to the given tool."""

  @abstractmethod
  def applyTool(self, other: Any) -> Any:
    """For each supported tool, this method defines how the subclass
    applies to the given tool."""

  @classmethod
  @abstractmethod
  def saveToJson(cls, instance: Any = None) -> str:
    """This method creates a json representation of the current instance
    that the subclass can use to recreate it."""

  @classmethod
  @abstractmethod
  def loadFromJson(cls, data: str) -> Any:
    """This method creates an instance from the json data."""
