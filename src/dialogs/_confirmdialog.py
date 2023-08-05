"""ConfirmDialog provides a dialog to confirm a user action. """
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtWidgets import QDialog, QGridLayout
from icecream import ic

from workside.widgets import CoreWidget

ic.configureOutput(includeContext=True)


class ConfirmDialog(QDialog):
  """ConfirmDialog provides a dialog to confirm a user action.
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, *args, **kwargs) -> None:
    parent = CoreWidget.parseParent(*args, **kwargs)
    QDialog.__init__(self, parent, )
    self._baseLayout = None
    self._baseWidget = None
    self._confirmButton = None
    self._rejectButton = None
    self._icon = None
    self._headerLabel = None

  def _createBaseLayout(self) -> NoReturn:
    """Creates the base layout"""
    self._baseLayout = QGridLayout()

  def _getBaseLayout(self, ) -> QGridLayout:
    """Getter-function for the baseLayout"""
    if self._baseLayout is None:
      self._createBaseLayout()
      return self._getBaseLayout()
    if isinstance(self._baseLayout, QGridLayout):
      return self._baseLayout
    raise TypeError

  def _createBaseWidget(self) -> NoReturn:
    """Creates the base layout"""
    self._baseWidget = CoreWidget()

  def _getBaseWidget(self, ) -> CoreWidget:
    """Getter-function for the baseWidget"""
    if self._baseWidget is None:
      self._createBaseWidget()
      return self._getBaseWidget()
    if isinstance(self._baseWidget, CoreWidget):
      return self._baseWidget
    raise TypeError
