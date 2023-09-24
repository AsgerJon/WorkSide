"""WorkSide - Settings - Fonts
Names and settings relating to fonts"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QFont
from icecream import ic

ic.configureOutput(includeContext=True)
Thin = QFont.Weight.Thin
Normal = QFont.Weight.Normal
Bold = QFont.Weight.Bold
FontCase = QFont.Capitalization
MixCase = QFont.MixedCase
UpCase = QFont.AllUppercase
LowCase = QFont.AllLowercase
CapCase = QFont.Capitalize
Spacing = QFont.SpacingType.AbsoluteSpacing
AbsSpacing = Spacing.AbsoluteSpacing
PctSpacing = Spacing.PercentageSpacing


def getBaseFont(family: str = None,
                fontSize: int = None,
                fontWeight: QFont.Weight = Normal) -> QFont:
  """Getter-function for QFont"""
  font = QFont()
  font.setFamily(family)
  font.setPointSize(fontSize)
  font.setWeight(fontWeight)
  return font
