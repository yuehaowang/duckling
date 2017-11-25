from .DisplayObject import DisplayObject
from .TextureData import TextureData


class Texture(DisplayObject):
	def __init__(self, data = None):
		super(Texture, self).__init__()

		self.textureData = data

	def _drawSelf(self, renderer):
		d = self.textureData

		if d == None:
			return

		renderer.drawImage(d.image, d.x, d.y, d.width, d.height)
		