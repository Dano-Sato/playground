from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class mainScene(Scene):
    h_string = "Hello World"
    time_interval = 100
    def initOnce(self):
        self.index = 0
        self.h = longTextObj("",textWidth=500)
        self.h.center = Rs.screenRect().center
        self.t = pygame.time.get_ticks()
        return
    def init(self):
        return
    def update(self):
        if pygame.time.get_ticks() - self.t > self.time_interval:
            self.t = pygame.time.get_ticks()
            self.index = min(len(self.h_string),self.index+1)
            self.h.text = self.h_string[:self.index]
            self.h.center = Rs.screenRect().center
        
        return
    def draw(self):
        self.h.draw()
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
