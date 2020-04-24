import pygame
pygame.init()
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        #adicionar todas as imagens ao conjunto de sprites
        self.images = []
        self.images.append(pygame.image.load('IMG/loop bg/loop.01.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.02.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.03.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.04.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.05.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.06.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.07.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.08.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.09.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.10.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.11.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.12.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.13.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.14.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.15.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.16.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.17.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.18.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.19.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.20.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.21.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.22.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.23.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.24.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.25.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.26.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.27.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.28.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.29.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.30.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.31.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.32.png'))
        self.images.append(pygame.image.load('IMG/loop bg/loop.33.png'))

        #index value para obter a imagem da matriz
        #inicialmente é 0 
        self.index = 0

        #agora a imagem que exibiremos será o índice da matriz de imagens 
        self.image = self.images[self.index]

        #criando um ret na posição x, y (5,5) do tamanho (150,198), que é o tamanho do sprite 
        self.rect = pygame.Rect(0, 0, 1000, 600)

    def update(self):
        #quando o método de atualização for chamado, incrementaremos o índice
        self.index += 1

        #se o índice for maior que o total de imagens
        if self.index >= len(self.images):
            #faremos o índice para 0 novamente
            self.index = 0
        
        #finalmente atualizaremos a imagem que será exibida
        self.image = self.images[self.index]
