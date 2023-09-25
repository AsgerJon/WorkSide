"""WorkToy - Core - FieldInstance
Code writing assistant."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Never, Any

from icecream import ic

from worktoy.descriptors import Attribute
from moreworktoy.texttools import AbstractTemplate

ic.configureOutput(includeContext=True)


class FieldInstance(AbstractTemplate):
  """WorkSide - Core - FieldInstance
  Code writing assistant."""

  pvtName = Attribute()
  capName = Attribute()
  defVal = Attribute()
  valueType = Attribute()
  permLevel = Attribute(2)
  allowGet = Attribute(True)
  allowSet = Attribute(True)
  allowDel = Attribute(False)
  createCode = Attribute()
  getCode = Attribute()
  setCode = Attribute()
  delCode = Attribute()
  clsCode = Attribute()
  initCode = Attribute()

  @createCode.GET
  def getCreateCode(self) -> list[str]:
    """Getter-function for creator code"""
    out = []
    for line in self.baseCreate():
      out.append(self.render(line))
    return out

  @clsCode.GET
  def getClsCode(self) -> list[str]:
    """Getter-function for class body contribution"""
    out = []
    for line in self.baseBody():
      out.append(self.render(line))
    return out

  @initCode.GET
  def getInitCode(self) -> list[str]:
    """Getter-function for initializer contribution"""
    out = []
    for line in self.baseInit():
      out.append(self.render(line))
    return out

  @allowGet.GET
  def getAllowGet(self) -> bool:
    """Getter-function for allow getter flag"""
    return True if self.permLevel > 0 else False

  @allowSet.GET
  def getAllowSet(self) -> bool:
    """Getter-function for allow setter flag"""
    return True if self.permLevel > 1 else False

  @allowDel.GET
  def getAllowDel(self) -> bool:
    """Getter-function for allow deleter flag"""
    return True if self.permLevel > 2 else False

  @getCode.GET
  def getGetCode(self) -> list[str]:
    """Getter-function for the code creating the getter function"""
    out = []
    lines = self.legalGet() if self.allowGet else self.illegalGet()
    for line in lines:
      out.append(self.render(line))
    return out

  @setCode.GET
  def getSetCode(self) -> list[str]:
    """Getter-function for the code creating the setter function"""
    out = []
    lines = self.legalSet() if self.allowSet else self.illegalSet()
    for line in lines:
      out.append(self.render(line))
    return out

  @delCode.GET
  def getDelCode(self) -> list[str]:
    """Getter-function for the code creating the deleter function"""
    out = []
    lines = self.legalDel() if self.allowDel else self.illegalDel()
    for line in lines:
      out.append(self.render(line))
    return out

  def __init__(self, name: str, defVal: Any, permArg: int,
               *args, **kwargs) -> None:
    """Simplified initiator"""
    AbstractTemplate.__init__(self, *args, **kwargs)
    self.name, self.defVal, self.permLevel = name, defVal, permArg
    self.valueType = type(defVal)

  @pvtName.GET
  def getPrivateName(self, ) -> str:
    """Getter-function for private name."""
    name = self.name
    if all([not c.isupper() for c in name]):
      name = '%sAttribute' % name
    chars = ['_%s' % c.lower() if c.isupper() else c for c in name]
    return '__%s__' % (''.join(chars))

  @capName.GET
  def getCapName(self) -> str:
    """Getter-function for capitalized name"""
    return '%s%s' % (self.name[0].upper(), self.name[1:])

  @classmethod
  def legalGet(cls) -> list[str]:
    """Getter function for the allowed getter code"""
    return [
      '<tab=1>@<fieldName>.GET',
      '<tab=1>def _get<capName>(self, **kwargs) -> <valueType>:',
      '<tab=2>\"\"\"Getter function for <fieldName>\"\"\"',
      '<tab=2>if self.<pvtName> is None:',
      '<tab=3>if kwargs.get(\'_recursion\', False):',
      '<tab=4>from worktoy.waitaminute import RecursiveCreateGetError',
      '<tab=4>creator = self._create<capName>',
      '<tab=4>argType = <valueType>',
      '<tab=4>argName = \'<pvtName>\'',
      '<tab=4>raise RecursiveCreateGetError(creator, argType, argName)',
      '<tab=3>self._create<capName>()',
      '<tab=3>return self._get<capName>(_recursion=True)',
      '<tab=2>return getattr(self, \'<pvtName>\', )',
    ]

  @classmethod
  def legalSet(cls) -> list[str]:
    """Getter function for the allowed setter code"""
    return ['<tab=1>@<fieldName>.SET',
            '<tab=1>def set<capName>(self, newValue: <valueType>) -> None:',
            '<tab=2>\"\"\"Setter-function for <fieldName>\"\"\"',
            '<tab=2>setattr(<valueType>, <pvtNameQuoted>, newValue)', ]

  @classmethod
  def legalDel(cls) -> Never:
    """Allowed deleter is not yet implemented"""
    raise NotImplementedError

  @classmethod
  def illegalGet(cls) -> Never:
    """Illegal getter is not yet implemented"""
    raise NotImplementedError

  @classmethod
  def illegalSet(cls) -> list[str]:
    """Getter function for the illegal setter code"""
    return [
      '<tab=1>@<fieldName>.SET',
      '<tab=1>def set<capName>(self, *_) -> Never:',
      '<tab=2>\"\"\"Illegal setter-function for <fieldName>\"\"\"',
      '<tab=2>from worktoy.waitaminute import ReadOnlyException',
      '<tab=2>attName = \'<fieldName>\'',
      '<tab=2>insName = str(self)',
      '<tab=2>clsName = self.__class__',
      '<tab=2>raise ReadOnlyException(attName, insName, clsName)',
    ]

  @classmethod
  def illegalDel(cls) -> list[str]:
    """Getter function for the illegal setter code"""
    return [
      '<tab=1>@<fieldName>.DEL',
      '<tab=1>def del<capName>(self, *_) -> Never:',
      '<tab=2>\"\"\"Illegal deleter-function for <fieldName>\"\"\"',
      '<tab=2>from worktoy.waitaminute import ProtectedAttributeError',
      '<tab=2>attName = \'<fieldName>\'',
      '<tab=2>insName = str(self)',
      '<tab=2>clsName = self.__class__',
      '<tab=2>raise ProtectedAttributeError(attName, insName, clsName)',
    ]

  def legalCreate(self) -> list[str]:
    """Getter-function for the field value creator function"""
    return [
      '<tab=1>@<fieldName>.CREATE',
      '<tab=1>def _create<capName>(self, ) -> None:',
      '<tab=2>\"\"\"Creator-function for <fieldName>\"\"\"',
      '<tab=2>newInstance = <valueType>()',
      '<tab=2>setattr(<valueType>, <pvtNameQuoted>, newInstance)',
    ]

  def getterCodes(self) -> str:
    """The getter codes"""
    out = []
    for segment in self.baseGet():
      out.append(segment)
    return '\n'.join(out)

  def getTags(self) -> dict[str, str]:
    """Getter-function for the dictionary mapping tags to replacements"""
    return {
      '<valueType>'    : self.valueType.__qualname__,
      '<fieldName>'    : self.name,
      '<pvtName>'      : self.pvtName,
      '<pvtNameQuoted>': '\'%s\'' % (self.pvtName),
      '<capName>'      : self.capName,
      '<defVal>'       : self.defVal,
    }

  def baseInit(self) -> list[str]:
    """Contribution to the '__init__' code."""
    return ['<tab=2>self.<pvtName> = <defVal>', ]

  def baseBody(self) -> list[str]:
    """Contribution to the class body."""
    return ['<tab=1><fieldName> = Field()', ]

  def baseGet(self) -> list[str]:
    """Getter-function for getter code"""
    return self.legalGet() if self.allowGet else self.illegalGet()

  def baseSet(self) -> list[str]:
    """Getter-function for setter code"""
    return self.legalSet() if self.allowSet else self.illegalSet()

  def baseDel(self) -> list[str]:
    """Getter-function for the deleter code"""
    return self.legalDel() if self.allowDel else self.illegalDel()

  def baseCreate(self, ) -> list[str]:
    """Getter-function for the creator code"""
    return self.legalCreate()
