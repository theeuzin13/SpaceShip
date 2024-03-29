import pygame



#herança para classe Sprite que trás uma série de recursos para tratar imagens
class Obj(pygame.sprite.Sprite):

    def __init__(self,img,pos,*groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=pos)

        self.tick = 0
        self.frame = 0

    def animation(self, speed, n_img, path):
        self.tick += 1
        if self.tick > speed:
            self.tick=0
            self.frame = (self.frame + 1) % n_img
            self.image = pygame.image.load(path+str(self.frame)+ ".png")