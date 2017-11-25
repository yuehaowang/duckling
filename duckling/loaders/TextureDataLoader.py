from ..core.Object import Object
from ..display.TextureData import TextureData


class TextureDataLoader(Object):
	def __init__(self):
		super(TextureDataLoader, self).__init__()

		self._textureDataList = {}

	def loadOne(self, name, path, properties = {}):
		px = py = 0
		pw = ph = None

		if "x" in properties:
			px = properties["x"]
		if "y" in properties:
			py = properties["y"]
		if "width" in properties:
			pw = properties["width"]
		if "height" in properties:
			ph = properties["height"]

		texData = TextureData(None, px, py, pw, ph)
		texData.load(path)

		self._textureDataList[name] = texData

	def loadList(self, li):
		for item in li:
			props = {}

			if "properties" in item:
				props = item["properties"]

			self.loadOne(item["name"], item["path"], props)

	def get(self, name):
		try:
			return self._textureDataList[name]
		except KeyError:
			return None
		