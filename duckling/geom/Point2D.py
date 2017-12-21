from ..core.Object import Object


class Point2D(Object):
	def __init__(self, x = 0, y = 0):
		super(Point2D, self).__init__()

		self.x = x
		self.y = y

	def __str__(self):
		return "Point2D(%s, %s)" % (self.x, self.y)

	__repr__ = __str__
