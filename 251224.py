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
    cardData(name="Card 3", description="Score + 100", effect = "score100")

]

class cardWidget(rectObj):
    HEIGHT = 350
    WIDTH = 210
    def __init__(self,card:cardData):
        super().__init__(pygame.Rect(0,0,self.WIDTH,self.HEIGHT))
        self.card = card
        self.nameObj = textObj(card.name,size=24,color=Cs.black)
        self.nameObj.midtop = self.offsetRect.midtop + RPoint(0,10)
        self.nameObj.setParent(self)

        self.descObj = textObj(card.description,size=16,color=Cs.black)
        self.descObj.midbottom = self.offsetRect.midbottom + RPoint(0,-10)
        self.descObj.setParent(self)

#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class mainScene(Scene):
    def initOnce(self):
        self.a = textObj("New game")
        self.a.midtop = Rs.screenRect().midtop + RPoint(0,30)

        hand = []
        self.hand = cardLayout(pos=RPoint(100,700),maxWidth=1000)
        for i in range(len(CARD_LIBRARY)):
            widget = cardWidget(CARD_LIBRARY[i].clone())
            widget.setParent(self.hand)

        return
    def init(self):
        return
    def update(self):
        self.hand.adjustLayout()
        return
    def draw(self):
        self.a.draw()
        self.hand.draw()
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
