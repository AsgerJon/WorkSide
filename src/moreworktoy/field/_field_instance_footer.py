"""WorkSide - Field - FieldInstanceFooter
Code formatted footer"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.settings import AlignCenter
from worktoy.texttools import TextBox, Paragraph

from moreworktoy.texttools import maxLineLen


class FieldInstanceFooter(Paragraph):
  """Code formatted footer"""

  def __init__(self, *args, **kwargs) -> None:
    Paragraph.__init__(self, *args, **kwargs)
    self.leftMargin = '  # /'
    self.rightMargin = '\\ #  '
    self.leftBorder = ''
    self.rightBorder = ''
    self.leftPadding = ''
    self.rightPadding = ''
    self.alignment = AlignCenter

  def __str__(self) -> str:
    n = maxLineLen - len(self.leftMargin + self.rightMargin)
    border = n * '¨'
    return '%s%s%s' % (self.leftMargin, border, self.rightMargin)
