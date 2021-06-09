import pygame 
from config import FPS, QUIT, INTRODUCTION
from assets import MUSICA_ENTRADA, load_assets
def tela_inicial(janela):
    assets = load_assets()
    clock = pygame.time.Clock()
    tela_de_inicio = pygame.image.load('imgs/Spacerun.png').convert()
    tela_de_inicio_rect = tela_de_inicio.get_rect()
    jogo = True
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = INTRODUCTION
                    jogo = False
        assets['musica_entrada'].play()
        janela.fill((0,0,0))
        janela.blit(tela_de_inicio, tela_de_inicio_rect)
        pygame.display.flip()
    return state
