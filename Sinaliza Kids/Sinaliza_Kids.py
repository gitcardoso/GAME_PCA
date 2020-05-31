import pygame
from Background import BG_INICIO
import Botoes as b
from time import sleep

pygame.init()


#Tela Inicial
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Sinaliza Kids')
BG = BG_INICIO()

audio_bg = pygame.mixer_music.load('AUDIO/background.wav')
pygame.mixer_music.play()

#Botões
but01 = b.Jogar()
but02 = b.Credito()


#Loop Principal do Jogo
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            break
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                if 455 > x > 207 and 288 > y > 144:
                    but01.mostrar_clicado(screen)
                    pygame.display.update()
                    sleep(0.2)
                
                    import jogo

                           
                elif 791 > x > 545 and 288 > y > 144:
                    but02.mostrar_clicado(screen)
                    pygame.display.update()
                    sleep(0.2)

                    import creditos

    
    #Exibições
    BG.mostrar(screen)
    but01.mostrar_clicar(screen)
    but02.mostrar_clicar(screen)


    #Atualizações
    pygame.display.update()
