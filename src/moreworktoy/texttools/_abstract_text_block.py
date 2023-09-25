"""WorkSide - Tools - TextTools - AbstractTextBlock
Baseclass for the different text carrying classes."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from icecream import ic

from moreworktoy.texttools import AbstractTextBlockAttributes
from worktoy.descriptors import Attribute
from worktoy.worktoyclass import WorkToyClass

ic.configureOutput(includeContext=True)


class AbstractTextBlock(AbstractTextBlockAttributes):
  """WorkSide - Tools - TextTools - AbstractTextBlock
  Baseclass for the different text carrying classes."""

  def __init_subclass__(cls, **kwargs) -> None:
    return object.__init_subclass__()

  @staticmethod
  def charLengthList(words: list[str]) -> int:
    """Length of the words in the list including spaces"""
    out = -1
    for word in words:
      out += (1 + len(word))
    return out

  @staticmethod
  def wordWrap(text: str, lineLen: int) -> list[str]:
    """Wraps the text at spaces and lists the words in lines not exceeding
    the indicated length."""
    words = text.split(' ')
    line = []
    lines = []
    for word in words:
      if AbstractTextBlock.charLengthList(line + [word, ]) > lineLen:
        lines.append(' '.join(line))
        line = []
      line.append(word)
    if line:
      lines.append(' '.join(line))
    return lines

  @staticmethod
  def centerText(text: str, width: int, fill: str = None) -> list[str]:
    """Centers and wraps the text. By default, the fill is whitespace"""
    lines = AbstractTextBlock.wordWrap(text, width)
    fill = WorkToyClass().maybe(fill, ' ')
    return [str.center(line, width, fill) for line in lines]

  rawText = Attribute()
