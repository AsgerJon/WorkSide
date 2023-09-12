"""WorkSide - Paint - FontCode
Dataclass for paint settings for labels."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Qt
from worktoy.descriptors import Field
from worktoy.worktoyclass import WorkToyClass


class FontCode(WorkToyClass):
  """WorkSide - Paint - FontCode
  Dataclass for paint settings for labels."""

  fontFamily = Field()
  fontSize = 16
  fontWeight = 400  # Normal: 400, Bold: 700
  fontColor = Field()
  backgroundColor = Field()
  borderColor = Field()
  borderWidth = 2
  cornerRadiusX = 4
  cornerRadiusY = 4
  verticalAlignment = Qt.AlignmentFlag.AlignVCenter
  horizontalAlignment = Qt.AlignmentFlag.AlignHCenter
