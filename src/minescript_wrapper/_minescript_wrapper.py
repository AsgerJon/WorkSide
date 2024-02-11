"""Minescript Wrapper
Wraps the interface with Minescript."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Optional

from minescript_wrapper import Item, Player, Entity, World, Block
from minescript_wrapper import Position, Listener, PositionF

from worktoy.worktoyclass import WorkToyClass
from worktoy.core import Function


class MinescriptWrapper(WorkToyClass):
  """Minescript Wrapper
  Wraps the interface with Minescript."""

  def __init__(self, *args, **kwargs) -> None:
    WorkToyClass.__init__(self, *args, **kwargs)
    self._minescript = (args or (None,))[0]

  def execute(self, command: str) -> None:
    """Runs the command"""
    return self._minescript.execute(command)

  def echo(self, message: str) -> None:
    """Echoes the message"""
    return self._minescript.execute(message)

  def chat(self, message: str) -> None:
    """Prepends space"""
    return self._minescript.execute(message)

  def log(self, message: str) -> bool:
    """Logs message"""
    return self._minescript.log(message)

  def screenshot(self, filePath: str) -> bool:
    """Saves a screenshot to given file path"""
    return self._minescript.screenshot(filePath)

  def flush(self) -> None:
    """Waits for job to complete"""
    return self._minescript.flush()

  def player_name(self) -> str:
    """Returns the player name"""
    return self._minescript.player_name()

  def player_position(self, callBack: Function = None) -> PositionF:
    """Returns [x: float, y: float, z: float] synchronously if given call
    back is None. Otherwise, runs the given call back on the list of
    coordinates."""
    if callBack is None:
      x, y, z = self._minescript.player_position()
      return PositionF(x, y, z)
    return self._minescript.player_position(callBack)

  def player_set_position(self, *args: float) -> bool:
    """Moves the player. Takes 3 to 5 floats: x, y, z, yaw and pitch."""
    posArg = self.maybeType(Position, *args)
    posFArg = self.maybeType(PositionF, *args)
    floatArgs = self.maybeType(float, *args)
    x, y, z = None, None, None
    if posFArg is not None:
      x, y, z = posFArg.x, posFArg.y, posFArg.z
    elif posArg is not None:
      x, y, z = posArg.x, posArg.y, posArg.z
    if self.empty(x, y, z) and len(floatArgs) > 2:
      return self._minescript.player_set_position(*floatArgs)
    from worktoy.waitaminute import TypeSignatureException
    supported = [
      (Position, float, float),
      (PositionF, float, float),
      (Position, float,),
      (PositionF, float,),
      (Position,),
      (PositionF,),
      (float, float, float, float, float),
      (float, float, float, float,),
      (float, float, float,),
    ]
    raise TypeSignatureException(args, *supported, )

  def player_hand_items(
      self, callBack: Function = None) -> Optional[list[Item]]:
    """Returns the list of items with index 0 being main hand and index 1
    at off-hand and then the hotbar."""
    if callBack is None:
      out = []
      data = self._minescript.player_hand_items()
      for item in data:
        newItem = Item(**item)
        out.append(newItem)
      return out
    return self._minescript.player_hand_items(callBack)

  def player_inventory(self,
                       callBack: Function = None) -> Optional[list[Item]]:
    """Returns the list of items in the inventory."""
    if callBack is None:
      out = []
      data = self._minescript.player_inventory()
      for item in data:
        newItem = Item(**item)
        out.append(newItem)
      return out
    return self._minescript.player_inventory(callBack)

  def player_inventory_slot_to_hotbar(
      self,
      slot: int,
      callBack: Function = None) -> Optional[int]:
    """Moves the inventory slot at 'slot' to the hotbar returning the
    hotbar slot to which the inventory slot were transferred."""
    return self._minescript.player_inventory_slot_to_hotbar(slot, callBack)

  def player_inventory_select_slot(
      self,
      slot: int,
      callBack: Function = None) -> Optional[int]:
    """Activates hotbar item at 'slot'."""
    return self._minescript.player_inventory_select_slot(slot, callBack)

  def player_press_forward(self, keyStatus: bool) -> None:
    """Presses 'w' when argument is True. """
    return self._minescript.player_press_forward(keyStatus)

  def player_press_backward(self, keyStatus: bool) -> None:
    """Presses 's' when argument is True. """
    return self._minescript.player_press_backward(keyStatus)

  def player_press_left(self, keyStatus: bool) -> None:
    """Presses 'a' when argument is True. """
    return self._minescript.player_press_left(keyStatus)

  def player_press_right(self, keyStatus: bool) -> None:
    """Presses 'd' when argument is True. """
    return self._minescript.player_press_right(keyStatus)

  def player_press_jump(self, keyStatus: bool) -> None:
    """Presses 'SPACE' when argument is True. """
    return self._minescript.player_press_jump(keyStatus)

  def player_press_sprint(self, keyStatus: bool) -> None:
    """Presses 'CTRL' when argument is True. """
    return self._minescript.player_press_sprint(keyStatus)

  def player_press_sneak(self, keyStatus: bool) -> None:
    """Presses 'SHIFT' when argument is True. """
    return self._minescript.player_press_sneak(keyStatus)

  def player_press_pick_item(self, keyStatus: bool) -> None:
    """Presses middle mouse button when argument is True. """
    return self._minescript.player_press_pick_item(keyStatus)

  def player_press_use(self, keyStatus: bool) -> None:
    """Presses 'e' when argument is True. """
    return self._minescript.player_press_use(keyStatus)

  def player_press_attack(self, keyStatus: bool) -> None:
    """Presses left mouse button when argument is True. """
    return self._minescript.player_press_attack(keyStatus)

  def player_press_swap_hands(self, keyStatus: bool) -> None:
    """Presses 'f' when argument is True. """
    return self._minescript.player_press_swap_hands(keyStatus)

  def player_press_drop(self, keyStatus: bool) -> None:
    """Presses 'q' when argument is True. """
    return self._minescript.player_press_drop(keyStatus)

  def player_orientation(self, ) -> tuple[float, float]:
    """Returns yaw and pitch."""
    return self._minescript.player_orientation()

  def player_set_orientation(self, yaw: float, pitch: float) -> None:
    """Sets the orientations."""
    return self._minescript.player_orientation(self, yaw, pitch)

  def player_get_targeted_block(
      self, viewDistance: float = None) -> list:
    """Returns: [[x, y, z], distance, side, block_description]"""
    return self._minescript.player_orientation(self, viewDistance)

  def player_health(self) -> float:
    """Returns the player health"""
    return self._minescript.player_health()

  def players(self, *args, NBT: bool = None) -> list[Player]:
    """Returns dictionary info about the named players"""
    return self._minescript.players(*args, NBT)

  def entities(self, *args, NBT: bool = None) -> list[Entity]:
    """Returns list of entities near the player."""
    return self._minescript.entities(*args, NBT)

  def world_properties(self, ) -> World:
    """Returns information about the active world."""
    return self._minescript.world_properties()

  def getblock(self,
               x: int, y: int, z: int,
               callBack: Function = None) -> Block:
    """Getter-function for the block type at the given coordinates."""
    return self._minescript.getblock(x, y, z, callBack)

  def getblocklist(self, points: list[Position],
                   callBack: Function = None, ) -> list[Block]:
    """Getter-function for list of block types at the given list."""
    pointList = []
    for p in points:
      pointList.append([p.x, p.y, p.z])
    return self._minescript.getblocklist(pointList, callBack)

  def await_loaded_region(self, x1: int, z1: int, x2: int, z2: int,
                          callBack: Function = None, ) -> None:
    """Notifies the caller when the region from (x1, z1) to (x2, z2) is
    loaded."""
    return self.await_loaded_region(x1, z1, x2, z2, callBack)

  def register_chat_message_listener(self, listener: Listener) -> None:
    """Registers the listener to monitor chat."""
    self.register_chat_message_listener(listener)

  def unregister_chat_message_listener(self) -> None:
    """Unregisters the listener to monitor chat."""
    self.unregister_chat_message_listener()

  def register_chat_message_interceptor(self, listener: Listener) -> None:
    """Registers the listener to interceptor chat."""
    self.register_chat_message_interceptor(listener)

  def unregister_chat_message_interceptor(self) -> None:
    """Unregisters the listener to interceptor chat."""
    self.unregister_chat_message_interceptor()
