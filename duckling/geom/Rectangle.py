from ..core.Object import Object


class Rectangle(Object):
	def __init__(self, x = 0, y = 0, w = 0, h = 0):
		super(Rectangle, self).__init__()

		self.x = x
		self.y = y
		self.width = w
		self.height = h

	def setTo(self, x, y, w, h):
		self.x = x
		self.y = y
		self.width = w
		self.height = h

	def __str__(self):
		return "Rectangle(%s, %s, %s, %s)" % (self.x, self.y, self.width, self.height)

	__repr__ = __str__
