"""WorkSide - Styles - FontStyle
Styles defining text box styles"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtGui import QFont
from worktoy.descriptors import DataField
from worktoy.worktoyclass import WorkToyClass

from workside.styles import ColorField


class FontStyle(WorkToyClass):
  """WorkSide - Styles - FontStyle
  Styles defining text box styles"""

  fillColor = ColorField.GREY()
  borderColor = ColorField.BLACK()
  fontColor = ColorField.BLACK()

  fontFamily = DataField('Modern')
  fontWeight = QFont.Weight.Normal

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
