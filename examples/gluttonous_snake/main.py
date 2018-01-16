import random
import duckling as dkl


class GluttonousSnake:
	def __init__(self):
		self.blockSize = 16
		self.blockNum = 21

		self.game = dkl.Game(self.blockNum * self.blockSize, self.blockNum * self.blockSize, "Gluttonous Snake")
		self.game.fps = 6
		self.create()
		self.game.run()

	def create(self):
		self.score = 0
		self.playing = True
		self.isGameOver = False

		self.target = None

		self.snake = [(10, 10), (10, 9)]
		self.direction = 0  # 0 - up; 1 - down; 2 - right; 3 - left;

		self.initLayers()
		self.initEvents()
		self.initScoreTex()

	def initLayers(self):
		self.stageLayer = dkl.Sprite()
		self.game.stage.addChild(self.stageLayer)

	def initEvents(self):
		self.game.stage.addEventListener(dkl.KeyboardEvent.KEY_DOWN, self.onKeyDown)
		self.stageLayer.addEventListener(dkl.LoopEvent.ENTER_FRAME, self.mainLoop)

	def initScoreTex(self):
		self.scoreTex = dkl.Texture()
		self.scoreTex.x = self.scoreTex.y = 10
		self.stageLayer.addChild(self.scoreTex)

		self.updateScoreText(self.score)

	def onKeyDown(self, e):
		d = e.data

		if d["key"] == dkl.Keyboard.ESC:
			exit(0)
		elif d["key"] == dkl.Keyboard.SPACE:
			self.playing = not self.playing

		if self.isGameOver:
			if d["key"] == dkl.Keyboard.ENTER:
				self.game.stage.destroy()
				self.create()

		if self.playing:
			if d["key"] == dkl.Keyboard.UP:
				self.direction = 0
			elif d["key"] == dkl.Keyboard.DOWN:
				self.direction = 1
			elif d["key"] == dkl.Keyboard.RIGHT:
				self.direction = 2
			elif d["key"] == dkl.Keyboard.LEFT:
				self.direction = 3

	def mainLoop(self, e):
		if not self.playing:
			return

		self.addFood()
		self.moveSnake()
		self.draw()

	def addFood(self):
		if self.target == None:
			while True:
				self.target = (random.randint(0, self.blockSize - 1), random.randint(0, self.blockSize - 1))

				if not self.target in self.snake:
					break

	def moveSnake(self):
		tx = self.snake[0][0]
		ty = self.snake[0][1]

		if self.direction == 0:
			ty += 1
		elif self.direction == 1:
			ty -= 1
		elif self.direction == 2:
			tx += 1
		elif self.direction == 3:
			tx -= 1

		if tx < 0 or tx >= self.blockNum or ty < 0 or ty >= self.blockNum or (tx, ty) in self.snake:
			self.gameOver()
			return
		elif self.target != None and tx == self.target[0] and ty == self.target[1]:
			self.eatFood()

		self.snake.insert(0, (tx, ty))
		self.snake.pop()

	def draw(self):
		self.stageLayer.graphics.clear()

		for y in range(self.blockNum):
			for x in range(self.blockNum):
				if (x, y) in self.snake:
					self.stageLayer.graphics.drawRect(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize, fillStyle=dkl.Color.fromHex("#AAAAAA"))
				elif self.target != None and self.target[0] == x and self.target[1] == y:
					self.stageLayer.graphics.drawRect(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize, fillStyle=dkl.Color.fromHex("#FF0000"))

	def eatFood(self):
		self.target = None
		self.updateScoreText(self.score + 1)

		tx = self.snake[-1][0]
		ty = self.snake[-1][1]

		if self.direction == 0:
			ty -= 1
		elif self.direction == 1:
			ty += 1
		elif self.direction == 2:
			tx -= 1
		elif self.direction == 3:
			tx += 1

		self.snake.append((tx, ty))

	def updateScoreText(self, p):
		self.score = p
		self.scoreTex.textureData = dkl.TextureData.fromText("Score: %s" % self.score, size=20)

	def gameOver(self):
		self.playing = False
		self.isGameOver = True

		titleTextTex = dkl.Texture(dkl.TextureData.fromText("Game Over", size=50))
		titleTextTex.x = (self.game.windowWidth - titleTextTex.getWidth()) / 2
		titleTextTex.y = 200
		self.stageLayer.addChild(titleTextTex)

		hintTextTex = dkl.Texture(dkl.TextureData.fromText(">>Press 'ENTER' to restart<<", size=20))
		hintTextTex.x = (self.game.windowWidth - hintTextTex.getWidth()) / 2
		hintTextTex.y = 140
		self.stageLayer.addChild(hintTextTex)


if __name__ == "__main__":
	game = GluttonousSnake()
