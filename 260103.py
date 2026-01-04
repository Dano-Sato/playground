from REMOLib import *






#게임 오브젝트들을 선언하는 곳입니다.
class Obj:
    None

class mainScene(Scene):
    def initOnce(self):
        self.h = imageObj(Icons.SUIT_HEARTS)
        self.h.center = Rs.screenRect().center

        self.player = rectObj(pygame.Rect(0,0,100,100),color=Cs.red)
        self.player.center = Rs.screenRect().center - RPoint(0,100)
        self.player_heart_container = layoutObj(pos=RPoint(0,-50),isVertical=False,spacing=5)
        self.player_heart_container.setParent(self.player)
        self.player_hearts = 3
        self.player_hearts_images = [imageObj(Icons.SUIT_HEARTS,scale=0.4) for _ in range(self.player_hearts)]
        for i in range(self.player_hearts):
            self.player_hearts_images[i].setParent(self.player_heart_container)
            self.player_hearts_images[i].colorize(Cs.red)
        self.player_heart_container.adjustBoundary()
        self.player_heart_container.center = RPoint(self.player.width//2,-30)
        return
    def init(self):
        return
    def gainHeart(self,amount=1):
        self.player_hearts += amount
        self.player_hearts_images.append(imageObj(Icons.SUIT_HEARTS,scale=0.4))
        self.player_hearts_images[-1].setParent(self.player_heart_container)
        self.player_hearts_images[-1].colorize(Cs.red)
        self.player_heart_container.adjustBoundary()
        self.player_heart_container.center = RPoint(self.player.width//2,-30)
        return
    def loseHeart(self,amount=1):
        if self.player_hearts <= 0:
            return
        self.player_hearts -= amount
        self.player_hearts_images.pop().setParent(None)
        self.player_heart_container.adjustBoundary()
        self.player_heart_container.center = RPoint(self.player.width//2,-30)
        return
    def update(self):
        if Rs.userJustPressed(pygame.K_z):
            self.gainHeart()
        if Rs.userJustPressed(pygame.K_x):
            self.loseHeart()
        if Rs.userPressing(pygame.K_LEFT):
            self.player.pos = self.player.pos - RPoint(10,0)
        if Rs.userPressing(pygame.K_RIGHT):
            self.player.pos = self.player.pos + RPoint(10,0)
        if Rs.userPressing(pygame.K_UP):
            self.player.pos = self.player.pos - RPoint(0,10)
        if Rs.userPressing(pygame.K_DOWN):
            self.player.pos = self.player.pos + RPoint(0,10)
        return
    def draw(self):
        self.h.draw()
        self.player.draw()
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
