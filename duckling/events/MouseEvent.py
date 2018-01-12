from .Event import Event


class MouseEvent(Event):
	def __init__(self, n):
		super(MouseEvent, self).__init__(n)

MouseEvent.MOUSE_DOWN = MouseEvent("__dkl_mouse_event_mouse_down")
MouseEvent.MOUSE_UP = MouseEvent("__dkl_mouse_event_mouse_up")
MouseEvent.MOUSE_MOVE = MouseEvent("__dkl_mouse_event_mouse_move")
