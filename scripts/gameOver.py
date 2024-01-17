#parte 3
from scripts.animatedBg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.text import Text
import pygame

class GameOver(Scene):
    def __init__(self):
        super().__init__()
        # depois iremos remover:
        self.bg = AnimatedBg("assets/menu/bg.png",[0,0], [0,-720], [self.all_sprites])
        self.title = Text("assets/fonts/airstrike.ttf", 50, "Game Over", "white", [490, 300])


    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False


    def update(self):
        self.bg.update()
        self.title.draw()
        return super().update()