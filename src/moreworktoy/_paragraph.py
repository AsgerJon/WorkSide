"""WorkSide - Tools - TextTools - Paragraph
The paragraph class represents justified text."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from worktoy.texttools import ParagraphAttributes, maxLineLen


class Paragraph(ParagraphAttributes):
  """WorkSide - Tools - TextTools - Paragraph
  The paragraph class represents justified text."""

  def __init__(self, text: str = None, *args, **kwargs) -> None:
    ParagraphAttributes.__init__(self, *args, **kwargs)
    self._rawText = self.monoSpace(text)

  def wrapLine(self, line: str) -> str:
    """Wraps the given line in left and right margins"""
    return '%s%s%s' % (self.leftMargin, line, self.rightMargin)

  def __len__(self) -> int:
    return maxLineLen - self.rightMargin - self.leftMargin

  def __str__(self, ) -> str:
    lines = self.wordWrap(self._rawText, len(self))
    return '\n'.join([self.wrapLine(line) for line in lines])
