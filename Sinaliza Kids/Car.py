import pygame
pygame.init()

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImgCar = pygame.image.load('IMG/car.png')

        self.rect = self.ImgCar.get_rect()
        self.rect = pygame.Rect(100, 320, 304, 120)


        self.velocidade = 10

    def mostrar(self, superficie):
        superficie.blit(self.ImgCar, self.rect)


    def movimento(self):

            if self.rect.bottom >= 490:
                self.rect.bottom = 490

            elif self.rect.top < 320:
                self.rect.top = 320