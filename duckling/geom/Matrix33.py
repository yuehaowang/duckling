import math

from ..core.Object import Object


class Matrix33(Object):
	def __init__(self, a = 1, b = 0, c = 0, d = 0, e = 1, f = 0, g = 0, h = 0, i = 1):
		super(Matrix33, self).__init__()

		self.setTo(a, b, c, d, e, f, g, h, i)

	def clone(self):
		return Matrix33(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i)

	def setTo(self, a, b, c, d, e, f, g, h, i):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
		self.f = f
		self.g = g
		self.h = h
		self.i = i

	def rotate(self, angle):
		rad = angle * math.pi / 180

		c = math.cos(rad)
		s = math.sin(rad)

		m = Matrix33(c, -s, 0, s, c, 0, 0, 0, 1)
		self.add(m)

	def translate(self, dx, dy):
		m = Matrix33(1, 0, dx, 0, 1, dy, 0, 0, 1)
		self.add(m)

	def scale(self, sx, sy):
		m = Matrix33(sx, 0, 0, 0, sy, 0, 0, 0, 1)
		self.add(m)

	def add(self, m):
		a = m.a * self.a + m.b * self.d + m.c * self.g
		b = m.a * self.b + m.b * self.e + m.c * self.h
		c = m.a * self.c + m.b * self.f + m.c * self.i
		d = m.d * self.a + m.e * self.d + m.f * self.g
		e = m.d * self.b + m.e * self.e + m.f * self.h
		f = m.d * self.c + m.e * self.f + m.f * self.i
		g = m.g * self.a + m.h * self.d + m.i * self.g
		h = m.g * self.b + m.h * self.e + m.i * self.h
		i = m.g * self.c + m.h * self.f + m.i * self.i

		self.setTo(a, b, c, d, e, f, g, h, i)

	def toArray(self, a):
		na0 = self.a * a[0] + self.b * a[1] + self.c * a[2]
		na1 = self.d * a[0] + self.e * a[1] + self.f * a[2]
		na2 = self.g * a[0] + self.h * a[1] + self.i * a[2]

		return [na0, na1, na2]

	def __str__(self):
		return "Matrix33(\n  %s %s %s\n  %s %s %s\n  %s %s %s\n)" % (self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i)

	__repr__ = __str__
