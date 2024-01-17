import pygame
from scripts.obj import Obj


class Scene:

    def __init__(self):

        self.display = pygame.display.get_surface()
        #uma espécie de array em grupos
        self.all_sprites = pygame.sprite.Group()
        #self.bg = Obj("assets/menu.png", [self.all_sprites])
        #parte 3 - descomentar
        #se estiver ativa, reproduz contúdo, se não vai para próxima cena.
        self.active = True

    def events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                #pygame.quit()
                #Parte 3 - tirar o quit
                #testar trocar cena
                self.active = False

    def draw(self):
        #cria todas imagens do grupo
        self.all_sprites.draw(self.display)

    def update(self):
        #atualiza todas imagens do grupo
        self.all_sprites.update()

