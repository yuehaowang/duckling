from ..core.Object import Object


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

	def clone(self):
		return Color(self.r, self.g, self.b, self.a)

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

Color.WHITE = Color.fromHex("#FFFFFF")
Color.BLACK = Color.fromHex("#000000")
Color.RED = Color.fromHex("#FF0000")
Color.DARK_RED = Color.fromHex("#800000")
Color.GREEN = Color.fromHex("#00FF00")
Color.DARK_GREEN = Color.fromHex("#008000")
Color.BLUE = Color.fromHex("#0000FF")
Color.DARK_BLUE = Color.fromHex("#000080")
Color.CYAN = Color.fromHex("#00FFFF")
Color.DARK_CYAN = Color.fromHex("#008080")
Color.MAGENTA = Color.fromHex("#FF00FF")
Color.DARK_MAGENTA = Color.fromHex("#800080")
Color.YELLOW = Color.fromHex("#FFFF00")
Color.DARK_YELLOW = Color.fromHex("#808000")
Color.GRAY = Color.fromHex("#A0A0A4")
Color.DARK_GRAY = Color.fromHex("#808080")
Color.LIGHT_GRAY = Color.fromHex("#C0C0C0")
Color.ORANGE = Color.fromHex("#FFA500")
Color.DARK_ORANGE = Color.fromHex("#FF8C00")
Color.ORANGE_RED = Color.fromHex("#FF4500")
Color.PURPLE = Color.fromHex("#800080")
Color.DARK_PURPLE = Color.fromHex("#663399")
Color.TRANSPARENT = Color(0, 0, 0, 0)
