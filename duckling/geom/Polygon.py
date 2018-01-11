from ..core.Object import Object
from .Rectangle import Rectangle
from .Vec2 import Vec2


class Polygon(Object):
	def __init__(self, o = None):
		super(Polygon, self).__init__()

		if isinstance(o, list):
			self.vertices = o
		elif isinstance(o, Rectangle):
			x = o.x
			y = o.y
			w = o.width
			h = o.height

			self.vertices = [Vec2(x, y), Vec2(x + w, y), Vec2(x + w, y + h), Vec2(x, y + h)]
		else:
			self.vertices = []

	def getTransform(self, m):
		res = []

		for p in self.vertices:
			arr = m.toArray([p.x, p.y, 1])
			res.append(Vec2(arr[0], arr[1]))

		return Polygon(res)

	def getSides(self):
		vtx = self.vertices
		l = len(vtx)
		res = []

		if l >= 3:
			preP = vtx[0]

			for p in vtx[1:]:
				res.append(Vec2.substract(p, preP))

				preP = p

			res.append(Vec2.substract(vtx[0], vtx[l - 1]))

		return res

	def getProjection(self, axis):
		vtx = self.vertices
		mini = None
		maxi = None

		for p in vtx:
			pro = Vec2.dot(p, axis) / axis.length()

			if mini == None or pro < mini:
				mini = pro

			if maxi == None or pro > maxi:
				maxi = pro

		return {"min" : mini, "max" : maxi}

	def getNearestPoint(self, p1):
		vtx = self.vertices
		rP = vtx[0]
		minDis = Vec2.distance(p1, rP)

		for p2 in vtx[1:]:
			d = Vec2.distance(p1, p2)

			if d < minDis:
				minDis = d
				rP = p2

		return rP

	def __str__(self):
		return "Polygon(%s)" % self.vertices

	__repr__ = __str__
