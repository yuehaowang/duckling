import duckling as dkl


class CollisionDetection:
	def __init__(self):
		self.game = dkl.Game(800, 600, "Collision Detection")
		self.create()
		self.game.run()

	def create(self):
		self.mainLayer = dkl.Sprite()
		self.mainLayer.graphics.drawRect(0, 0, self.game.windowWidth, self.game.windowHeight, fillStyle = dkl.Color.TRANSPARENT)  # draw a transparent background
		self.game.stage.addChild(self.mainLayer)

		self.mainLayer.addEventListener(dkl.MouseEvent.MOUSE_MOVE, self.onMouseMove)
		self.mainLayer.addEventListener(dkl.MouseEvent.MOUSE_UP, self.stopDrag)

		self.dragTarget = None
		self.preMousePos = None

		self.createShapes()

	def onMouseMove(self, e):
		if self.dragTarget == None or self.preMousePos == None:
			return

		self.dragTarget.x += e.data["mouseX"] - self.preMousePos[0]
		self.dragTarget.y += e.data["mouseY"] - self.preMousePos[1]

		self.preMousePos = (e.data["mouseX"], e.data["mouseY"])

		for child in self.mainLayer.childList:
			if child.objectIndex != self.dragTarget.objectIndex and child.hitTestObject(self.dragTarget):
				dkl.log("%s and %s collide." % (child.name, self.dragTarget.name))

	def startDrag(self, e):
		self.dragTarget = e.currentTarget
		self.preMousePos = (e.data["mouseX"], e.data["mouseY"])

	def stopDrag(self, e):
		self.dragTarget = None
		self.preMousePos = None

	def createShapes(self):
		fillColor = dkl.Color.fromHex("#EAEAEA")
		strokeColor = dkl.Color.fromHex("#0000EE")

		fillColor.a = 0.5

		sh1 = dkl.Sprite()
		sh1.x = 100
		sh1.y = 100
		sh1.rotation = 30
		sh1.name = "Rect"
		sh1.graphics.drawRect(-50, -50, 100, 100, fillStyle = fillColor, strokeStyle = strokeColor, lineWidth = 3)
		sh1.addShapes(sh1.getVisualShapes())
		sh1.addEventListener(dkl.MouseEvent.MOUSE_DOWN, self.startDrag)
		self.mainLayer.addChild(sh1)

		sh2 = dkl.Sprite()
		sh2.x = 250
		sh2.y = 200
		sh2.name = "Circle"
		sh2.graphics.drawArc(0, 0, 50, fillStyle = fillColor, strokeStyle = strokeColor, lineWidth = 3)
		sh2.addShapes(sh2.getVisualShapes())
		sh2.addEventListener(dkl.MouseEvent.MOUSE_DOWN, self.startDrag)
		self.mainLayer.addChild(sh2)

		sh3 = dkl.Sprite()
		sh3.x = 400
		sh3.y = 150
		sh3.name = "Polygon"
		sh3.graphics.drawVertices([dkl.Point2D(-30, -30), dkl.Point2D(-60, 0), dkl.Point2D(-10, 80), dkl.Point2D(60, 60), dkl.Point2D(90, 10), dkl.Point2D(10, -50)], fillStyle = fillColor, strokeStyle = strokeColor, lineWidth = 3)
		sh3.addShapes(sh3.getVisualShapes())
		sh3.addEventListener(dkl.MouseEvent.MOUSE_DOWN, self.startDrag)
		self.mainLayer.addChild(sh3)


if __name__ == "__main__":
	CollisionDetection()
