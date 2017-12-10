from .Event import Event


class LoopEvent(Event):
	def __init__(self, n):
		super(LoopEvent, self).__init__(n)

LoopEvent.ENTER_FRAME = LoopEvent("__dkl_event_enter_frame")
