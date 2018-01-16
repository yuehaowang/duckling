from .Polygon import Polygon
from .Circle import Circle
from .Vec2 import Vec2


class SAT(object):
	@staticmethod
	def hitTest(A, B):
		res = None

		if isinstance(A, Polygon) and isinstance(B, Polygon):
			res = SAT.hitTestPolygons(A, B)
		elif isinstance(A, Circle) and isinstance(B, Circle):
			res = SAT.hitTestCircles(A, B)
		else:
			c = None
			p = None

			if isinstance(A, Circle):
				c = A
				p = B
			else:
				c = B
				p = A

			res = SAT.hitTestCircleAndPolygon(c, p)

		return res

	@staticmethod
	def hitTestPolygons(a, b):
		sides = a.getSides()
		sides.extend(b.getSides())
		axises = []

		for side in sides:
			axises.append(side.normL())

		return SAT.__isGap(axises, a, b)

	@staticmethod
	def hitTestCircles(a, b):
		axis = Vec2(a.x - b.x, a.y - b.y)
		
		proA = a.getProjection(axis)
		proB = b.getProjection(axis)

		if SAT.__isOverlay(proA, proB):
			return False

		return True

	@staticmethod
	def hitTestCircleAndPolygon(c, p):
		sides = p.getSides()
		axises = []

		for side in sides:
			axises.append(side.normL())

		p1 = p.getNearestPoint(Vec2(c.x, c.y))

		axises.append(Vec2(p1.x - c.x, p1.y - c.y))

		return SAT.__isGap(axises, c, p)

	@staticmethod
	def __isGap(axises, a, b):
		for axis in axises:
			proA = a.getProjection(axis)
			proB = b.getProjection(axis)

			if SAT.__isOverlay(proA, proB):
				return False

		return True

	@staticmethod
	def __isOverlay(proA, proB):
		mini = None
		maxi = None

		if proA["min"] < proB["min"]:
			mini = proA["min"]
		else:
			mini = proB["min"]

		if proA["max"] > proB["max"]:
			maxi = proA["max"]
		else:
			maxi = proB["max"]

		return (proA["max"] - proA["min"]) + (proB["max"] - proB["min"]) < maxi - mini
