from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class myCheckbox(rectObj):
    def __init__(self,rect,color=Cs.white,checked=False,**kwargs):
        super().__init__(rect,color=color,**kwargs)
        self.checked = checked
        self.inner_checkmark = imageObj(Icons.CHECKMARK)
        self.inner_checkmark.setParent(self)
        self.inner_checkmark.center = self.offsetRect.center
    def toggle(self):
        self.checked = not self.checked
        if self.checked:
            self.inner_checkmark.alpha = 255
        else:
            self.inner_checkmark.alpha = 0
    def draw(self):
        super().draw()
        return

class mainScene(Scene):
    def initOnce(self):
        self.mybox = myCheckbox(pygame.Rect(0,0,100,100),color=Cs.red,checked=False)
        self.mybox.center = Rs.screenRect().center
        return
    def init(self):
        return
    def update(self):
        if Rs.userJustLeftClicked():
            if self.mybox.collideMouse():
                self.mybox.toggle()
        return
    def draw(self):
        self.mybox.draw()
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
