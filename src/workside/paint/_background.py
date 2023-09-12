"""WorkSide - Paint - Background
Paints the background"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from icecream import ic
from worktoy.worktoyclass import WorkToyClass

from workside.moreworktoy import AutoField
from workside.paint import ColorSpec


class Background(WorkToyClass):
  """WorkSide - Paint - Background
  Paints the background"""

  fillColor = AutoField(ColorSpec.LIME())
  borderColor = AutoField(ColorSpec.YELLOW())

  ic(fillColor)
  ic(borderColor)

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
