"""WorkSide - Tools - BoxAlign
Class representation of box alignment. This class specifies how a
rectangle is positioned inside another."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Union, Any

from PySide6.QtCore import Qt
from worktoy.descriptors import Field

from workside.tools import AbstractTools


class BoxAlign(AbstractTools):
  """WorkSide - Tools - BoxAlign
  Class representation of box alignment. This class specifies how a
  rectangle is positioned inside another."""

  vertical = Field()
  horizontal = Field()
  verticalKeys = Field()
  horizontalKeys = Field()

  @staticmethod
  def getFlag(name: Union[str, int]) -> Qt.AlignmentFlag:
    """Finds the alignment flag with the given name or value"""
    for item in Qt.AlignmentFlag:
      if name in [item.name, item.value]:
        return item

  @horizontal.GET
  def getHorizontalAlignment(self) -> Qt.AlignmentFlag:
    """Getter-function for horizontal alignment flag"""
    return self._horizontalAlignment

  @vertical.GET
  def getVerticalAlignment(self) -> Qt.AlignmentFlag:
    """Getter-function for vertical alignment flag"""
    return self._verticalAlignment

  def _parseKwargs(self, ) -> tuple[Qt.AlignmentFlag, Qt.AlignmentFlag]:
    """Parses keyword arguments"""
    keys = self.getKeywordArgs().keys()
    items = self.getKeywordArgs().items()
    if 'horizontal' in keys and 'vertical' in keys:
      hFlag, vFlag = items['horizontal'], items['vertical']
      self.useArg('horizontal')
      self.useArg('vertical')
      return hFlag, vFlag

  def _parseArgs(self) -> tuple[Qt.AlignmentFlag, Qt.AlignmentFlag]:
    """Parses positional arguments"""
    flags = self.maybeTypes(Qt.AlignmentFlag, self.getPosArgs())
    flags = list(set(flags))
    hFlag = [flag for flag in flags if flag.value < 9]
    vFlag = [flag for flag in flags if flag.value > 17]
    if len(hFlag) == 1 and len(vFlag) == 1:
      return hFlag[0], vFlag[0]

  def __init__(self, *args, **kwargs) -> None:
    AbstractTools.__init__(self, *args, **kwargs)
    flags = None
    parsers = [self._parseKwargs, self._parseArgs]
    for parser in parsers:
      if flags is None:
        flags = parser()
    hCenter = Qt.AlignmentFlag.AlignHCenter
    vCenter = Qt.AlignmentFlag.AlignVCenter
    flags = self.maybe(flags, (hCenter, vCenter))
    self._horizontalAlignment = flags[0]
    self._verticalAlignment = flags[1]

  @classmethod
  def saveToJson(cls, instance: BoxAlign = None) -> str:
    """Implementation"""
    return json.dumps(dict(horizontal=instance.horizontal,
                           vertical=instance.vertical))

  @classmethod
  def loadFromJson(cls, data: str) -> BoxAlign:
    """Implementation"""
    data = json.loads(data)
    return BoxAlign(**data)

  def toolSupport(self, tool: type) -> bool:
    """Does not support tools directly!"""
    return False

  def applyTool(self, other: Any) -> Any:
    """Does not support tools directly!"""
    return other
