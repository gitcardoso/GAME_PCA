import pygame
from Background import BG_JOGO
from Car import Car

pygame.init()

 
#Tela Inicial
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Sinaliza Kids')
BG = BG_JOGO()
imgs_bg = pygame.sprite.Group(BG)
watch = pygame.time.Clock()


#Inserindo o Carro
Carro = Car()


#Loop Principal do Jogo
while True:
    
    Carro.movimento()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
                Carro.rect.bottom += Carro.velocidade
     
        if event.key == pygame.K_UP:
                Carro.rect.top -= Carro.velocidade


   
    #Exibições
    imgs_bg.draw(screen)
    Carro.mostrar(screen)


    #Atualização
    imgs_bg.update()
    pygame.display.update()


    #Velocidade do Gif (loop) de imagens de fundo
    watch.tick(2)
