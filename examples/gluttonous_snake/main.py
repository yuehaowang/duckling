import random
import duckling as dkl


class GluttonousSnake:
	def __init__(self):
		super(GluttonousSnake, self).__init__()

		self.blockSize = 16
		self.blockNum = 21

		self.snake = [(10, 10), (10, 11)]
		self.direction = 0  # 0 - up; 1 - down; 2 - right; 3 - left;
		self.length = 2

		self.target = None

		self.playing = True
		self.isGameOver = False
		self.score = 0

		self.game = dkl.Game(self.blockNum * self.blockSize, self.blockNum * self.blockSize, "Gluttonous Snake")
		self.game.fps = 6
		self.create()
		self.game.run()

	def create(self):
		self.stageLayer = dkl.Sprite()
		self.game.stage.addChild(self.stageLayer)

		self.game.stage.addEventListener(dkl.KeyboardEvent.KEY_DOWN, self.onKeyDown)
		self.stageLayer.addEventListener(dkl.LoopEvent.ENTER_FRAME, self.mainLoop)

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
			if d["key"] == dkl.Keyboard.RETURN:
				self.isGameOver = False
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
		self.snake.pop()

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

	def draw(self):
		self.stageLayer.graphics.clear()

		for y in range(self.blockNum):
			for x in range(self.blockNum):
				if (x, y) in self.snake:
					self.stageLayer.graphics.drawRect(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize, fillStyle=dkl.Color.fromHex("#333333"))
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

		textTex = dkl.Texture(dkl.TextureData.fromText("Game Over", size=50))
		textTex.x = (self.game.windowWidth - textTex.getWidth()) / 2
		textTex.y = 200
		self.stageLayer.addChild(textTex)


if __name__ == "__main__":
	game = GluttonousSnake()