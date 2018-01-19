import duckling as dkl
import random
class Jump():
    def __init__(self):
        super(Jump,self).__init__()
        self.barriers=[]
        self.barrier = []
        self.playing = False

        self.score = 0
        self.game = dkl.Game(660,600,"Jump")
        self.load = dkl.TextureDataLoader()
        self.load.loadList([{'name':'bird','path':'./bird'}])
        
        self.create()
        self.create_bird()
        self.create_barrier()
        self.start()
        self.game.run()
        
    def create(self):
        self.stageLayer = dkl.Sprite()
        self.game.stage.addChild(self.stageLayer)
        self.game.stage.addEventListener(dkl.KeyboardEvent.KEY_DOWN, self.onKeyDown)
        self.stageLayer.addEventListener(dkl.LoopEvent.ENTER_FRAME, self.mainLoop)

        self.scoreTex = dkl.Texture()
        self.scoreTex.x = self.scoreTex.y = 1
        self.stageLayer.addChild(self.scoreTex)
        self.updateScoreText(self.score)

    def start(self):
        self.start = False

        self.startTex = dkl.Texture(dkl.TextureData.fromText(" Please Enter 'SPACE' To Start ", size=40))
        self.startTex.x = (self.game.windowWidth - self.startTex.getWidth()) / 2
        self.startTex.y = 320
        self.stageLayer.addChild(self.startTex)
        

    def create_bird(self):
        self.bird = dkl.Texture(self.load.get('bird'))
        self.bird.x = 4
        self.bird.y = self.game.windowHeight/2
        self.stageLayer.addChild(self.bird)

    def create_barrier(self):
        for i in range(2):
            a=random.randint(120,self.game.windowHeight-120)
            for e in range(self.game.windowHeight):
                if abs(e-a)>55:
                    self.barrier.append([i*(self.game.windowWidth/2)+400,e])
            self.barriers.insert(0,self.barrier.copy())
            self.barrier.clear()
    
    def move(self):
        for i in self.barriers:
            for e in i:
                e[0]-=10
                if e[0]<=0:
                    self.barriers.pop()
                    a=random.randint(120,self.game.windowHeight-120)
                    for e in range(self.game.windowHeight):
                        if abs(e-a)>55:
                            self.barrier.append([self.game.windowWidth+10,e])
                    self.barriers.insert(0,self.barrier.copy())
                    self.barrier.clear()
                    self.updateScoreText(self.score+1)
                    break    
        self.bird.y-=8
        for i in self.barriers:
            if [self.bird.x+self.bird.getWidth()-2,self.bird.y+self.bird.getHeight()/2] in i or self.bird.y<=0 or self.bird.y>=self.game.windowHeight:
                self.gameOver() 
        
    def onKeyDown(self, e):
        d = e.data
        if d["key"] == dkl.Keyboard.ESC:
            exit(0)
        elif d["key"] == dkl.Keyboard.F5:
            self.barriers=[]
            self.barrier=[]
            self.playing = True
            self.score = 0
            self.stageLayer.removeChild(self.textTex)
            self.stageLayer.removeChild(self.bird)
            self.stageLayer.removeChild(self.hintTextTex)
            self.create_bird()
            self.create_barrier()
        if not self.playing:
            if not self.start:
                pass
            else:
                return
        if d["key"] == dkl.Keyboard.ENTER:
            self.playing = not self.playing         
        
        elif d["key"] == dkl.Keyboard.SPACE:
            if self.start == False:
                self.start = True
                self.playing = True
                self.stageLayer.removeChild(self.startTex)
            else:
                self.bird.y+=50
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
        for i in self.barriers:
            for e in i:
                self.stageLayer.graphics.drawRect(e[0] , e[1] , 1, 1, fillStyle=dkl.Color.fromHex("#FF0000"))
    def gameOver(self):
        self.playing = False
        self.textTex = dkl.Texture(dkl.TextureData.fromText("Game Over", size=80))
        self.textTex.x = (self.game.windowWidth - self.textTex.getWidth()) / 2
        self.textTex.y = 340
        self.stageLayer.addChild(self.textTex)

        self.hintTextTex = dkl.Texture(dkl.TextureData.fromText(">>Press 'F5' to restart<<", size = 40, color = dkl.Color.GREEN))
        self.hintTextTex.x = (self.game.windowWidth - self.hintTextTex.getWidth()) / 2
        self.hintTextTex.y = 260
        self.stageLayer.addChild(self.hintTextTex)
if __name__ == "__main__":
	game = Jump()				
