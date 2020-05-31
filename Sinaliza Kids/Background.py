import pygame
pygame.init()

class BG_JOGO(pygame.sprite.Sprite):
    def __init__(self):
        super(BG_JOGO, self).__init__()
        #Adicionando as imagens ao conjunto de sprites
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

        #Definindo o Index com valor 0
        self.index = 0

        #Definindo o valor Index como a posição da lista que será exibida na tela
        #Inicialmente será exibida na tela a imagem de posição 0 da lista
        self.image = self.images[self.index]

        #criando um ret na posição x, y (0,0) do tamanho (1000, 600), que é o tamanho do sprite
        #Não sei ainda a utilidade de usar a função rect 
        self.rect = pygame.Rect(0, 0, 1000, 600)

    def update(self):
        #Definindo que a cada repedição while, o comando update adicione +1 ao valor do Index
        self.index += 1

        #Se o valor do Index for maior que o total de imagens
        if self.index >= len(self.images):
            #Faremos o Index retornar para o valor 0 novamente
            self.index = 0
        
        #Atualizando a posição da lista com o novo valor do Index
        #Isso automaticamente mudará a imagem que será exibida, criando assim o loop
        self.image = self.images[self.index]



class BG_INICIO(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.BGI = pygame.image.load('IMG/bg_inicio.png')

    def mostrar(self, superficie):
        superficie.blit(self.BGI, (0,0))

   