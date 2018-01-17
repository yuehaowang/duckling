import math

from ..core.Object import Object


class Point2D(Object):
	def __init__(self, x = 0, y = 0):
		super(Point2D, self).__init__()

		self.x = x
		self.y = y

	@staticmethod
	def distance(p1, p2):
		return Point2D.distance2(p1.x, p1.y, p2.x, p2.y)

	@staticmethod
	def distance2(x1, y1, x2, y2):
		x = x1 - x2
		y = y1 - y2

		return math.sqrt(x ** 2 + y ** 2)

	@staticmethod
	def interpolate(p1, p2, f):
		return Point2D(p1.x + (p2.x - p1.x) * (1 - f), p1.y + (p2.y - p1.y) * (1 - f))

	@staticmethod
	def polar(l, a):
		return Point2D(l * math.cos(a), l * math.sin(a))

	def length(self):
		return Point2D.distance2(self.x, self.y, 0, 0)

	def setTo(self, x, y):
		if not isinstance(x, (int, float)):
			x = 0
		if not isinstance(y, (int, float)):
			y = 0

		self.x = x
		self.y = y

	def copyFrom(self, s):
		self.setTo(s.x, s.y)

	def equals(self, t):
		return self.x == t.x and self.y == t.y

	def normalize(self, t):
		l = self.length()

		if l <= 0:
			return

		scale = t / l

		self.x *= scale
		self.y *= scale

	def offset(self, dx, dy):
		self.x += dx
		self.y += dy

	@staticmethod
	def add(v1, v2):
		return Point2D(v1.x + v2.x, v1.y + v2.y)

	@staticmethod
	def substract(v1, v2):
		return Point2D(v1.x - v2.x, v1.y - v2.y)

	@staticmethod
	def fromVec2(v):
		return Point2D(v.x, v.y)

	def __str__(self):
		return "Point2D(%s, %s)" % (self.x, self.y)

	__repr__ = __str__

	def __add__(self, v):
		return Point2D.add(self, v)

	def __sub__(self, v):
		return Point2D.substract(self, v)
