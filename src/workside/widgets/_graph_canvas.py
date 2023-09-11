"""WorkSide - Widgets - GraphCanvas
Canvas allowing users to draw."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtCore import Qt, QRect, QPoint, QLine
from PySide6.QtGui import QPaintEvent, QPainter, QPen, QColor
from PySide6.QtWidgets import QWidget
from worktoy.worktoyclass import WorkToyClass

from workside.tools import Color


class GraphCanvas(QWidget, WorkToyClass):
  """WorkSide - Widgets - GraphCanvas
  Canvas allowing users to draw."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self._gridGap = None
    self._gridPen = None
    self._solidGridPen = None
    self._gridColor = None
    self._gridPenStyle = None

    parent = self.maybeType(QWidget, *args)
    if parent is None:
      QWidget.__init__(self, )
    else:
      QWidget.__init__(self, parent)

  def createGridGap(self) -> None:
    """Creator-function for the grid gap."""
    self._gridGap = 32

  def getGridGap(self, **kwargs) -> int:
    """Getter-function for the grid gap"""
    if self._gridGap is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self.createGridPenStyle
        varType = Qt.PenStyle
        varName = '_gridPenStyle'
        raise RecursiveCreateGetError(creator, varType, varName)
      self.createGridPenStyle()
      return self.getGridGap(_recursion=True)
    return self._gridGap

  def createGridPenStyle(self) -> None:
    """Creator-function for the grid pen style"""
    self._gridPenStyle = Qt.PenStyle.DashLine

  def getGridPenStyle(self, **kwargs, ) -> Qt.PenStyle:
    """Getter-function for the grid pen style."""
    if self._gridPenStyle is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self.createGridPenStyle
        varType = Qt.PenStyle
        varName = '_gridPenStyle'
        raise RecursiveCreateGetError(creator, varType, varName)
      self.createGridPenStyle()
      return self.getGridPenStyle(_recursion=True)
    return self._gridPenStyle

  def createGridColor(self, ) -> None:
    """Creator function for the grid color"""
    self._gridColor = QColor(91, 91, 91)

  def getGridColor(self, **kwargs) -> QColor:
    """Getter-function for the grid color"""
    if self._gridColor is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self.createGridColor
        varType = QColor
        varName = '_gridColor'
        raise RecursiveCreateGetError(creator, varType, varName)
      self.createGridColor()
      return self.getGridColor(_recursion=True)
    return self._gridColor

  def createGridPen(self) -> QPen:
    """Creator function for the grid pen"""
    self._gridPen = QPen()
    self._gridPen.setStyle(self.getGridPenStyle)
    self._gridPen.setColor(self.getGridColor())
    self._gridPen.setWidth(1)
    return self._gridPen

  def getGridPen(self, **kwargs) -> QPen:
    """Getter-function for the grid pen"""
    if self._gridPen is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self.createGridColor
        varType = QColor
        varName = '_gridColor'
        raise RecursiveCreateGetError(creator, varType, varName)
      self.createGridPen()
      return self.getGridPen(_recursion=True)
    return self._gridPen

  def createSolidGridPen(self) -> None:
    """Creator function for the solid grid pen"""
    self._solidGridPen = QPen()
    self._solidGridPen.setStyle(Qt.PenStyle.SolidLine)
    self._solidGridPen.setWidth(1)
    self._solidGridPen.setColor(self.getGridColor())

  def getSolidGridPen(self, **kwargs) -> QPen:
    """Getter-function for the solid grid line"""
    if self._solidGridPen is None:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = self.createSolidGridPen
        varType = QPen
        varName = '_solidGridPenStyle'
        raise RecursiveCreateGetError(creator, varType, varName)
      self.createSolidGridPen()
      return self.getSolidGridPen(_recursion=True)
    return self._solidGridPen

  def parseColor(self, *args, **kwargs) -> QColor:
    """Parses arguments to color"""

  def penFactory(self, *args, **kwargs) -> QPen:
    """QPen factory"""
    intArgs = self.maybeTypes(int, *args)
    widthArg = None
    if intArgs:
      widthArg = min(intArgs)
    widthKeys = self.stringList("""width, w, lineWidth, lineThickness, 
      thickness""")

  def getViewPort(self, ) -> QRect:
    """Getter-function for the viewport"""
    return self.visibleRegion().boundingRect()

  def paintEvent(self, event: QPaintEvent) -> None:
    """Implementation of the paint event."""
    painter = QPainter()
    painter.begin(self)
    viewRect = painter.viewport()
    vLines, hLines = [], []
    w, h = viewRect.weight(), viewRect.height()
    x0 = int((w % self.getGridGap()) / 2)
    y0 = int((h % self.getGridGap()) / 2)
    X, Y = [x0], [y0]
    vLines.append(QLine(QPoint(x0, 0), QPoint(x0, h)))
    hLines.append(QLine(QPoint(0, y0), QPoint(w, y0)))
    while x0 + self.getGridGap() < w and y0 + self.getGridGap() < h:
      if x0 + self.getGridGap() < w:
        x0 += self.getGridGap()
        vLines.append(QLine(QPoint(x0, 0), QPoint(x0, h)))
      if y0 + self.getGridGap() < h:
        y0 += self.getGridGap()
        hLines.append(QLine(QPoint(0, y0), QPoint(w, y0)))
    gridPen = self.getGridPen()
    solidPen = self.getSolidGridPen()
    for i, line in enumerate(hLines):
      pass
