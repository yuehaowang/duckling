from .DisplayObject import DisplayObject
from .TextureData import TextureData


class Texture(DisplayObject):
	def __init__(self, data = None):
		super(Texture, self).__init__()

		self.textureData = data

	def _getOriginalWidth(self):
		if self.textureData != None and self.textureData.width != None:
			return self.textureData.width

		return 0

	def _getOriginalHeight(self):
		if self.textureData != None and self.textureData.height != None:
			return self.textureData.height

		return 0

	def _drawSelf(self, renderer):
		d = self.textureData

		if d == None:
			return

		renderer.drawImage(d.image, d.x, d.y, d.width, d.height)
		