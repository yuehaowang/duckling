# -*- coding: utf-8 -*-

import duckling as dkl


def onClick(e):
	dkl.log("Click %s" % e.currentTarget.name)

def onMouseMove(e):
	dkl.log("Mouse moves on %s" % e.currentTarget.name)

def demoInit():
	# green layer
	layer1 = dkl.Sprite()
	layer1.x = 200
	layer1.y = 200
	layer1.name = "Green Layer"
	layer1.graphics.drawRect(0, 0, 150, 150, fillStyle = dkl.Color.GREEN, strokeStyle = dkl.Color.DARK_GREEN, lineWidth = 3)
	layer1.addEventListener(dkl.MouseEvent.MOUSE_DOWN, onClick)
	game.stage.addChild(layer1)

	# orange layer
	layer2 = dkl.Sprite()
	layer2.x = 100
	layer2.y = 100
	layer2.name = "Orange Layer"
	layer2.graphics.drawRect(0, 0, 150, 150, fillStyle = dkl.Color.ORANGE, strokeStyle = dkl.Color.ORANGE_RED, lineWidth = 3)
	layer2.addEventListener(dkl.MouseEvent.MOUSE_DOWN, onClick)
	game.stage.addChild(layer2)

	# blue layer
	layer3 = dkl.Sprite()
	layer3.mouseShelter = False
	layer3.x = 300
	layer3.y = 100
	layer3.name = "Blue Layer"
	layer3.graphics.drawRect(0, 0, 150, 150, fillStyle = dkl.Color.fromHex("#00BFFF"), strokeStyle = dkl.Color.fromHex("#4169E1"), lineWidth = 3)
	layer3.addEventListener(dkl.MouseEvent.MOUSE_DOWN, onClick)
	layer3.addEventListener(dkl.MouseEvent.MOUSE_MOVE, onMouseMove)
	game.stage.addChild(layer3)

if __name__ == "__main__":
	game = dkl.Game(570, 450, "Mouse Event Demo")
	demoInit()
	game.run()
