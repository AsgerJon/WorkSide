"""WorkSide - Widgets - Banner
Constant colored banner widgets"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Qt
from worktoy.descriptors import Field, Flag

from workside.draw import BackgroundStyleState, BackgroundStyle
from workside.widgets import CoreWidget


class Banner(CoreWidget):
  """WorkSide - Widgets - Banner
  Constant colored banner widgets"""

  #
  # drawBackground = Flag(True)
  # drawText = Flag(True)
  #
  # backgroundStyle = Field()

  def __init__(self, vertical: bool = None, horizontal: bool = None,
               *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)
    self.drawText = False
    if vertical:
      self.setFixedWidth(16)
    if horizontal:
      self.setFixedHeight(16)

  def __str__(self, ) -> str:
    """String representation"""
    return 'Banner'

  def __repr__(self) -> str:
    """Code representation"""
    return self.__class__.__qualname__

  def getAlignmentFlags(self) -> Qt.AlignmentFlag:
    """Getter-function for the alignment flags."""
    return Qt.AlignmentFlag.AlignCenter
  #
  # @backgroundStyle.getter
  # def getBackgroundStyle(self, ) -> BackgroundStyleState:
  #   """Getter-function for background style"""
  #   state = 'banner-hover' if self.hovered else 'banner'
  #   return BackgroundStyle.getStateStyle(state)
