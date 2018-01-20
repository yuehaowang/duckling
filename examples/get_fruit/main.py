import random
import duckling as dkl


class GetFruit:
	def __init__(self):
		self.game = dkl.Game(800, 600, "Get Fruit")
		self.loadRes()
		self.create()
		self.game.run()

	def loadRes(self):
		self.loader = dkl.TextureDataLoader()
		self.loader.loadList([
			{"name": "bg", "path": "./images/back.jpg"},
			{"name": "player", "path": "./images/player.png"},
			{"name": "item0", "path": "./images/item0.png"},
			{"name": "item1", "path": "./images/item1.png"},
			{"name": "item2", "path": "./images/item2.png"},
			{"name": "item3", "path": "./images/item3.png"},
			{"name": "item4", "path": "./images/item4.png"},
			{"name": "item5", "path": "./images/item5.png"},
			{"name": "item6", "path": "./images/item6.png"},
			{"name": "item7", "path": "./images/item7.png"}
		])

	def create(self):
		self.score = 0

		self.addItemIndex = 0
		self.addItemSpeed = 100

		self.playing = True

		self.initLayers()
		self.initEvents()

	def initLayers(self):
		self.stageLayer = dkl.Sprite()
		self.game.stage.addChild(self.stageLayer)

		self.addBg()
		self.addPlayer()
		self.initScoreTex()

		self.itemLayer = dkl.Sprite()
		self.stageLayer.addChild(self.itemLayer)

	def initEvents(self):
		self.game.stage.addEventListener(dkl.KeyboardEvent.KEY_DOWN, self.onKeyDown)
		self.game.stage.addEventListener(dkl.KeyboardEvent.KEY_UP, self.onKeyUp)

		self.stageLayer.addEventListener(dkl.LoopEvent.ENTER_FRAME, self.mainLoop)

	def initScoreTex(self):
		self.scoreTex = dkl.Texture()
		self.scoreTex.x = 20
		self.scoreTex.y = self.game.windowHeight - 50
		self.stageLayer.addChild(self.scoreTex)

		self.updateScoreText(self.score)

	def updateScoreText(self, p):
		self.score = p
		self.scoreTex.textureData = dkl.TextureData.fromText("Score: %s" % self.score, color = dkl.Color.RED, size = 25)

	def addBg(self):
		bgTex = dkl.Texture(self.loader.get("bg"))
		self.stageLayer.addChild(bgTex)

	def addPlayer(self):
		self.player = Player(self.loader.get("player"))
		self.player.x = self.game.windowWidth / 2
		self.player.y = 65
		self.stageLayer.addChild(self.player)

	def onKeyDown(self, e):
		if e.data["key"] == dkl.Keyboard.ESC:
			self.game.exit()

		if self.playing:
			if e.data["key"] == dkl.Keyboard.RIGHT:
				self.player.changeDirection(1)
			elif e.data["key"] == dkl.Keyboard.LEFT:
				self.player.changeDirection(-1)
		else:
			if e.data["key"] == dkl.Keyboard.ENTER:
				self.stageLayer.destroy()
				self.create()

	def onKeyUp(self, e):
		if self.playing:
			self.player.changeDirection(0)

	def mainLoop(self, e):
		if not self.playing:
			return

		self.addItemIndex += 1

		if self.addItemIndex > self.addItemSpeed:
			index = random.randint(0, 7)

			item = Item(self.loader.get("item%s" % index), index)
			item.x = random.randint(50, self.game.windowWidth -50)
			item.y = self.game.windowHeight + 50
			self.itemLayer.addChild(item)

			self.addItemIndex = 0

		self.player.mainLoop()

		if self.player.x < 50:
			self.player.x = 50
		elif self.player.x > self.game.windowWidth - 50:
			self.player.x = self.game.windowWidth - 50

		for child in self.itemLayer.childList:
			if self.detectCollision(child):
				if child.index < 4:
					self.updateScoreText(self.score + 1)

					child.remove()
					continue
				else:
					self.gameOver()
					break

			child.mainLoop()

	def detectCollision(self, item):
		r = ((item.x - self.player.x) ** 2 + (item.y - self.player.y) ** 2) ** 0.5

		return r < (self.player.getWidth() + item.getWidth()) / 2

	def gameOver(self):
		self.playing = False

		titleTextTex = dkl.Texture(dkl.TextureData.fromText("Game Over", size = 70, color = dkl.Color.RED))
		titleTextTex.x = (self.game.windowWidth - titleTextTex.getWidth()) / 2
		titleTextTex.y = 340
		self.stageLayer.addChild(titleTextTex)

		hintTextTex = dkl.Texture(dkl.TextureData.fromText(">>Press 'ENTER' to restart<<", size = 30, color = dkl.Color.ORANGE))
		hintTextTex.x = (self.game.windowWidth - hintTextTex.getWidth()) / 2
		hintTextTex.y = 240
		self.stageLayer.addChild(hintTextTex)

class Player(dkl.Sprite):
	def __init__(self, img):
		super(Player, self).__init__()

		self.direction = 0

		self.animaCol = 0
		self.animaRow = 3

		self.nextFrameIndex = 0
		self.nextFrameSpeed = 5

		self.tex = dkl.Texture(img)
		self.tex.x = -32
		self.tex.y = -32
		self.tex.textureData.y = self.animaRow * 64
		self.tex.textureData.width = 64
		self.tex.textureData.height = 64
		self.addChild(self.tex)

	def changeDirection(self, direction):
		if direction == 0:
			self.animaRow = 3
		elif direction == -1:
			self.animaRow = 2
		elif direction == 1:
			self.animaRow = 1

		self.direction = direction

	def mainLoop(self):
		self.nextFrameIndex += 1

		if self.nextFrameIndex > self.nextFrameSpeed:
			self.animaCol += 1

			if self.animaCol > 3:
				self.animaCol = 0

			self.tex.textureData.x = self.animaCol * 64
			self.tex.textureData.y = self.animaRow * 64

			self.nextFrameIndex = 0

		self.x += self.direction * 2

class Item(dkl.Sprite):
	def __init__(self, img, index):
		super(Item, self).__init__()

		self.index = index

		self.tex = dkl.Texture(img)
		self.tex.x = -32
		self.tex.y = -32
		self.addChild(self.tex)

	def mainLoop(self):
		self.y -= 2

		if self.y < -40:
			self.remove()


if __name__ == '__main__':
	GetFruit()
