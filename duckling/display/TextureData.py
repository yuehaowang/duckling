import PIL

from ..core.Object import Object


class TextureData(Object):
	def __init__(self, img = None, x = 0, y = 0, width = None, height = None):
		super(TextureData, self).__init__()

		if img != None:
			if width == None:
				width = img.size[0]

			if height == None:
				height = img.size[1]

		self.image = img
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def load(self, path):
		self.image = PIL.Image.open(path).convert("RGBA").transpose(PIL.Image.FLIP_TOP_BOTTOM)

		size = self.image.size
		if self.width == None or self.width < 0:
			self.width = size[0]
		if self.height == None or self.height < 0:
			self.height = size[1]
		