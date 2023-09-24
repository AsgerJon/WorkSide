"""WorkSide - Styles - StyleState
Suggested default implementation"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from workside.stylestates import AbstractStyleState, State
from worktoy.core import Items, Keys, Values
from worktoy.descriptors import Attribute


class StyleState(AbstractStyleState):
  """WorkSide - Styles - StyleState
  Suggested default implementation"""

  isDisabled = Attribute()
  isDisabledHover = Attribute()
  isHovered = Attribute()
  isPressed = Attribute()
  isToggled = Attribute()
  isHoverToggled = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    AbstractStyleState.__init__(self, *args, **kwargs)
    self._iterContents = None
    self.__is_disabled__ = State(isEnabled=False, isHovered=False)
    self.__is_disabled_hovered__ = State(isEnabled=False, isHovered=True)
    self.__is_hovered__ = State(isEnabled=True, isHovered=True)
    self.__is_pressed__ = State(isEnabled=True, isPressed=True)
    self.__is_toggled__ = State(isEnabled=True, isToggled=True, )
    self.__is_hovered_toggled__ = State(isEnabled=True,
                                        isToggled=True,
                                        isHovered=True)

  def _resetIterContents(self) -> None:
    self._iterContents = [k for k in self.keys()]

  def _getIterContents(self, ) -> list:
    return self._iterContents

  def __iter__(self) -> StyleState:
    self._resetIterContents()
    return self

  def __next__(self) -> str:
    try:
      return self._getIterContents().pop(0)
    except IndexError:
      raise StopIteration

  def getFlags(self) -> list:
    """Getter-function for flags"""
    return self.stringList(
      """disabled, disabledHover, hovered, pressed, toggled, hoverToggled""")

  def getStates(self) -> list:
    """Getter-function for expected states. States not appearing in this
    list are considered undefined."""
    return [self.isDisabled,
            self.isDisabledHover,
            self.isHovered,
            self.isPressed,
            self.isToggled,
            self.isHoverToggled,
            ]

  def _asDict(self) -> dict[str, State]:
    return {k: v for k, v in zip(self.getFlags(), self.getStates())}

  def items(self) -> Items:
    """Implementation of 'dict.items'"""
    return self._asDict().items()

  def keys(self) -> Keys:
    """Implementation of 'dict.keys'"""
    return self._asDict().keys()

  def values(self) -> Values:
    """Implementation of 'dict.values'"""
    return self._asDict().values()
