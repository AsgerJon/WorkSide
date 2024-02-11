"""workside - Core - StrucWidget
Code writing assistant"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from worktoy.descriptors import Attribute


class StrucWidget(QWidget):
  """Widget showing information about the current structure"""

  structureInfo = Attribute()
  structureLayout = Attribute()
  structureLabel = Attribute()
  structureHeader = Attribute()

  def __init__(self, *args, **kwargs) -> None:
    QWidget.__init__(self, *args, **kwargs)
    self._baseLayout = QVBoxLayout()
    self.__structure_info__ = 'No structure here!'
    self.__structure_label__ = None
    self.__structure_header__ = None
    self.__structure_layout__ = None

  def _createStructureLayout(self) -> None:
    """Creator function for the layout"""
    self.__structure_layout__ = QHBoxLayout()

  @structureLayout.GET
  def _getStructureLayout(self, **kwargs) -> QHBoxLayout:
    """Getter function for the layout"""
    if self.__structure_layout__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createStructureLayout()
      return self._getStructureLayout(recursion=True)
    return self.__structure_layout__

  @structureInfo.GET
  def _getStructureInfo(self) -> str:
    """Getter-function for information relating to the current structure"""
    return self.__current_structure_info__

  @structureInfo.SET
  def _setStructureInfo(self, info: str) -> None:
    """Setter-function for information relating to the current structure"""
    self.__current_structure_info__ = info

  def _createStructureHeader(self) -> None:
    """Creator-function for the header widget"""
    self.__structure_header__ = QLabel()
    self.__structure_header__.setText('Current Structure: ')

  @structureHeader.GET
  def _getStructureHeader(self, **kwargs) -> QLabel:
    """Getter-function for the header widget"""
    if self.__structure_header__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createStructureHeader()
      return self._getStructureHeader(recursion=True)
    return self.__structure_header__

  def _createStructureLabel(self) -> None:
    """Creator-function for the widget showing information about the
    current structure"""
    self.__structure_label__ = QLabel()
    self.__structure_label__.setText(self.structureInfo)

  @structureLabel.GET
  def _getStructureLabel(self, **kwargs) -> QLabel:
    """Getter-function for the header widget."""
    if self.__structure_label__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createStructureLabel()
      return self._getStructureLabel(recursion=True)
    return self.__structure_label__

  def setupWidgets(self) -> None:
    """Sets up the widgets"""
    self.structureLayout.addWidget(self.structureHeader)
    self.structureLayout.addWidget(self.structureLabel)
    self.setLayout(self.structureLayout)

  def show(self) -> None:
    """Reimplementation invoking the 'setupWidgets' method before invoking
    the super call."""
    self.setupWidgets()
    super().show()
