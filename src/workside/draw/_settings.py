"""WorkSide - Draw - Settings
Reads settings from json file that is exposed to the user."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
import os

from PySide6.QtGui import QColor
from worktoy.descriptors import IntAttribute, Field, StrAttribute
from worktoy.worktoyclass import WorkToyClass

from workside.draw import Color


class BackgroundStyleState(WorkToyClass):
  """Class representation of the styles required to specify a background
  painting. """

  stateName = StrAttribute()

  cornerRadius = IntAttribute(5)
  borderWidth = IntAttribute(2)
  fillRed = IntAttribute(255)
  fillGreen = IntAttribute(255)
  fillBlue = IntAttribute(255)
  borderRed = IntAttribute(0)
  borderGreen = IntAttribute(0)
  borderBlue = IntAttribute(0)

  fillColor = Field()
  borderColor = Field()

  fillQColor = Field()
  borderQColor = Field()

  @borderColor.getter
  def getBorderColor(self, ) -> Color:
    """Getter-function for border color"""
    return Color(self.borderRed, self.borderGreen, self.borderBlue)

  @borderQColor.getter
  def getBorderQColor(self) -> QColor:
    return QColor(self.borderRed, self.borderGreen, self.borderBlue)

  @fillColor.getter
  def getFillColor(self, ) -> Color:
    """Getter-function for border color"""
    return Color(self.fillRed, self.fillGreen, self.fillBlue)

  @fillQColor.getter
  def getFillQColor(self) -> QColor:
    return QColor(self.fillRed, self.fillGreen, self.fillBlue)

  @borderColor.setter
  def setBorderColor(self, color: Color) -> None:
    """Setter-function for the border color."""
    self.borderRed = color.red
    self.borderGreen = color.green
    self.borderBlue = color.blue

  @fillColor.setter
  def setFillColor(self, color: Color) -> None:
    """Setter-function for the border color."""
    self.fillRed = color.red
    self.fillGreen = color.green
    self.fillBlue = color.blue

  @borderQColor.setter
  def setBorderQColor(self, color: QColor) -> None:
    """Setter-function for the border color."""
    self.borderRed = color.red()
    self.borderGreen = color.green()
    self.borderBlue = color.blue()

  @fillQColor.setter
  def setFillQColor(self, color: QColor) -> None:
    """Setter-function for the border color."""
    self.fillRed = color.red()
    self.fillGreen = color.green()
    self.fillBlue = color.blue()

  @staticmethod
  def dictColor(rgb: dict) -> Color:
    """Loads a color from the rgb data"""
    red = rgb.get('red', 255)
    green = rgb.get('green', 255)
    blue = rgb.get('blue', 255)
    return Color(red, green, blue)

  @classmethod
  def fromJson(cls, data: dict, keyName: str) -> BackgroundStyleState:
    """Creates an instance from the data in the json data entry. """
    cls.__core_instance__ = cls()
    state = cls()
    state.cornerRadius = data.get('cornerRadius', state.cornerRadius)
    state.borderWidth = data.get('borderWidth', state.borderWidth)
    state.border = cls.dictColor(data.get('border', {}))
    state.fill = cls.dictColor(data.get('fill', {}))
    state.stateName = keyName
    return state

  def __str__(self, ) -> str:
    """String representation"""
    msg = """%s:\n
    Fill Color: %s, Border Color: %s, Corner Radius: %s, Border 
      Width: %s"""
    fill, border = self.fillColor, self.borderColor
    radius, width = self.cornerRadius, self.borderWidth
    return msg % (fill, border, radius, width)

  def __repr__(self, ) -> str:
    """Code representation."""
    fill, border = self.fillColor, self.borderColor
    radius, width = self.cornerRadius, self.borderWidth
    name = self.__class__.__qualname__
    return '%s(%s, %s, %s, %s)' % (name, fill, border, radius, width)


class BackgroundStyle(WorkToyClass):
  """Style contains an instance of the State class for each mouse state."""

  __style_states__ = {}

  @classmethod
  def getStyleStates(cls, ) -> dict[str, BackgroundStyleState]:
    """Getter-function for the style states."""
    return cls.__style_states__

  @staticmethod
  def getJsonFilePath() -> str:
    """Getter-function for the"""
    here = os.path.dirname(__file__)
    fileName = 'style_settings.json'
    filePath = os.path.join(here, fileName)
    print(filePath)
    return filePath

  @classmethod
  def loadJSONFile(cls) -> str:
    """Loads the given json file."""
    filePath = cls.getJsonFilePath()
    with open(filePath, 'r') as f:
      data = f.read()
    return data

  @classmethod
  def parseJson(cls, ) -> dict:
    """Parses the json data"""
    data = cls.loadJSONFile()
    return json.loads(data)

  @classmethod
  def loadStates(cls, ) -> None:
    """Creates BackgroundStyleState instances for each entry in the json
    data."""
    data = cls.parseJson()
    for (key, val) in data.items():
      state = BackgroundStyleState.fromJson(val, key)
      cls.getStyleStates().update({key: state})

  def __str__(self, ) -> str:
    """String representation."""
    states = [str(v) for (k, v) in self.getStyleStates().items()]
    return '\n'.join(states)
