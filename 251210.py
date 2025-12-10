from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class mainScene(Scene):
    def initOnce(self):
        self.a = rectObj(pygame.Rect(0,0,100,100),color=Cs.red)
        self.a.center = Rs.screenRect().center
        
        return
    def init(self):
        return
    def update(self):
        if Rs.userJustLeftClicked():
            self.a.color=Cs.blue
            self.a.easeout(["center","color"],[Rs.mousePos(),Cs.red])

        return
    def draw(self):
        self.a.draw()
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
