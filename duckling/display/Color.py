class Color(object):
	def __init__(self, r = 0, g = 0, b = 0, a = 1):
		super(Color, self).__init__()

		self.set(r, g, b, a)

	def set(self, r = 0, g = 0, b = 0, a = 1):
		self.r = r
		self.g = g
		self.b = b
		self.a = a

	def toList(self):
		return [self.r, self.g, self.b, self.a]

	@staticmethod
	def fromHex(s):
		if len(s) <= 1 or s[0] != "#" or (not len(s[1:]) in (3, 6, 4, 8)):
			return Color()

		s = s[1:]
		i, l = 0, len(s)
		rgba = []

		while i < l:
			channelVal = s[i:i + 2] if l in (6, 8) else (s[i] + s[i])

			rgba.append(int(channelVal, base = 16) / 255)

			if l in (3, 4):
				i += 1
			else:
				i += 2

		if l in (3, 6):
			rgba.append(1)

		return Color(*rgba)
