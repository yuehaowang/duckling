import duckling as dkl
import random
class Jump():
    def __init__(self):
        super(Jump,self).__init__()
        self.blockSize = 18
        self.blockNum = 20
        self.barriers=[]
        self.barrier = []
        self.playing = True
        self.score = 0
        self.block = [4,self.blockNum/2]


        self.game = dkl.Game(self.blockNum * self.blockSize, self.blockNum * self.blockSize, "Jump")
        self.game.fps = 8
        self.create()
        self.create_barrier()
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
    def create_barrier(self):
        for i in range(5):
            a=random.randint(3,self.blockNum-3)
            for e in range(self.blockNum):
                if abs(e-a)>2:
                    self.barrier.append([i*10+18,e])
            self.barriers.insert(0,self.barrier.copy())
            self.barrier.clear()
    
    def move(self):
        for i in self.barriers:
            for e in i:
                e[0]-=1
                if e[0]==1:
                    self.barriers.pop()
                    a=random.randint(6,self.blockNum-6)
                    for e in range(self.blockNum):
                        if abs(e-a)>2:
                            self.barrier.append([51,e])
                    self.barriers.insert(0,self.barrier.copy())
                    self.barrier.clear()
                    self.updateScoreText(self.score+1)
                    break    
        self.block[1]-=1
        tx=self.block[0]
        ty=self.block[1]
        for i in self.barriers:
            if [tx,ty] in i or ty<=0 or ty>=self.blockNum:
                self.gameOver() 
        
    def onKeyDown(self, e):
        d = e.data
        if d["key"] == dkl.Keyboard.ESC:
            exit(0)
        elif d["key"] == dkl.Keyboard.ENTER:
            self.playing = not self.playing         
        elif d["key"] == dkl.Keyboard.F5:
            self.barriers=[]
            self.barrier=[]
            self.playing = True
            self.score = 0
            self.block = [2,self.blockNum/2]
            self.stageLayer.removeChild(self.textTex)
            self.create_barrier()
        elif d["key"] == dkl.Keyboard.SPACE:
            self.block[1]+=2
    def updateScoreText(self, p):
        self.score = p
        self.scoreTex.textureData = dkl.TextureData.fromText("Score: %s" % self.score, size=20)
    def mainLoop(self, e):
        if not self.playing:
            return

        self.move()

        self.draw()
        
    def draw(self):
        self.stageLayer.graphics.clear()
        for y in range(self.blockNum):
            for x in range(self.blockNum):
                if [x, y] == self.block:
                    self.stageLayer.graphics.drawRect(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize, fillStyle=dkl.Color.fromHex("#333333"))
                for i in self.barriers:
                    if [x,y] in i:
                        self.stageLayer.graphics.drawRect(x * self.blockSize, y * self.blockSize, 5, self.blockSize, fillStyle=dkl.Color.fromHex("#FF0000"))
    def gameOver(self):
        self.playing = False
        self.textTex = dkl.Texture(dkl.TextureData.fromText("Game Over", size=50))
        self.textTex.x = (self.game.windowWidth - self.textTex.getWidth()) / 2
        self.textTex.y = 200
        self.stageLayer.addChild(self.textTex)
if __name__ == "__main__":
	game = Jump()				
