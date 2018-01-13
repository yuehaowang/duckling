import platform

from PIL import Image as PILImage, ImageFont as PILImageFont, ImageDraw as PILImageDraw

from ..core.Object import Object
from .Color import Color


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

	@staticmethod
	def fromText(text, *, size = 12, font = None, color = Color()):
		if font == None:
			os = platform.system()

			if os == "Windows":
				font = "msyh.ttc"
			elif os == "Darwin":
				font = "Arial Unicode.ttf"
			elif os == "Linux":
				font = "fonts-japanese-gothic.ttf"

		imgFont = PILImageFont.truetype(font, size)

		img = PILImage.new("RGBA", imgFont.getsize(text), (0, 0, 0, 0))

		imgDraw = PILImageDraw.Draw(img)
		imgDraw.text((0, 0), text, font = imgFont, fill=(0, 0, 0, 255))

		return TextureData(img.transpose(PILImage.FLIP_TOP_BOTTOM))

	def load(self, path):
		self.image = PILImage.open(path).convert("RGBA").transpose(PILImage.FLIP_TOP_BOTTOM)

		size = self.image.size
		if self.width == None or self.width < 0:
			self.width = size[0]
		if self.height == None or self.height < 0:
			self.height = size[1]
		