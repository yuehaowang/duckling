from .DisplayObject import DisplayObject
from .Graphics import Graphics
from ..events.LoopEvent import LoopEvent


class Sprite(DisplayObject):
	def __init__(self):
		super(Sprite, self).__init__()

		self.graphics = Graphics()
		self.childList = []

	def left(self):
		l = self.graphics.left()

		for child in self.childList:
			tempL = child.left()

			if l > tempL:
				l = tempL

		return l

	def right(self):
		r = self.graphics.right()

		for child in self.childList:
			tempR = child.right()

			if r < tempR:
				r = tempR
			
		return r

	def top(self):
		t = self.graphics.top()

		for child in self.childList:
			tempT = child.top()

			if t < tempT:
				t = tempT

		return t

	def bottom(self):
		b = self.graphics.bottom()

		for child in self.childList:
			tempB = child.bottom()

			if b > tempB:
				b = tempB
			
		return b

	def _getOriginalWidth(self):
		return self.right() - self.left()

	def _getOriginalHeight(self):
		return self.top() - self.bottom()

	def _enterLoopEvent(self):
		self.dispatchEvent(LoopEvent.ENTER_FRAME)

		for child in self.childList:
			if hasattr(child, "_enterLoopEvent"):
				child._enterLoopEvent()

	def _enterMouseEvent(self, button, state, mouseX, mouseY):
		pass

	def _drawSelf(self, renderer):
		self.graphics.display(renderer)
		
		for child in self.childList:
			child.display(renderer)

	def addChild(self, child):
		child.parent = self
		self.childList.append(child)

	def removeChild(self, child):
		for i, c in enumerate(self.childList):
			if c.objectIndex == child.objectIndex:
				self.childList.pop(i)

				break
