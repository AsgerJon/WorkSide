"""WorkSide - Paint - Color
Class representation of colors"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.worktoyclass import WorkToyClass

from workside.moreworktoy import CoreField


class ColorField(WorkToyClass):
  """WorkSide - Paint - Color
  Class representation of colors"""

  red = CoreField(0)
  green = CoreField(0)
  blue = CoreField(0)
  alpha = CoreField(0)
