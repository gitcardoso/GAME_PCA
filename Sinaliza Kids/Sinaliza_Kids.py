import pygame
from Background import Background
from Car import Car
pygame.init()


 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Sinaliza Kids')
watch = pygame.time.Clock()

#Fundo Jogo
BG = Background()
imgs_bg = pygame.sprite.Group(BG)

#Carro
Carro = Car()


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


    imgs_bg.update()

    #drawing the sprite
    imgs_bg.draw(screen)

    Carro.mostrar(screen)

    #updating the display
    pygame.display.update()

    #finally delaying the loop to with clock tick for 10fps 
    watch.tick(2)