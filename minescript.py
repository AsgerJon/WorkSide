"""workside - Core - minescript
Mocking the minescript module"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from worktoy.core import Function


def execute(command: str) -> None:
  """LMAO"""
  pass


def echo(message: str) -> None:
  """LMAO"""
  pass


def chat(message: str) -> None:
  """LMAO"""
  pass


def log(message: str) -> None:
  """LMAO"""
  pass


def player_name() -> str:
  """LMAO"""
  pass


def register_chat_message_interceptor(interceptor: Function) -> None:
  """LMAO"""
  pass


def unregister_chat_message_interceptor() -> None:
  """LMAO"""
  pass


def register_chat_message_listener(listener: Function) -> None:
  """LMAO"""
  pass
