import math

from .Color import Color
from .DisplayObject import DisplayObject
from ..geom.Point2D import Point2D
from ..geom.Vec2 import Vec2
from ..geom.Polygon import Polygon
from ..geom.Circle import Circle
from ..geom.Rectangle import Rectangle
from ..geom.SAT import SAT


class Graphics(DisplayObject):
	def __init__(self):
		super(Graphics, self).__init__()

		self.arcSmoothness = 2
		self._drawFuncList = []
		self._shapeList = []

	def left(self):
		l = None

		for p in self._shapeList:
			temp = p.left()

			if l == None or l > temp:
				l = temp

		if l == None:
			return 0

		return l

	def right(self):
		r = None

		for p in self._shapeList:
			temp = p.right()

			if r == None or r < temp:
				r = temp

		if r == None:
			return 0
			
		return r

	def top(self):
		t = None

		for p in self._shapeList:
			temp = p.top()

			if t == None or t < temp:
				t = temp

		if t == None:
			return 0
			
		return t

	def bottom(self):
		b = None

		for p in self._shapeList:
			temp = p.bottom()

			if b == None or b > temp:
				b = temp

		if b == None:
			return 0
			
		return b

	def _getOriginalWidth(self):
		return self.right() - self.left()

	def _getOriginalHeight(self):
		return self.top() - self.bottom()

	def _paintClosedShape(self, renderer, lineWidth, strokeStyle, fillStyle):
		if fillStyle != None:
			renderer.setColor(fillStyle)
			renderer.fill()

		self._strokeShape(renderer, lineWidth, strokeStyle)

		renderer.end()

	def _strokeShape(self, renderer, lineWidth, strokeStyle):
		if lineWidth >= 1 and strokeStyle != None:
			renderer.setLineWidth(lineWidth)
			renderer.setColor(strokeStyle)
			renderer.stroke()

	def drawVertices(self, vtx, *, lineWidth = 1, strokeStyle = Color(0, 0, 0, 1), fillStyle = None):
		self._shapeList.append(Polygon(list(map(Vec2.fromPoint2D, vtx))))

		def func(renderer):
			if len(vtx) <= 1:
				return

			renderer.moveTo(vtx[0].x, vtx[0].y)

			for p in vtx[1:]:
				renderer.lineTo(p.x, p.y)

			renderer.closePath()

			self._paintClosedShape(renderer, lineWidth, strokeStyle, fillStyle)

		self._drawFuncList.append(func)

	def drawRect(self, x, y, w, h, *, lineWidth = 1, strokeStyle = Color(0, 0, 0, 1), fillStyle = None):
		self._shapeList.append(Polygon(Rectangle(x, y, w, h)))

		def func(renderer):
			renderer.moveTo(x, y)
			renderer.lineTo(x + w, y)
			renderer.lineTo(x + w, y + h)
			renderer.lineTo(x, y + h)
			renderer.closePath()

			self._paintClosedShape(renderer, lineWidth, strokeStyle, fillStyle)

		self._drawFuncList.append(func)

	def drawLine(self, x0, y0, x1, y1, *, lineWidth = 1, strokeStyle = Color(0, 0, 0, 1)):
		self._shapeList.append(Polygon([Vec2(x0, y0), Vec2(x1, y1)]))

		def func(renderer):
			renderer.moveTo(x0, y0)
			renderer.lineTo(x1, y1)

			self._strokeShape(renderer, lineWidth, strokeStyle)

			renderer.end()

		self._drawFuncList.append(func)

	def drawArc(self, x0, y0, r, *, beginAngle = 0, endAngle = 360, lineWidth = 1, strokeStyle = Color(0, 0, 0, 1), fillStyle = None):
		if abs(endAngle - beginAngle) >= 360:
			self._shapeList.append(Circle(x0, y0, r))

		beginAngle, endAngle = math.radians(beginAngle % 360), math.radians(endAngle % 360)
		w = self.arcSmoothness / r

		if beginAngle < 0:
			beginAngle += math.pi * 2
		if endAngle < 0:
			endAngle += math.pi * 2

		if endAngle <= beginAngle:
			endAngle += math.pi * 2

		def func(renderer):
			renderer.moveTo(x0 + r * math.cos(beginAngle), y0 + r * math.sin(beginAngle))

			currAngle = beginAngle
			while currAngle < endAngle:
				renderer.lineTo(x0 + r * math.cos(currAngle), y0 + r * math.sin(currAngle))

				currAngle += w

			renderer.closePath()

			self._paintClosedShape(renderer, lineWidth, strokeStyle, fillStyle)

		self._drawFuncList.append(func)

	def clear(self):
		self._drawFuncList.clear()

	def _drawSelf(self, renderer):
		for func in self._drawFuncList:
			func(renderer)

	def _isMouseOn(self, x, y, m):
		t = self.getMatrix()
		t.add(m)

		pt = Circle(x, y, 0)

		for p in self._shapeList:
			sh = p.getTransform(m)

			if SAT.hitTest(sh, pt):
				return True

		return False
