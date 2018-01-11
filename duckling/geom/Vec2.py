from ..core.Object import Object


class Vec2(Object):
	def __init__(self, x = 0, y = 0):
		super(Vec2, self).__init__()
		
		self.x = x
		self.y = y

	def __str__(self):
		return "Vec2(%s, %s)" % (self.x, self.y)

	__repr__ = __str__

	def __add__(self, v):
		return Vec2.add(self, v)

	def __sub__(self, v):
		return Vec2.substract(self, v)
	
	@staticmethod
	def distance(v1, v2):
		dx = v1.x - v2.x
		dy = v1.y - v2.y

		return math.sqrt(dx ** 2 + dy ** 2)

	@staticmethod
	def add(v1, v2):
		return Vec2(v1.x + v2.x, v1.y + v2.y)

	def substract(v1, v2):
		return Vec2(v1.x - v2.x, v1.y - v2.y)

	@staticmethod
	def dot(v1, v2):
		return v1.x * v2.x + v1.y * v2.y

	@staticmethod
	def cross(v1, v2):
		return v1.x * v2.y - v1.y * v2.x

	def length(self):
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def normalize(self):
		l = self.length()

		return Vec2(self.x / l, self.y / l)

	def normL(self):
		return Vec2(self.y, -self.x)

	def normR(self):
		return Vec2(-self.y, self.x)	
