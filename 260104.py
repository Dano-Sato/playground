from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

@dataclass
class JyankenCard:
    name: str
    description: str
    effect: str
    lv: int
    power: int

    def clone(self):
        return replace(self)

class cardWidget(rectObj):
    def __init__(self,card:JyankenCard,scene:"mainScene"):
        super().__init__(pygame.Rect(0,0,200,300))
        self.card = card
        self.scene = scene
        self.nameObj = textObj(card.name,size=24,color=Cs.black)
        self.nameObj.setParent(self)
        self.nameObj.center = self.offsetRect.midtop + RPoint(0,30)
        self.descriptionObj = textObj(card.description,size=16,color=Cs.black)
        self.descriptionObj.setParent(self)
        self.descriptionObj.midbottom = self.offsetRect.midbottom + RPoint(0,-30)
        self.fliped = False
        return
    def on_drag(self):
        self.center = Rs.mousePos() - self.parent.pos
    def on_drop(self):
        self.flip()
        return
    def draw(self):
        super().draw()
        return
    def handle_events(self):
        Rs.dragEventHandler(self,draggedObj=self, draggingFunc=self.on_drag,
        dropFunc=self.on_drop)
    def flip(self):
        self.fliped = not self.fliped
        if self.fliped:
            self.nameObj.alpha = 0
            self.descriptionObj.alpha = 0
            self.color = Cs.brown
        else:
            self.nameObj.alpha = 255
            self.descriptionObj.alpha = 255
            self.color = Cs.white
        return


class mainScene(Scene):
    def initOnce(self):
        self.jyankenCards = [JyankenCard(name="Rock",description="Rock",effect="Rock",lv=1),
                             JyankenCard(name="Paper",description="Paper",effect="Paper",lv=1),
                             JyankenCard(name="Scissors",description="Scissors",effect="Scissors",lv=1)]
        self.cardWidgets = [cardWidget(card,self) for card in self.jyankenCards]
        self.cardLayout = cardLayout(pos=RPoint(0,0),isVertical=False,maxWidth=1000)
        for widget in self.cardWidgets:
            widget.setParent(self.cardLayout)
        self.cardLayout.center = Rs.screenRect().center + RPoint(0,300)

        self.enemyCard = cardWidget(JyankenCard(name="Rock",description="Rock",effect="Rock",lv=1),self)
        self.enemyCard.center = Rs.screenRect().center - RPoint(0,400)
        return
    def init(self):
        return
    def update(self):
        self.cardLayout.adjustLayout()
        for widget in self.cardWidgets:
            widget.handle_events()
        return
    def draw(self):
        self.cardLayout.draw()
        self.enemyCard.draw()
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
