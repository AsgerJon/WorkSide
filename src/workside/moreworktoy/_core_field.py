"""MoreWorkToy - IntField
Integer valued descriptor"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import json
from typing import Any
from warnings import warn

from worktoy.worktoyclass import WorkToyClass


class UsedArg:
  """Used to indicate that a positional argument has already been used."""

  def __init__(self, originalArg: Any) -> None:
    self._originalArg = originalArg

  def getOriginalArg(self) -> Any:
    """Getter-function for the original argument. """
    return self._originalArg


class CoreField(WorkToyClass):
  """MoreWorkToy - IntField
  Integer valued descriptor"""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    base = (args or (None,))[0]
    if isinstance(base, type):
      self._sourceType = base
      self._defaultValue = base()
    elif base is not None:
      self._defaultValue = base
      self._sourceType = type(base)
    else:
      raise ValueError('Default value or source type required!')
    if self._sourceType not in [int, float, str]:
      msg = """The type given: %s is not one of the supported types: %s, 
        %s and %s""" % (self._sourceType, int, float, str)
      raise TypeError(msg)
    self._fieldName = None
    self._fieldOwner = None

  def getDefaultValue(self, ) -> Any:
    """Getter-function for the default value"""
    return self._defaultValue

  def __get__(self, obj: Any, cls: type) -> Any:
    """Getter function"""
    return self.explicitGetter(obj)

  def __set__(self, obj: Any, newValue: Any) -> None:
    """Setter function"""
    return self.explicitSetter(obj, newValue)

  def __delete__(self, obj: Any, ) -> None:
    """Deleter function"""
    raise NotImplementedError

  def __set_name__(self, owner: type, name: str) -> None:
    """Triggered when the owner class is created."""
    self.setFieldName(name)
    self.setFieldOwner(owner)

  def getSourceType(self) -> type:
    """Getter-function for the type"""
    return self._sourceType

  def getFieldName(self) -> str:
    """Getter-function for field name"""
    return self._fieldName

  def setFieldName(self, fieldName: str) -> None:
    """Setter-function for field name"""
    self._fieldName = fieldName

  def getFieldOwner(self) -> type:
    """Getter-function for field owner"""
    return self._fieldOwner

  def setFieldOwner(self, fieldOwner: type) -> None:
    """Setter-function for field owner"""
    existing = getattr(fieldOwner, '__core_fields__', {})
    existing |= {self.getFieldName(): self}
    setattr(fieldOwner, '__core_fields__', existing)
    self._fieldOwner = fieldOwner

  def getPrivateFieldName(self, ) -> str:
    """Getter-function for the private field name on the object. """
    return '_%s' % self.getFieldName()

  def wrapInit(self, cls: type) -> type:
    """Wraps the __init__ on the fieldOwner. Please note, that for each
    core field this method runs, thus only the field appearing last in the
    class body is actually used."""

    autoFields = getattr(cls, '__core_fields__', {})
    if not autoFields:
      warn('wrapInit invoked, but no core fields were present!')
      return cls

    def __auto_fields_kwargs__(instance: Any, *__, **kwargs) -> None:
      """This method tries to populate auto fields from keyword arguments."""
      kwargs = {**kwargs, }
      for fieldName, autoField in autoFields.items():
        pvtName = autoField.getPrivateFieldName()
        if getattr(instance, pvtName, None) is None:
          fieldType = autoField.getSourceType()
          fieldKwarg = None
          kwargVal = kwargs.get(fieldName, None)
          if isinstance(kwargVal, fieldType) and fieldKwarg is None:
            fieldKwarg = kwargVal
            kwargs[fieldName] = UsedArg(kwargVal)
            setattr(instance, pvtName, fieldKwarg)

    def __auto_fields_args__(instance: Any, *args, **_) -> None:
      """This method populates auto fields from the positional and keyword
      arguments. """
      args = [arg for arg in args if not isinstance(arg, UsedArg)]
      for fieldName, autoField in autoFields.items():
        pvtName = autoField.getPrivateFieldName()
        if getattr(instance, pvtName, None) is None:
          fieldType = autoField.getSourceType()
          fieldArg = None
          fieldDefVal = autoField.getDefaultValue()
          for i, arg in enumerate(args):
            if fieldArg is None:
              if isinstance(arg, fieldType):
                fieldArg = arg
                args[i] = UsedArg(arg)
          setattr(instance, pvtName, self.maybe(fieldArg, fieldDefVal))

    originalInit = getattr(cls, '__init__')

    def __new_init__(instance, *args, **kwargs) -> None:
      """This is the combination of the original init and the extra init.
      Please note, that if the original init is not implemented,
      it defaults to object.__init__. In this edge case, only the extra
      init is used."""
      __auto_fields_kwargs__(instance, *args, **kwargs)
      __auto_fields_args__(instance, *args, **kwargs)
      if originalInit is object.__init__:
        originalInit(instance, )
      else:
        originalInit(instance, *args, **kwargs)

    setattr(cls, '__init__', __new_init__)
    return cls

  def explicitGetter(self, obj: Any) -> Any:
    """Explicit getter function"""
    out = getattr(obj, self.getPrivateFieldName(), None)
    if out is None:
      setattr(obj, self.getPrivateFieldName(), self.getDefaultValue())
    return getattr(obj, self.getPrivateFieldName())

  def explicitSetter(self, obj: Any, newValue: Any) -> None:
    """Explicit getter function"""
    setattr(obj, self.getPrivateFieldName(), newValue)

  def encode(self, obj: Any) -> str:
    """Encodes self"""
    typeNames = [(int, '__int__'), (float, '__float__'), (str, '__str__'), ]
    typeName = None
    for type_, name in typeNames:
      if typeName is None:
        if type_ is self.getSourceType():
          typeName = name
    value = self.explicitGetter(obj)
    data = {'__core_type__': typeName, '__core_value__': value}
    return json.dumps(data)

  def decode(self, obj: Any, encodedData: str) -> None:
    """The decoder"""
    data = json.loads(encodedData)
    self.explicitSetter(obj, data['__core_value__'])
    # sourceType = self.getSourceType()
    # if sourceType == str:
    #   return self.explicitSetter(obj, CoreField.decodeStr(value))
    # elif sourceType == int:
    #   return self.explicitSetter(obj, CoreField.decodeInt(value))
    # elif sourceType == float:
    #   return self.explicitSetter(obj, CoreField.decodeFloat(value))

  @staticmethod
  def decodeStr(data: str) -> str:
    """Returns the string as is"""
    return data

  @staticmethod
  def decodeInt(data: str) -> int:
    """Decodes to integer"""
    digs = {str(i): i for i in range(10)}

    data = [c for c in reversed(data) if digs.get(c, None) is not None]
    out = 0
    for i, char in enumerate(data):
      num = digs.get(char, None)
      if num is not None:
        out += (num * 10 ** i)
    return out

  @staticmethod
  def decodeFloat(data: str) -> float:
    """Decodes to float"""
    if '.' not in data:
      if ',' not in data:
        if ';' not in data:
          if '|' not in data:
            data = '%s.0' % data
          else:
            data = data.replace('|', '.')
        else:
          data = data.replace(';', '.')
      else:
        data = data.replace(',', '.')
    digs = ['%d' % i for i in range(10)] + ['.', ]
    data = [char for char in data if char in digs]
    data = ''.join(data)
    left, right = data.split('.')[:2]
    n = len(right)
    intVal = CoreField.decodeInt(data)
    return intVal * 10 ** (-n)
