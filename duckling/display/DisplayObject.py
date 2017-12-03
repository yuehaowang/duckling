from ..events.EventDispatcher import EventDispatcher


class DisplayObject(EventDispatcher):
	def __init__(self):
		super(DisplayObject, self).__init__()

		self.x = 0
		self.y = 0
		self.rotation = 0
		self.scaleX = 1
		self.scaleY = 1

	def display(self, renderer):
		renderer.save()

		renderer.translate(self.x, self.y)
		renderer.scale(self.scaleX, self.scaleY)
		renderer.rotate(self.rotation)

		self._drawSelf(renderer)

		renderer.restore()

	def _drawSelf(self, renderer):
		pass
		