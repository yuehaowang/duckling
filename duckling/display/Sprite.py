from .DisplayObject import DisplayObject
from .Graphics import Graphics


class Sprite(DisplayObject):
	def __init__(self):
		super(Sprite, self).__init__()

		self.graphics = Graphics()
		self.childList = []

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
