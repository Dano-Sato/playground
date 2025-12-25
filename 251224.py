from REMOLib import *



@dataclass
class cardData:
    name: str
    description: str
    effect: str

    def clone(self):
        return replace(self)

CARD_LIBRARY = [
    cardData(name="Card 1", description="Score + 1", effect = "score1"),
    cardData(name="Card 2", description="Score + 10", effect = "score10"),
    cardData(name="Card 3", description="Score + 100", effect = "score100"),
    cardData(name="Card 4", description="Damage 10", effect = "damage10"),
    cardData(name="Card 5", description="Damage 1 to all", effect = "damage1all"),

]

class cardWidget(rectObj):
    HEIGHT = 350
    WIDTH = 210
    def __init__(self,card:cardData,scene:"mainScene"):
        super().__init__(pygame.Rect(0,0,self.WIDTH,self.HEIGHT))
        self.card = card
        self.scene = scene
        self.nameObj = textObj(card.name,size=24,color=Cs.black)
        self.nameObj.midtop = self.offsetRect.midtop + RPoint(0,10)
        self.nameObj.setParent(self)

        self.descObj = textObj(card.description,size=16,color=Cs.black)
        self.descObj.midbottom = self.offsetRect.midbottom + RPoint(0,-10)
        self.descObj.setParent(self)

    def on_drag(self):
        self.center = Rs.mousePos() - self.parent.pos

    def on_drop(self):
        if self.center.y > 0:
            return
        if self.card.effect == "score1":
            self.scene.setScore(self.scene.getScore()+1)
        elif self.card.effect == "score10":
            self.scene.setScore(self.scene.getScore()+10)
        elif self.card.effect == "score100":
            self.scene.setScore(self.scene.getScore()+100)
        
        self.setParent(None)
            

        return


    def handle_events(self):
        Rs.dragEventHandler(self,draggedObj=self, draggingFunc=self.on_drag,
        dropFunc=self.on_drop)

#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class mainScene(Scene):
    def initOnce(self):

        self.score = 0
        self.scoreBoard = textObj("SCORE:0")
        self.scoreBoard.midtop = Rs.screenRect().midtop + RPoint(0,30)

        self.hand = cardLayout(pos=RPoint(200,700),maxWidth=1000)
        for i in range(len(CARD_LIBRARY)):
            widget = cardWidget(CARD_LIBRARY[i].clone(),self)
            widget.setParent(self.hand)

        return
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score = score
        self.scoreBoard.text = f"SCORE:{self.score}"
    def init(self):
        return
    def update(self):
        self.hand.adjustLayout()
        for widget in self.hand.getChilds():
            widget.handle_events()
            
        return
    def draw(self):
        self.scoreBoard.draw()
        self.hand.draw()
        if Rs.draggedObj:
            Rs.draggedObj.draw()
        return


class defaultScene(Scene):
    def initOnce(self):
        return
    def init(self):
        return
    def update(self):
        return
    def draw(self):
        return

class Scenes:
    mainScene = mainScene()


if __name__=="__main__":
    #Screen Setting
    window = REMOGame(window_resolution=(1920,1080),screen_size=(2560,1440),fullscreen=False,caption="DEFAULT")
    window.setCurrentScene(Scenes.mainScene)
    window.run()

    # Done! Time to quit.
