import pygame
pygame.init()

class Jogar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImgClicar = pygame.image.load('IMG/botao_jogar_clicar.png')
        self.ImgClicado = pygame.image.load('IMG/botao_jogar_clicado.png')

        self.rect1 = self.ImgClicar.get_rect()
        self.rect1 = pygame.Rect(208, 145, 246, 143)

        self.rect2 = self.ImgClicado.get_rect()
        self.rect2 = pygame.Rect(208, 145, 246, 143)


    def mostrar_clicar(self, superficie):
        superficie.blit(self.ImgClicar, self.rect1)

    def mostrar_clicado(self, superficie):
        superficie.blit(self.ImgClicado, self.rect2)


class Credito(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImgClicar = pygame.image.load('IMG/botao_credito_clicar.png')
        self.ImgClicado = pygame.image.load('IMG/botao_credito_clicado.png')

        self.rect1 = self.ImgClicar.get_rect()
        self.rect1 = pygame.Rect(546, 145, 246, 143)

        self.rect2 = self.ImgClicado.get_rect()
        self.rect2 = pygame.Rect(546, 145, 246, 143)


    def mostrar_clicar(self, superficie):
        superficie.blit(self.ImgClicar, self.rect1)

    def mostrar_clicado(self, superficie):
        superficie.blit(self.ImgClicado, self.rect2)