from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class mainScene(Scene):
    def initOnce(self):
        self.p = rectObj(pygame.Rect(0,0,100,100),color=Cs.red)
        self.p.center = Rs.screenRect().center
        self.score = textObj("0",size=44,color=Cs.white)
        self.score.midtop = Rs.screenRect().midtop + RPoint(0,50)
        return
    def getScore(self):
        return int(self.score.text)
    def setScore(self,score):
        self.score.text = str(score)
    def init(self):
        return
    def update(self):
        if Rs.userJustLeftClicked():
            self.p.color = Cs.blue
            self.p.easeout(["center","color"],[Rs.mousePos(),Cs.red])
            self.setScore(self.getScore() + 1)
        return
    def draw(self):
        self.p.draw()
        self.score.draw()
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
