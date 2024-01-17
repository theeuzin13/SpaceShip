import pygame, sys
from scripts.scene import Scene
from scripts.menu import Menu
from scripts.game import Game
from scripts.gameOver import GameOver
from scripts.settings import *

class StartGame:

    def __init__(self):

        #padrão iniciar font, som e video
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption("SpaceShip")

        self.display = pygame.display.set_mode([WIDTH, HEIGHT])

        self.scene = "menu"
        self.current_scene = Menu()

        #parte 1 - FPS
        self.fps =pygame.time.Clock()

    def run(self):

        while True:


            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"
                self.current_scene = Game()
            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            #for para pegar eventos do jogo
            for event in pygame.event.get():
                #fecha o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #chama o método de eventos da cena
                self.current_scene.events(event)

            self.display.fill("black")
            self.current_scene.draw()
            #parte 2 - descomentar - tradicional
            #self.current_scene.draw(self.display)
            self.current_scene.update()
            pygame.display.flip()