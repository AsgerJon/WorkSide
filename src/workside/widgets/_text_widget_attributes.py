"""WorkSide - Widgets - TextWidgetAttributes
Attribute class for the TextWidget class"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from typing import Never

from PySide6.QtGui import QFont

from workside.settings import Color, Black, MixCase, Normal, FontCase

from workside.widgets import AbstractWidget
from worktoy.descriptors import Attribute


class TextWidgetAttributes(AbstractWidget, ):
  """ Attribute class for the TextWidget class """

  @staticmethod
  def alignLeft(text: str, n: int) -> str:
    """Aligns the text left and pads to n chars plus padding"""
    return '%s%s%s ' % (' ', text, ((n - len(text)) * ' '))

  @staticmethod
  def alignRight(text: str, n: int) -> str:
    """Aligns the text right and pads to n chars plus padding"""
    return ' %s%s%s' % (((n - len(text)) * ' '), text, ' ')

  @staticmethod
  def alignCenter(text: str, n: int) -> str:
    """Aligns the text right and pads to n chars plus padding"""
    return str.center(text, n, ' ')

  currentText = Attribute('Hello World')
  fontFamily = Attribute('Modern No. 20')
  fontSize = Attribute()
  fontWeight = Attribute(Normal)
  fontCap = Attribute(MixCase)
  fontColor = Attribute(Black)
  lineLength = Attribute(40)
  letterSpacing = Attribute(0)
  wordSpacing = Attribute(0)
  textAlign = Attribute('left')

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  currentText  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @currentText.GET
  def getCurrentText(self, ) -> str:
    """Getter-function for currentText"""
    n = self.lineLength
    lines = self.wordWrap(self.__current_text__, self.lineLength)
    if self.textAlign == 'left':
      return '\n'.join([self.alignLeft(line, n) for line in lines])
    if self.textAlign == 'center':
      return '\n'.join([self.alignCenter(line, n) for line in lines])
    if self.textAlign == 'right':
      return '\n'.join([self.alignRight(line, n) for line in lines])
    if self.textAlign == 'justify':
      raise NotImplementedError
    raise ValueError

  @currentText.SET
  def setCurrentText(self, newValue: str) -> None:
    """Setter-function for currentText"""
    self.__current_text__ = newValue

  @currentText.DEL
  def delCurrentText(self, *_) -> Never:
    """Illegal deleter-function for currentText"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'currentText'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  fontFamily  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @fontFamily.GET
  def getFontFamily(self, ) -> str:
    """Getter-function for fontFamily"""
    return self.__font_family__

  @fontFamily.SET
  def setFontFamily(self, newValue: str) -> None:
    """Setter-function for fontFamily"""
    self.__font_family__ = newValue

  @fontFamily.DEL
  def delFontFamily(self, *_) -> Never:
    """Illegal deleter-function for fontFamily"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'fontFamily'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  fontSize  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @fontSize.GET
  def getFontSize(self, ) -> int:
    """Getter-function for fontSize"""
    return self.__font_size__

  @fontSize.SET
  def setFontSize(self, newValue: int) -> None:
    """Setter-function for fontSize"""
    self.__font_size__ = newValue

  @fontSize.DEL
  def delFontSize(self, *_) -> Never:
    """Illegal deleter-function for fontSize"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'fontSize'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  fontWeight  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @fontWeight.GET
  def getFontWeight(self, ) -> QFont.Weight:
    """Getter-function for fontWeight"""
    return self.__font_weight__

  @fontWeight.SET
  def setFontWeight(self, newValue: QFont.Weight) -> None:
    """Setter-function for fontWeight"""
    self.__font_weight__ = newValue

  @fontWeight.DEL
  def delFontWeight(self, *_) -> Never:
    """Illegal deleter-function for fontWeight"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'fontWeight'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<<  fontCap  >>>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @fontCap.GET
  def getFontCap(self, ) -> FontCase:
    """Getter-function for fontCap"""
    return self.__font_cap__

  @fontCap.SET
  def setFontCap(self, newValue: FontCase) -> None:
    """Setter-function for fontCap"""
    self.__font_cap__ = newValue

  @fontCap.DEL
  def delFontCap(self, *_) -> Never:
    """Illegal deleter-function for fontCap"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'fontCap'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<  letterSpacing  >>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @letterSpacing.GET
  def getLetterSpacing(self, ) -> int:
    """Getter-function for letterSpacing"""
    return self.__letter_spacing__

  @letterSpacing.SET
  def setLetterSpacing(self, newValue: int) -> None:
    """Setter-function for letterSpacing"""
    self.__letter_spacing__ = newValue

  @letterSpacing.DEL
  def delLetterSpacing(self, *_) -> Never:
    """Illegal deleter-function for letterSpacing"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'letterSpacing'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<  wordSpacing  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @wordSpacing.GET
  def getWordSpacing(self, ) -> float:
    """Getter-function for wordSpacing"""
    return self.__word_spacing__

  @wordSpacing.SET
  def setWordSpacing(self, newValue: float) -> None:
    """Setter-function for wordSpacing"""
    self.__word_spacing__ = newValue

  @wordSpacing.DEL
  def delWordSpacing(self, *_) -> Never:
    """Illegal deleter-function for wordSpacing"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'wordSpacing'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  fontColor  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @fontColor.GET
  def getFontColor(self, ) -> Color:
    """Getter-function for fontColor"""
    return self.__font_color__

  @fontColor.SET
  def setFontColor(self, newValue: Color) -> None:
    """Setter-function for fontColor"""
    self.__font_color__ = newValue

  @fontColor.DEL
  def delFontColor(self, *_) -> Never:
    """Illegal deleter-function for fontColor"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'fontColor'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  lineLength  >>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @lineLength.GET
  def getLineLength(self, ) -> int:
    """Getter-function for lineLength"""
    return self.__line_length__

  @lineLength.SET
  def setLineLength(self, newValue: int) -> None:
    """Setter-function for lineLength"""
    self.__line_length__ = newValue

  @lineLength.DEL
  def delLineLength(self, *_) -> Never:
    """Illegal deleter-function for lineLength"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'lineLength'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  # | <<<<<<<<<<<<<<<<<<<<<<<<<<  textAlign  >>>>>>>>>>>>>>>>>>>>>>>>>> | #
  # | ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ | #
  @textAlign.GET
  def getTextAlign(self, ) -> str:
    """Getter-function for textAlign"""
    return self.__text_align__

  @textAlign.SET
  def setTextAlign(self, newValue: str) -> None:
    """Setter-function for textAlign"""
    self.__text_align__ = newValue

  @textAlign.DEL
  def delTextAlign(self, *_) -> Never:
    """Illegal deleter-function for textAlign"""
    from worktoy.waitaminute import ProtectedAttributeError
    attName = 'textAlign'
    insName = str(self)
    clsName = self.__class__
    raise ProtectedAttributeError(attName, insName, clsName)

  # | _________________________________________________________________ | #
  def __init__(self, *args, **kwargs) -> None:
    AbstractWidget.__init__(self, *args, **kwargs)
    self.__current_text__ = 'Hello World'
    self.__font_family__ = 'Modern No. 20'
    self.__font_size__ = 12
    self.__font_weight__ = Normal
    self.__font_cap__ = MixCase
    self.__letter_spacing__ = 0
    self.__word_spacing__ = 0
    self.__font_color__ = Black
    self.__line_length__ = 60
    self.__text_align__ = 'left'
