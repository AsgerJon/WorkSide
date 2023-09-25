"""WorkToy - Core - ParseCode
Code writing assistant"""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from icecream import ic

from worktoy.descriptors import Attribute, FieldInstance
from worktoy.settings import tabIndent
from worktoy.texttools import Header
from worktoy.worktoyclass import AbstractTemplate

ic.configureOutput(includeContext=True)


class FieldClass(AbstractTemplate):
  """WorkSide - Core - ParseCode
  Code writing assistant"""

  addedFields = Attribute([])
  className = Attribute('NewClass')
  classParent = Attribute()
  metaClass = Attribute()
  classDoc = Attribute('Documentation')

  def __init__(self, *args, **kwargs) -> None:
    AbstractTemplate.__init__(self, *args, **kwargs)
    nameKeys = self.stringList("""name, clsName, className""")
    nameKwarg = self.searchKey(*nameKeys, **kwargs)
    docKeys = self.stringList("""docString, docs, doc, documentation""")
    docKwarg = self.searchKey(*docKeys, **kwargs)
    nameArg, docArg = [*self.maybeTypes(str, *args), *(None, None,)][:2]
    nameDefault, docDefault = 'NewClass', 'Documentation'
    self.className = self.maybe(nameKwarg, nameArg, nameDefault)
    self.classDoc = self.maybe(docKwarg, docArg, docDefault)
    mclsKeys = self.stringList("""mcls, metaclass, type""")
    mclsKwarg = self.searchKey(*mclsKeys, **kwargs)
    parentKeys = self.stringList("""parent, parentClass, super""")
    parentKwarg = self.searchKey(*parentKeys, **kwargs)
    parentArg, mclsArg = None, None
    parentDefault, mclsDefault = object, type
    for arg in args:
      if isinstance(arg, type):
        if issubclass(arg, type) and mclsArg is None:
          mclsArg = arg  # Indicates arg is a metaclass or type.
        elif parentArg is None:
          parentArg = arg  # Indicates arg is a class, but not a metaclass.
    self.mcls = self.maybe(mclsKwarg, mclsArg, mclsDefault)
    self.parent = self.maybe(parentKwarg, parentArg, parentDefault)

  def getTabTags(self) -> dict[str, str]:
    """Getter-function for tab tags"""
    return {'<tab=%d>' % i: tabIndent * i for i in range(16)}

  def getTags(self) -> dict[str, str]:
    """Getter-function for the dictionary mapping tags to replacements"""
    return {
      **self.getTabTags(),
      '<clsName>': self.className,
      '<parent>' : self.classParent,
      '<mcls>'   : self.metaClass,
      '<doc>'    : self.classDoc,
    }

  def addField(self, *args, **kwargs) -> None:
    """Adds a 'FieldInstance' or creates a field instance. """
    fieldArg = self.maybeType(FieldInstance, *args)
    if isinstance(fieldArg, FieldInstance):
      return self.addedFields.append(fieldArg)
    return self.addedFields.append(self.createField(*args, **kwargs))

  def createField(self, *args, **kwargs) -> FieldInstance:
    """Creates and returns a field instance"""
    return FieldInstance(*args, **kwargs)

  def clsHead(self) -> list[str]:
    """Code lines for the class header"""
    return [
      'class <clsName>(<parent>, metaclass=<mcls>):',
      '<tab=1>\"\"\"<doc>\"\"\"',
    ]

  def baseInit(self) -> list[str]:
    """Getter-function for code creating the '__init__' method."""
    return [
      '<tab=1>def __init__(self, *args, **kwargs) -> None:',
      '<tab=2><parent>.__init__(self, *args, **kwargs)',
    ]

  def buildClassHead(self) -> list[str]:
    """Returns the class header with the current values."""
    return [self.render(line) for line in self.clsHead()]

  def buildAttributes(self) -> list[str]:
    """Returns the list of attributes definitions in the class body"""
    outLines = []
    for attr in self.addedFields:
      for line in attr.clsCode:
        outLines.append(self.render(line))
    return outLines

  def buildAccessors(self) -> list[str]:
    """Builds the accessor for each attribute"""
    outLines = []
    for attr in self.addedFields:
      outLines.append(str(Header(attr.name)))
      for acc in [attr.getCode, attr.setCode, attr.delCode]:
        for line in acc:
          outLines.append(self.render(line))
    return outLines

  def buildInit(self) -> list[str]:
    """Builds the general '__init__' method"""
    return [self.render(line) for line in self.baseInit()]

  def buildInitDefaultValues(self) -> list[str]:
    """Collects the entries in the '__init__' for each attribute."""
    outLines = []
    for attr in self.addedFields:
      for line in attr.initCode:
        outLines.append(self.render(line))
    return outLines

  def buildClass(self) -> str:
    """Builds the entire class"""
    out = []
    for line in self.buildClassHead():
      out.append(line)
      out.append('\n')
    for line in self.buildAttributes():
      out.append(line)
      out.append('\n')
    for line in self.buildAccessors():
      out.append(line)
      out.append('\n')
    for line in self.buildInit():
      out.append(line)
      out.append('\n')
    for line in self.buildInitDefaultValues():
      out.append(line)
    return '\n'.join(out)
