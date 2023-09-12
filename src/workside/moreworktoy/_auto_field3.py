"""MoreWorkToy - AutoField
Subclass of DataField"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any
from warnings import warn

from worktoy.core import Function
from worktoy.worktoyclass import WorkToyClass


class UsedArg:
  """Used to indicate that a positional argument has already been used."""

  def __init__(self, originalArg: Any) -> None:
    self._originalArg = originalArg

  def getOriginalArg(self) -> Any:
    """Getter-function for the original argument. """
    return self._originalArg


class AutoField(WorkToyClass):
  """MoreWorkToy - AutoField
  Subclass of DataField"""

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
    self._defaultValue = (args or (None,))[0]
    if self._defaultValue is not None:
      self._sourceType = type(self._defaultValue)
    self._fieldName = None
    self._fieldOwner = None
    self._getterFunction = None
    self._setterFunction = None
    self._encoderFunction = None
    self._decoderFunction = None

  def SET(self, setterFunction: Function) -> Function:
    """Decorator for the setter function"""
    if self._setterFunction is not None:
      raise TypeError
    self._setterFunction = setterFunction
    return setterFunction

  def GET(self, getterFunction: Function) -> Function:
    """Decorator for the getter function"""
    if self._getterFunction is None:
      raise TypeError
    self._getterFunction = getterFunction
    return getterFunction

  def ENC(self, encoderFunction: Function) -> Function:
    """Decorator for the encoder function"""
    if self._encoderFunction is None:
      raise TypeError
    self._encoderFunction = encoderFunction
    return self._encoderFunction

  def DEC(self, decoderFunction: Function) -> Function:
    """Decorator for the decoder function"""
    if self._decoderFunction is None:
      raise TypeError
    self._decoderFunction = decoderFunction
    return self._decoderFunction

  def __set_name__(self, owner: type, name: str) -> None:
    """Triggered when the owner class is created."""
    self.setFieldName(name)
    self.setFieldOwner(owner)

  def getSourceType(self, ) -> type:
    """Getter-function for the source type"""
    return self._sourceType

  def setSourceType(self, sourceType: type) -> None:
    """Setter-function for the source type"""
    self._sourceType = sourceType

  def getDefaultValue(self, ) -> Any:
    """Getter-function for the default value"""
    return self._defaultValue

  def setDefaultValue(self, defaultValue: Any) -> None:
    """Setter-function for the default value"""
    self._defaultValue = defaultValue
    if self._sourceType is None:
      self._sourceType = type(self._defaultValue)
    elif not isinstance(defaultValue, self._sourceType):
      raise TypeError

  def typeGuard(self, arg: Any) -> Any:
    """Returns the given argument if it passes type check. Otherwise,
    raises an exception."""
    if self._sourceType is None:
      return arg
    if isinstance(arg, self._sourceType):
      return arg
    raise TypeError

  def getPrivateFieldName(self, ) -> str:
    """Getter-function for the private field name on the object. """
    return '_%s' % self.getFieldName()

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
    existing = getattr(fieldOwner, '__auto_fields__', {})
    existing |= {self.getFieldName(): self}
    setattr(fieldOwner, '__auto_fields__', existing)
    self._fieldOwner = self.wrapInit(fieldOwner)

  def __get__(self, obj: Any, cls: type) -> Any:
    """Getter function"""
    out = getattr(obj, self.getPrivateFieldName(), None)
    if out is None:
      setattr(obj, self.getPrivateFieldName(), self.getDefaultValue())
    return getattr(obj, self.getPrivateFieldName())

  def __set__(self, obj: Any, newValue: Any) -> None:
    """Setter function"""
    setattr(obj, self.getPrivateFieldName(), self.typeGuard(newValue))

  def __delete__(self, obj: Any, ) -> None:
    """Deleter function"""
    raise NotImplementedError

  def getGetterFunction(self, ) -> Function:
    """Getter-functino for getter"""
    if self._getterFunction is None:
      def getter(obj, ) -> Any:
        """Getter-function"""
        return getattr(obj, self.getPrivateFieldName(), )

      return getter
    if isinstance(self._getterFunction, Function):
      return self._getterFunction
    raise TypeError

  def getSetterFunction(self) -> Function:
    """Getter-function for setter"""
    if self._setterFunction is None:
      def setter(obj, newValue: Any) -> None:
        """Setter-function"""
        setattr(obj, self.getPrivateFieldName(), self.typeGuard(newValue))

      return setter
    if isinstance(self._setterFunction, Function):
      return self._setterFunction
    raise TypeError

  def getEncoderFunction(self) -> Function:
    """
    Getter-function for encoder. This getter tries the following encoders
    in the order given:
      1. Method decorated by this instance as encoder.
      2. An encoder defined on the source type
      3. Attempts to directly apply 'json.dumps'
    This encoder assumes that the object to be encoded is the current
    instance.
    """
    if isinstance(self._encoderFunction, Function):
      return self._encoderFunction

    def encodeInstance(instance: Any, obj: Any) -> str:
      """Encodes itself as it appears on the given object."""
      value = AutoField.explicitGetter(instance, obj)

    return encodeInstance

  def getDecoderFunction(self, encodedData: str) -> Function:
    """
    Getter-function for decoder. This getter tries the following decoders
    in the order given:
      1. Method decorated byu this instance as decoder.
      2. A decoder defined on the source type
      3. Attempts to directly apply 'json.loads'
    This decoder attempts to create a new instance of this class and then
    attempts to match the field values on the new instance with the data
    given to decode.
    """

    if isinstance(self._encoderFunction, Function):
      return self._decoderFunction

    def decodeInstance(encodedData: str) -> Any:
      """Decodes the encoded data creating a new instance."""

  def explicitGetter(self, obj: Any) -> Any:
    """Explicit getter function"""
    getter = self.getGetterFunction()
    return getter(obj)

  def explicitSetter(self, obj: Any, newValue: Any) -> None:
    """Explicit getter function"""
    setter = self.getSetterFunction()
    return setter(obj, newValue)

  def explicitEncoder(self, value: Any) -> Any:
    """Explicit encoder function"""
    encoder = self.getEncoderFunction()
    return encoder(value)

  def explicitDecoder(self, encodedData: str) -> Any:
    """Explicit decoder function"""
    decoder = self.getDecoderFunction()
    return decoder(encodedData)

  def wrapInit(self, cls: type) -> type:
    """Wraps the __init__ on the fieldOwner. Please note, that for each
    auto field this method runs, thus only the field appearing last in the
    class body is actually used."""

    autoFields = getattr(cls, '__auto_fields__', {})
    if not autoFields:
      warn('wrapInit invoked, but no auto fields were present!')
      return cls

    def __auto_fields_kwargs__(instance: Any, *args, **kwargs) -> None:
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

    def __auto_fields_args__(instance: Any, *args, **kwargs) -> None:
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
