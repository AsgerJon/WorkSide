"""WorkSide - StyleStates - AbstractStyleState
This class should define the statespace. Typically, by defining each state
in terms of a set of flags such that each state is defined uniquely by
which flags it raises."""
#  MIT Licence
#  Copyright (c) 2023 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from worktoy.worktoyclass import WorkToyClass


class AbstractStyleState(WorkToyClass):
  """WorkSide - StyleStates - AbstractStyleState
  This class should define the statespace. Typically, by defining each state
  in terms of a set of flags such that each state is defined uniquely be
  which flags it raises."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)

  @abstractmethod
  def getFlags(self) -> list:
    """Getter-function for the list of flags defining the state space. If
    an alternative state space definition than the default one in the
    StyleState subclass, let this method return the 'enabled' flag."""

  @abstractmethod
  def getStates(self) -> list:
    """Getter-function for list of supported states."""
