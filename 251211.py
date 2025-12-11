from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class myCard(rectObj):
    def __init__(self,rect,color=Cs.white,name="",**kwargs):
        super().__init__(rect,color=color,**kwargs)
        self.nameText = textObj(name,size=24,color=Cs.black)
        self.nameText.setParent(self)
        self.nameText.center = self.offsetRect.midtop + RPoint(0,30)
    def draw(self):
        super().draw()
        return

class myCheckbox(rectObj):
    color_picked = Cs.salmon
    color_unpicked = Cs.gray

    def __init__(self,rect,checked=True,**kwargs):
        if checked:
            color = self.color_picked
        else:
            color = self.color_unpicked
        super().__init__(rect,color=color,**kwargs)
        self.checked = checked
        self.inner_checkmark = imageObj(Icons.CHECKMARK,scale=0.9)
        self.inner_checkmark.setParent(self)
        self.inner_checkmark.center = self.offsetRect.center
    def toggle(self):
        self.checked = not self.checked
        if self.checked:
            self.inner_checkmark.alpha = 255
            self.color = self.color_picked
        else:
            self.inner_checkmark.alpha = 0
            self.color = self.color_unpicked
    def draw(self):
        super().draw()
        return

class mainScene(Scene):
    def initOnce(self):
        self.cards: list[myCard] = []
        self.checkboxes: list[myCheckbox] = []
        for i in range(5):
            card = myCard(pygame.Rect(0,0,200,300),color=Cs.yellow,name=f"My Card {i+1}")
            checkbox = myCheckbox(pygame.Rect(0,0,100,100))
            card.center = RPoint(300 + i*220, Rs.screenRect().centery - 200)
            checkbox.midtop = card.midbottom + RPoint(0,20)
            self.cards.append(card)
            self.checkboxes.append(checkbox)
        return
    def init(self):
        return
    def update(self):

        if Rs.userJustLeftClicked():
            for checkbox in self.checkboxes:
                if checkbox.collideMouse():
                    checkbox.toggle()
                    print(f"Checked status: {[cb.checked for cb in self.checkboxes]}")
    def draw(self):
        for card in self.cards:
            card.draw()
        for checkbox in self.checkboxes:
            checkbox.draw()
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
