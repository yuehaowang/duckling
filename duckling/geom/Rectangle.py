from ..core.Object import Object


class Rectangle(Object):
	def __init__(self, x = 0, y = 0, w = 0, h = 0):
		super(Rectangle, self).__init__()

		self.x = x
		self.y = y
		self.width = w
		self.height = h
	
	def contains(self, x, y):
		return self.x <= x <= (self.x + self.width) and self.y <= y <= (self.y + self.height)

	def containsRect(self, rect):
		return rect.x >= self.x and (rect.x + rect.width) <= (self.x + self.width) and rect.y >= self.y and (rect.y + rect.height) <= (self.y + self.height)
		
	def equals(self, v):
		return v.x == self.x and v.width == self.width and v.y == self.y and v.height == self.height

	def inflate(self, dx, dy):
		self.width += dx
		self.height += dy

	def intersection(self, t):
		ix = self.x if self.x > t.x else t.x
		iy = self.y if self.y > t.y else t.y
		ax = (t.x + t.width) if (self.x + self.width) > (t.x + t.width) else (self.x + self.width)
		ay = (t.y + t.height) if (self.y + self.height) > (t.y + t.height) else (self.y + self.height)

		if ix <= ax and iy <= ay:
			return Rectangle(ix, iy, ax, ay)
		else:
			return Rectangle(0, 0, 0, 0)

	def intersects(self, t):
		ix = self.x if self.x > t.x else t.x
		iy = self.y if self.y > t.y else t.y
		ax = (t.x + t.width) if (self.x + self.width) > (t.x + t.width) else (self.x + self.width)
		ay = (t.y + t.height) if (self.y + self.height) > (t.y + t.height) else (self.y + self.height)

		return ix <= ax and iy <= ay

	def isEmpty(self):
		return self.x == 0 and self.y == 0 and self.width == 0 and self.height == 0

	def offset(self, dx, dy):
		self.x += dx
		self.y += dy

	def setEmpty(self):
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0

	def setTo(self, x, y, w, h):
		if not isinstance(x, (int, float)):
			x = 0
		if not isinstance(y, (int, float)):
			y = 0
		if not isinstance(w, (int, float)):
			w = 0
		if not isinstance(h, (int, float)):
			h = 0

		self.x = x
		self.y = y
		self.width = w
		self.height = h

	def union(self, t):
		return Rectangle(t.x if self.x > t.x else self.x, t.y if self.y > t.y else self.y, (self.x + self.width) if (self.x + self.width) > (t.x + t.width) else (t.x + t.width), (self.y + self.height) if (self.y + self.height) > (t.y + t.height) else (t.y + t.height))

	def __str__(self):
		return "Rectangle(%s, %s, %s, %s)" % (self.x, self.y, self.width, self.height)

	__repr__ = __str__
