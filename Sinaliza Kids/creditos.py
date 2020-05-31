import pygame

pygame.init()


#Tela Inicial
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Creditos')
BLACK = (0, 0, 0)


#Loop Principal do Jogo
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break


    #Exibições
    screen.fill(BLACK)


    #Atualização
    pygame.display.flip()
