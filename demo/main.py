# -*- coding: utf-8 -*-

import duckling as dkl


class GameTest:
	def __init__(self):
		super(GameTest, self).__init__()
		
		self.game = dkl.Game(800, 600, "Test")
		self.create()
		self.game.run()

	def create(self):
		## Draw shapes: rectangle, circle, triangle

		layer = dkl.Sprite()
		layer.x = 50
		layer.y = 300
		layer.graphics.drawRect(0, 0, 150, 150, fillStyle = dkl.Color.fromHex("#00EE00"), strokeStyle = dkl.Color.fromHex("#009900"), lineWidth = 5)
		layer.graphics.drawArc(275, 75, 75, fillStyle = dkl.Color.fromHex("#EE0000"), strokeStyle = dkl.Color.fromHex("#990000"), lineWidth = 5)
		layer.graphics.drawVertices([dkl.Point2D(400, 0), dkl.Point2D(475, 150), dkl.Point2D(550, 0)], fillStyle = dkl.Color.fromHex("#0000EE"), strokeStyle = dkl.Color.fromHex("#000099"), lineWidth = 5)
		self.game.stage.addChild(layer)

		def moveShapes(e):
			e.currentTarget.x += 1

		layer.addEventListener(dkl.Event.ENTER_FRAME, moveShapes)


		## Load and display images

		loader = dkl.TextureDataLoader()
		loader.loadList([
			{"name" : "yaxi_logo", "path" : "./yaxi_logo.png"},
			{"name" : "avatar", "path" : "./avatar.png"}
		])
		
		tex1 = dkl.Texture(loader.get("avatar"))
		tex1.x = tex1.y = 30
		tex1.textureData.x = tex1.textureData.y = 30
		tex1.textureData.width = tex1.textureData.height = 100
		self.game.stage.addChild(tex1)

		tex2 = dkl.Texture(loader.get("yaxi_logo"))
		tex2.x = 360
		tex2.y = 30
		tex2.rotation = 30
		self.game.stage.addChild(tex2)


		## Display text field

		textTexData = dkl.TextureData.fromText("Hello World! 你好世界！こんにちは世界！")
		textTex = dkl.Texture(textTexData)
		textTex.x = 50
		textTex.y = 500
		textTex.scaleX = 1.5
		textTex.scaleY = 1.6
		self.game.stage.addChild(textTex)



if __name__ == "__main__":
	game = GameTest()
