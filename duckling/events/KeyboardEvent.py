from OpenGL.GLUT import *

from ..core.Keyboard import Keyboard
from .Event import Event


class KeyboardEvent(Event):
	def __init__(self, n):
		super(KeyboardEvent, self).__init__(n)

KeyboardEvent.KEY_DOWN = KeyboardEvent("__dkl_keyboard_event_key_down")
