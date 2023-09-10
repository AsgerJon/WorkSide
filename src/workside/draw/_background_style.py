"""WorkSide - Draw - BackgroundStyle"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
import os

from icecream import ic
from worktoy.worktoyclass import WorkToyClass

from workside.draw import BackgroundStyleState

ic.configureOutput(includeContext=True)

State = BackgroundStyleState


class BackgroundStyle(WorkToyClass, ):
  """Style contains an instance of the State class for each mouse state."""

  __style_states__ = {}

  @staticmethod
  def getJsonFilePath() -> str:
    """Getter-function for the"""
    here = os.path.dirname(__file__)
    fileName = 'style_settings.json'
    filePath = os.path.join(here, fileName)
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
    styleDict = {}
    for (key, val) in data.items():
      state = BackgroundStyleState()
      state.radius = val.get('cornerRadius', None)
      state.width = val.get('borderWidth', None)
      red = val.get('border', None).get('red', None)
      green = val.get('border', None).get('green', None)
      blue = val.get('border', None).get('blue', None)
      state.borderRed = red
      state.borderGreen = green
      state.borderBlue = blue
      styleDict |= {key: state}
    setattr(cls, '__style_states__', styleDict)

  @classmethod
  def getStyles(cls, **kwargs) -> dict[str, BackgroundStyleState]:
    """Getter function for the style matching the given state."""
    styles = getattr(cls, '__style_states__', None)
    if not styles:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = cls.loadStates
        varType = dict
        varName = '__style_states__'
        raise RecursiveCreateGetError(creator, varType, varName)
      cls.loadStates()
      return cls.getStyles(_recursion=True)
    return styles

  @classmethod
  def getStateStyle(cls, state: str) -> BackgroundStyleState:
    """Getter-function for the styles at the given state. """
    styles = cls.getStyles()
    stateStyle = styles.get(state, None)
    if stateStyle is None:
      raise TypeError
    return stateStyle
