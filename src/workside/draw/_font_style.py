"""WorkSide - Draw - FontStyle
Handles the font styles."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
import os

from icecream import ic
from worktoy.worktoyclass import WorkToyClass

from workside.draw import BackgroundStyleState, FontStyleState

ic.configureOutput(includeContext=True)

State = BackgroundStyleState


class FontStyle(WorkToyClass):
  """FontStyle"""

  __font_states__ = {}

  @staticmethod
  def getJsonFilePath() -> str:
    """Getter-function for the"""
    here = os.path.dirname(__file__)
    fileName = 'font_settings.json'
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
    """Creates FontStyleStates instances for each entry in the json data."""
    data = cls.parseJson()
    fontDict = {}
    for (key, val) in data.items():
      instance = FontStyleState.fromJson(val)
      instance.state = key
      fontDict |= {key: instance}
    setattr(cls, '__font_states__', fontDict)

  @classmethod
  def getFonts(cls, **kwargs) -> dict[str, FontStyleState]:
    """Getter function for the font matching the given state"""
    font = getattr(cls, '__font_states__', None)
    if not font:
      if kwargs.get('_recursion', False):
        from worktoy.waitaminute import RecursiveCreateGetError
        creator = cls.loadStates
        varType = dict
        varName = '__font_states__'
        raise RecursiveCreateGetError(creator, varType, varName)
      cls.loadStates()
      return cls.getFonts(_recursion=True)
    return font

  @classmethod
  def getStateFont(cls, state: str) -> FontStyleState:
    """Getter-function for the styles at the given state. """
    fonts = cls.getFonts()
    stateFont = fonts.get(state, None)
    if stateFont is None:
      raise TypeError
    return stateFont
