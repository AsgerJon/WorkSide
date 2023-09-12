"""MoreWorkToy - AutoClass
Subclass of DataClass automating accessors."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Any

from worktoy.descriptors import DataClass

from workside.moreworktoy._auto_field3 import AutoField


class AutoClass(DataClass):
  """MoreWorkToy - AutoClass
  Subclass of DataClass automating accessors."""

  def __init__(self, *args, **kwargs) -> None:
    DataClass.__init__(self, *args, **kwargs)
    self._innerClass = None

  def __call__(self, target: type) -> type:
    """Decorates the type with the auto class functionality"""
    if self._innerClass is not None:
      raise TypeError
    setattr(target, '__auto_class__', True)
    self._innerClass = target

    def encodeAll(obj: Any) -> str:
      """Encodes the auto fields on the class"""
      out = {}
      fieldDictionary = getattr(self._innerClass, '__auto_fields__', {})
      for name, field in fieldDictionary.items():
        if isinstance(field, AutoField):
          fieldValue = field.explicitGetter(obj)
          encodedData = field.explicitEncoder(fieldValue)
          out |= {name: encodedData}
      return json.dumps(out)

    def decodeAll(encodedData: str) -> Any:
      """Creates a new instance of inner class. Then decodes the
      encodedData and populates the auto fields on the inner class."""
      fieldDictionary = getattr(self._innerClass, '__auto_fields__', {})
      decodedDataFields = json.loads(encodedData)
      decodedInstance = self._innerClass()

      for fieldName, autoField in fieldDictionary.items():
        fieldEncodedData = decodedDataFields.get(fieldName, None)
        fieldValue = autoField.explicitDecoder(fieldEncodedData)
        setattr(decodedInstance, fieldName, fieldValue)
      return decodedInstance

    setattr(target, 'decodeAll', decodeAll)
    setattr(target, 'encodeAll', encodeAll)
    return target
