"""WorkSide - Widgets - CoreWidget
The core widget is the abstract baseclass shared by the widgets in the
WorkSide framework."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import QEvent, Signal, QPointF, QPoint, Qt, QRect
from PySide6.QtGui import QPaintEvent, QPainter, QFontMetrics, QFont
from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.descriptors import Flag, Field, FloatAttribute, StrAttribute, \
  IntAttribute
from worktoy.worktoyclass import WorkToyClass

from workside.draw import BackgroundStyleState, BackgroundStyle, \
  FontStyleState, FontStyle

ic.configureOutput(includeContext=True)


class CoreWidget(QWidget, WorkToyClass, ):
  """WorkSide - Widgets - CoreWidget
  The core widget is the abstract baseclass shared by the widgets in the
  WorkSide framework.

  textState should be one of:
    legend
    paragraph
    header
    title
  """

  text = Field()
  textState = StrAttribute('legend')
  alignmentFlags = Field()
  vAlign = IntAttribute()  # {-1: 'left', 0: 'center', 1: 'right'}
  hAlign = IntAttribute()  # {-1: 'up', 0: 'center', 1: 'down'}

  mousePos = Field()
  backgroundStyle = Field()
  fontStyle = Field()

  enter = Signal(QWidget, )
  leave = Signal(QWidget, )
  move = Signal(QWidget)

  hovered = Flag(False)
  mouseX = FloatAttribute(0)
  mouseY = FloatAttribute(0)

  drawBackground = Flag(True)
  drawText = Flag(False)

  @classmethod
  def handleStateChange(cls, widget: QWidget, ) -> None:
    """Handles state changes"""
    widget.update()

  @classmethod
  def handleMouseMove(cls, widget: CoreWidget, point: QPointF = None,
                      ) -> None:
    """Handles mouse moves."""
    if isinstance(point, QPoint):
      widget.mousePos = point.toPointF()
    if isinstance(point, QPointF):
      widget.mousePos = point

  @mousePos.getter
  def getMousePos(self, *_) -> QPointF:
    """Getter-function for the mouse position."""
    return QPointF(self.mouseX, self.mouseY)

  @mousePos.setter
  def setMousePos(self, point: QPointF) -> None:
    """Setter-function for the mouse position"""
    self.mouseX, self.mouseY = point.x(), point.y()

  @alignmentFlags.getter
  def getAlignmentFlags(self) -> Qt.AlignmentFlag:
    """Getter-function for alignment flags as defined by the Qt Enum."""
    wrap = Qt.TextFlag.TextWordWrap
    bottom = Qt.AlignmentFlag.AlignBottom
    right = Qt.AlignmentFlag.AlignRight
    top = Qt.AlignmentFlag.AlignTop
    left = Qt.AlignmentFlag.AlignLeft
    hCenter = Qt.AlignmentFlag.AlignHCenter
    vCenter = Qt.AlignmentFlag.AlignVCenter
    justify = Qt.AlignmentFlag.AlignJustify
    return wrap | right | bottom

  def getViewRect(self) -> QRect:
    """Getter-function for the rectangle holding the viewport. """
    return self.visibleRegion().boundingRect()

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    parent = self.maybeType(QWidget, *args)
    QWidget.__init__(self, parent)
    self.setMouseTracking(True)
    self.enter.connect(self.__class__.handleStateChange)
    self.leave.connect(self.__class__.handleStateChange)
    strArg = self.maybeType(str, *args, )
    if isinstance(strArg, str):
      self.text = strArg

  @backgroundStyle.getter
  def getBackgroundStyle(self, ) -> BackgroundStyleState:
    """Getter-function for background style"""
    state = 'hover' if self.hovered else 'base'
    return BackgroundStyle.getStateStyle(state)

  @fontStyle.getter
  def getFontStyle(self) -> FontStyleState:
    """Getter-function for the font style"""
    textStates = self.stringList('legend, paragraph, header, title')
    if self.textState in textStates:
      return FontStyle.getStateFont(self.textState)

  def getFont(self) -> QFont:
    """Getter-function for the QFont with the current text state.-"""
    return self.fontStyle.font

  def getFontMetrics(self) -> QFontMetrics:
    """Getter-function for the font metrics."""
    return QFontMetrics(self.getFont(), self)

  def getTextRect(self, targetRect: QRect = None) -> QRect:
    """Getter-function for the rectangle that would hold this text whilst
    being constrained to the given target rectangle. This target defaults
    to the current viewport of this widget.
    GET RECT!! LMAO"""
    targetRect = self.maybe(targetRect, self.getViewRect())
    flags = self.getAlignmentFlags()
    return self.getFontMetrics().boundingRect(targetRect, flags, self.text)

  def event(self, event: QEvent) -> bool:
    """Takes 'enter', 'leave' and 'move' events to update the hovered
    flag."""
    self.hAlign = 1
    self.vAlign = 1
    if event.type() == QEvent.Type.Leave:
      self.hovered = False
      self.leave.emit(self, )
    elif event.type() == QEvent.Type.Enter:
      self.hovered = True
      self.enter.emit(self, )
    elif event.type() == QEvent.Type.Move:
      pass
    return QWidget.event(self, event)

  def paintEvent(self, event: QPaintEvent) -> None:
    """Paint event"""
    from workside.widgets import WorkPainter
    WorkPainter.paintMeLike(self)

  def __str__(self, ) -> str:
    """String representation"""
    return 'Core Class'

  def __repr__(self) -> str:
    """Code representation"""
    return self.__class__.__qualname__
