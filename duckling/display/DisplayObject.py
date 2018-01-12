from ..events.EventDispatcher import EventDispatcher
from ..geom.Matrix33 import Matrix33
from ..geom.Vec2 import Vec2
from ..geom.SAT import SAT
from ..geom.Polygon import Polygon
from ..geom.Circle import Circle


class DisplayObject(EventDispatcher):
	PARENT_ROOT = "__dkl_parent_root"

	def __init__(self):
		super(DisplayObject, self).__init__()

		self.x = 0
		self.y = 0
		self.rotation = 0
		self.scaleX = 1
		self.scaleY = 1
		self.parent = None
		self.name = "displayObject%s" % self.objectIndex

	def getRootMatrix(self):
		p = self
		m = Matrix33()

		while p and p != DisplayObject.PARENT_ROOT:
			m.scale(p.scaleX, p.scaleY)
			m.rotate(p.rotation)
			m.translate(p.x, p.y)

			p = p.parent
		
		return m

	def getMatrix(self):
		m = Matrix33()
		
		m.scale(self.scaleX, self.scaleY)
		m.rotate(self.rotation)
		m.translate(self.x, self.y)
		
		return m

	def left(self):
		return self.x

	def right(self):
		return self.x + self.getWidth()

	def top(self):
		return self.y + self.getHeight()

	def bottom(self):
		return self.y

	def getWidth(self):
		return self._getOriginalWidth() * self.scaleX

	def getHeight(self):
		return self._getOriginalHeight() * self.scaleY

	def _getOriginalWidth(self):
		return 0

	def _getOriginalHeight(self):
		return 0

	def _isMouseOn(self, x, y, m):
		t = self.getMatrix()
		t.add(m)

		sh = Polygon([Vec2(0, 0), Vec2(self._getOriginalWidth(), 0), Vec2(self._getOriginalWidth(), self._getOriginalHeight()), Vec2(0, self._getOriginalHeight())]).getTransform(t)

		return SAT.hitTest(Circle(x, y, 0), sh)

	def display(self, renderer):
		renderer.save()

		renderer.translate(self.x, self.y)
		renderer.rotate(self.rotation)
		renderer.scale(self.scaleX, self.scaleY)

		self._drawSelf(renderer)

		renderer.restore()

	def _drawSelf(self, renderer):
		pass
		