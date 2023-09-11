"""WorkSide - Tools - AbstractTools
Baseclass for tools applied to styles"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod
from typing import Union, Any

from PySide6.QtGui import QPen, QBrush
from worktoy.worktoyclass import WorkToyClass

PaintTools = Union[tuple[QBrush, QPen]]


class AbstractTools(WorkToyClass):
  """WorkSide - Tools - AbstractTools
  Baseclass for tools applied to styles"""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

  @abstractmethod
  def toolSupport(self, tool: type) -> bool:
    """Defines if the subclass can be applied to the given tool."""

  @abstractmethod
  def applyTool(self, other: Any) -> Any:
    """For each supported tool, this method defines how the subclass
    applies to the given tool."""

  def __rshift__(self, other: Any) -> Any:
    """Applies this color to other"""
    if self.toolSupport(other):
      return self.applyTool(other)

  def __rlshift__(self, other: Any) -> Any:
    """Applies this color to other"""
    return self >> other
