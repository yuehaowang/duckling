import math
from ..core.Object import Object


class Circle(Object):
	def __init__(self, x = 0, y = 0, r = 0):
		super(Circle, self).__init__()

		self.x = x
		self.y = y
		self.r = r

	def getTransform(self, m):
		v1 = m.toArray([self.x, self.y, 1])
		v2 = m.toArray([self.x + self.r, self.y, 1])
		dx = v1[0] - v2[0]
		dy = v1[1] - v2[1]

		return Circle(v1[0], v1[1], math.sqrt(dx ** 2 + dy ** 2))

	def getProjection(self, axis):
		pro = Vec2.dot(Vec2(self.x, self.y), axis) / axis.length()

		return {"min" : pro - self.r, "max" : pro + self.r}

	def __str__(self):
		return "Circle(%s, %s, %s)" % (self.x, self.y, self.r)

	__repr__ = __str__
