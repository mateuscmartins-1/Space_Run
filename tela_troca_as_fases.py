import pygame
from config import FPS, QUIT, GAME, GAME2, GAME3
from assets import PLANETA1, PLANETA2, PLANETA3, PLANETA2_RECT, PLANETA1_RECT, PLANETA3_RECT, MUSICA_TRANSICAO, MUSICA_ENTRADA, load_assets
def tela_troca_fase1(janela):
    assets = load_assets()
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
    assets[MUSICA_ENTRADA].stop()
    assets[MUSICA_TRANSICAO].play()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = GAME
                    jogo = False
        janela.fill((0, 0, 0))  
        janela.blit(assets[PLANETA1],assets[PLANETA1_RECT])
        pygame.display.flip()
    return state

def tela_troca_fase2(janela):
    assets = load_assets()
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
    pygame.mixer.music.stop()
    assets[MUSICA_TRANSICAO].play()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(loops= -1)
                    state = GAME2
                    jogo = False
        janela.fill((0, 0, 0))  
        janela.blit(assets[PLANETA2],assets[PLANETA2_RECT])
        pygame.display.flip()
    return state

def tela_troca_fase3(janela):
    assets = load_assets()
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
    pygame.mixer.music.stop()
    assets[MUSICA_TRANSICAO].play()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(loops= -1)
                    state = GAME3
                    jogo = False
        janela.fill((0, 0, 0))  
        janela.blit(assets[PLANETA3],assets[PLANETA3_RECT])
        pygame.display.flip()
    return state
