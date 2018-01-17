from .DisplayObject import DisplayObject
from .Graphics import Graphics
from ..events.LoopEvent import LoopEvent
from ..events.MouseEvent import MouseEvent


class Sprite(DisplayObject):
	def __init__(self):
		super(Sprite, self).__init__()

		self._cacheIsMouseOn = False
		self.childList = []
		self.shapes = []
		self.mouseEnabled = True
		self.mouseChildren = True
		self.mouseShelter = True
		self.graphics = Graphics()
		self.graphics.parent = self

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

	def _enterMouseEvent(self, eve, m):
		isOn = False

		if self._isMouseOn(eve["mouseX"], eve["mouseY"], m):
			if self.mouseShelter:
				isOn = True

			eveData = {
				"mouseX" : eve["mouseX"],
				"mouseY" : eve["mouseY"],
				"selfX" : eve["mouseX"] - m.c - self.x,
				"selfY" : eve["mouseY"] - m.f - self.y
			}

			if "button" in eve and "state" in eve:
				if eve["state"] == 0:
					eveType = MouseEvent.MOUSE_DOWN
				else:
					eveType = MouseEvent.MOUSE_UP

				eveData["button"] = eve["button"]
			else:
				eveType = MouseEvent.MOUSE_MOVE

			if self.mouseEnabled:
				self.dispatchEvent(eveType, data=eveData)

			if self.mouseChildren:
				for child in self.childList[::-1]:
					if isinstance(child, Sprite):
						if child._enterMouseEvent(eve, m):
							break

		self._cacheIsMouseOn = False

		return isOn

	def _isMouseOn(self, x, y, m):
		if self._cacheIsMouseOn:
			return True

		t = self.getMatrix()
		t.add(m)

		for child in self.childList:
			if child._isMouseOn(x, y, t):
				self._cacheIsMouseOn = True

				return True

		if self.graphics._isMouseOn(x, y, t):
			self._cacheIsMouseOn = True

			return True

		return False

	def _drawSelf(self, renderer):
		self.graphics.display(renderer)
		
		for child in self.childList:
			child.display(renderer)

	def addShape(self, sh):
		self.shapes.append(sh)

	def addChild(self, child):
		child.parent = self
		self.childList.append(child)

	def removeChild(self, child):
		for i, c in enumerate(self.childList):
			if c.objectIndex == child.objectIndex:
				self.childList.pop(i)

				break

	def removeAllChildren(self):
		self.childList.clear()

	def destroy(self):
		self.removeAllChildren()
		self.graphics.clear()
		self.removeAllEventListeners()
