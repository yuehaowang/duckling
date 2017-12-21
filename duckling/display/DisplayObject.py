from ..events.EventDispatcher import EventDispatcher
from ..geom.Matrix33 import Matrix33


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

	def getRootMatrix(self):
		if self.parent != DisplayObject.PARENT_ROOT:
			m = self.parent.getRootMatrix()
		else:
			m = Matrix33()

		m.translate(self.x, self.y)
		m.scale(self.scaleX, self.scaleY)
		m.rotate(self.rotation)

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

	def display(self, renderer):
		renderer.save()

		renderer.translate(self.x, self.y)
		renderer.scale(self.scaleX, self.scaleY)
		renderer.rotate(self.rotation)

		self._drawSelf(renderer)

		renderer.restore()

	def _drawSelf(self, renderer):
		pass
		