from .DisplayObject import DisplayObject
from .Graphics import Graphics
from ..events.Event import Event


class Sprite(DisplayObject):
	def __init__(self):
		super(Sprite, self).__init__()

		self.graphics = Graphics()
		self.childList = []

	def _enterLoopEvent(self):
		self.dispatchEvent(Event.ENTER_FRAME)

		for child in self.childList:
			if hasattr(child, "_enterLoopEvent"):
				child._enterLoopEvent()

	def _drawSelf(self, renderer):
		self.graphics.display(renderer)
		
		for child in self.childList:
			child.display(renderer)

	def addChild(self, child):
		self.childList.append(child)

	def removeChild(self, child):
		for i, c in enumerate(self.childList):
			if c.objectIndex == child.objectIndex:
				self.childList.pop(i)

				break
