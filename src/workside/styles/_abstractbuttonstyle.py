"""Specialised subclass of BaseStyle for use with abstract buttons. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QBrush, QColor
from icecream import ic
from worktoy.typetools import CallMeMaybe

from workside.settings import flag
from workside.styles import BaseStyle

ic.configureOutput(includeContext=True)


def adjustBrush(decorator: CallMeMaybe,
                state: CallMeMaybe) -> CallMeMaybe:
  """Decorator function for the brush getter function. This is the outer
  factory"""

  def factory(getBrush: CallMeMaybe) -> CallMeMaybe:
    """Inner factory creating the replacement getter function"""

    def func(self, ) -> QBrush:
      """Replacement function"""
      brush = getBrush(self)
      if getattr(self, state, None):
        return decorator(brush)
      return brush

    return func

  return factory


def stateFactory(state: str, ) -> CallMeMaybe:
  """State check function"""

  def func(baseStyle: BaseStyle) -> bool:
    """Checks if the base style is currently in the given state"""


def hoverBrush(brush: QBrush) -> QBrush:
  """Makes the brush lighter in color"""
  color = brush.color()
  r, g, b = [255 - c for c in [color.red(), color.green(), color.blue()]]
  r, g, b = [int(c * 0.85) for c in [r, g, b]]
  r, g, b = [255 - c for c in [r, g, b]]
  brush.setColor(QColor(r, g, b))
  return brush


@flag('hover')
@flag('pressed')
@flag('enabled')
@flag('activated')
@flag('moving')
class AbstractButtonStyle(BaseStyle):
  """Specialised subclass of BaseStyle for use with abstract buttons
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence. """

  def __init__(self, name: str, base: BaseStyle) -> None:
    data = base.getData()
    BaseStyle.__init__(self, name, data)

  def getBrush(self) -> QBrush:
    """Getter-function for QBrush"""
    brush = BaseStyle.getBrush()
    return brush
