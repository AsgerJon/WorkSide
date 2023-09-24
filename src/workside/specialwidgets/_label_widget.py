"""WorkToy - Core - LabelWidget
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from workside.widgets import TextWidget
from worktoy.descriptors import Attribute
from worktoy.settings import AlignFlag, AlignCenter
from worktoy.texttools import Paragraph


class LabelWidget(TextWidget):
  """Subclass of TextWidget with character restrictions limited to one
  line."""

  paragraph = Attribute()
  alignment = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    lineLenKeys = self.stringList("""charLimit, charLim, chars""")
    lineLenKwarg = self.searchKey(*lineLenKeys, **kwargs)
    lineLenArg = self.maybeType(int, *args)
    lineLenDefault = 40
    alignKeys = self.stringList("""alignment, align, horizontalAlign""")
    alignKwarg = self.searchKey(*alignKeys, **kwargs)
    alignArg = self.maybeType(AlignFlag, *args)
    alignDefault = AlignCenter
    textKeys = self.stringList("""'text, label, currentText""")
    textKwarg = self.searchKey(*textKeys, **kwargs)
    textArg = self.maybeType(str, *args)
    textDefault = 'lmao'
    p = Paragraph()
    p.leftMargin = ''
    p.leftBorder = ''
    p.leftPadding = ''
    p.rightMargin = ''
    p.rightBorder = ''
    p.rightPadding = ''
    self.paragraph = p
    TextWidget.__init__(self, *args, **kwargs)
    self.lineLength = self.maybe(lineLenKwarg, lineLenArg, lineLenDefault)
    self.alignment = self.maybe(alignKwarg, alignArg, alignDefault)
    self.currentText = self.maybe(textKwarg, textArg, textDefault)

  def getCurrentText(self) -> str:
    """Getter-function for currentText"""
    return str(self.paragraph)

  def setCurrentText(self, text: str) -> None:
    """Setter-function for currentText"""
    self.paragraph.currentText = text

  def getLineLength(self, ) -> int:
    """Getter-function for line length"""
    return self.paragraph.lineLen

  def setLineLength(self, _lineLen: int) -> None:
    """Setter-function for line length"""
    self.paragraph.lineLen = _lineLen

  def getAlignment(self, ) -> AlignFlag:
    """Getter-function for alignment"""
    return self.paragraph.alignment

  def setAlignment(self, *_align: AlignFlag) -> None:
    """Setter-function for alignment"""
    self.paragraph.alignment = _align
