import pygame

class Scene:

    def __init__(self):
        pygame.display.set_caption("BeeHoney")

        #Parte 2
        self.image = pygame.image.load("assets/menu.png")

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    def draw(self, display):

        #parte 2 - descomentar
        display.blit(self.image, [0,0])


    def update(self):
        pass