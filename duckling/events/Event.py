from ..core.Object import Object


class Event(Object):
	def __init__(self, n):
		super(Event, self).__init__()

		self.id = n
		self.target = None
		self.currentTarget = None
