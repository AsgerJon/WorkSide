"""WorkSide - Draw - BackgroundStyle"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
import os
from typing import Any

from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.worktoyclass import WorkToyClass

from workside.draw import BackgroundStyleState

ic.configureOutput(includeContext=True)


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
