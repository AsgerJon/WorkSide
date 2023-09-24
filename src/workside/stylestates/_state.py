"""WorkSide - StyleStates - State
Symbolic class representation of states"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Optional

from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass


class State(WorkToyClass):
  """WorkSide - StyleStates - State
  Symbolic class representation of states"""

  __flag_primes__ = [2, 3, 5, 7, ]

  isEnabled = Attribute()
  isHovered = Attribute()
  isPressed = Attribute()
  isToggled = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    args = [*args, *[None for _ in range(4)]]
    enabledKwarg = self.searchKey('enabled', **kwargs)
    hoveredKwarg = self.searchKey('hovered', **kwargs)
    pressedKwarg = self.searchKey('pressed', **kwargs)
    toggledKwarg = self.searchKey('toggled', **kwargs)
    enabledArg, hoveredArg, pressedArg, toggledArg = args[:4]
    self.__is_enabled__ = self.maybe(enabledKwarg, enabledArg)
    self.__is_hovered__ = self.maybe(hoveredKwarg, hoveredArg)
    self.__is_pressed__ = self.maybe(pressedKwarg, pressedArg)
    self.__is_toggled__ = self.maybe(toggledKwarg, toggledArg)
    self.__iter_contents__ = None

  def _resetIterContents(self) -> None:
    self.__iter_contents__ = [
      (self.isEnabled, 2),
      (self.isHovered, 3),
      (self.isPressed, 5),
      (self.isToggled, 7),
    ]

  def _getIterContents(self) -> list:
    return self.__iter_contents__

  def __iter__(self) -> State:
    self._resetIterContents()
    return self

  def __next__(self) -> Optional[bool]:
    try:
      return self._getIterContents().pop(0)
    except IndexError:
      raise StopIteration

  def __hash__(self) -> int:
    out = 1
    for flag, value, ignore in zip(self, [2, 3, 5, 7], [11, 13, 17, 19]):
      if flag is None:
        out *= ignore
      elif flag:
        out *= value
    return out

  def __int__(self, ) -> int:
    return self.__hash__()

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, int):
      return False if int(self) - other else True
    if isinstance(other, State):
      for i, j in zip(self, other):
        if i is not None and j is not None:
          if i ^ j:
            return False
      return True
    return NotImplemented

  def __bool__(self) -> bool:
    for flag in self:
      if flag is not None:
        return True
    return False
