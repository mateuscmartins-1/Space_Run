import pygame
from config import FPS,QUIT,INIT
from assets import load_assets,YOU_WIN,YOU_LOSE,TELA_ESTRELAS,TELA_ESTRELAS_RECT

def tela_final1(janela):
    assets = load_assets()
    clock = pygame.time.Clock()
    jogo = True
    controle = True
    pygame.mixer.music.stop()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(loops= -1)
                    state= INIT
                    jogo = False
        if controle:
            assets[YOU_LOSE].play()
            controle = False
        font = pygame.font.SysFont(None, 130)
        font2 = pygame.font.SysFont(None, 50)
        gameover = font.render('GAME OVER! YOU LOSE', True, (255, 0, 0))  
        jogue_novamente = font2.render("PARA JOGAR NOVAMENTE PRESSIONE [ENTER]",True, (255,255,255))
        janela.fill((0, 0, 0))  
        janela.blit(assets[TELA_ESTRELAS], assets[TELA_ESTRELAS_RECT])
        janela.blit(gameover, (90 , 139))
        janela.blit(jogue_novamente,(200,400))
        pygame.display.flip()
    return state

def tela_final2(janela):
    assets = load_assets()
    clock = pygame.time.Clock()
    jogo = True
    controle = True
    pygame.mixer.music.stop()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state= INIT
                    jogo = False
        if controle:
            assets[YOU_WIN].play()
            controle = False
        font = pygame.font.SysFont(None, 130)
        font2 = pygame.font.SysFont(None, 50)
        gameover = font.render('GAME OVER! YOU WIN', True, (0, 255, 0))  
        jogue_novamente = font2.render("PARA JOGAR NOVAMENTE PRESSIONE [ENTER]",True, (255,255,255))
        janela.fill((0, 0, 0))  
        janela.blit(assets[TELA_ESTRELAS], assets[TELA_ESTRELAS_RECT])
        janela.blit(gameover, (90 , 139))
        janela.blit(jogue_novamente,(200,400))
        pygame.display.flip()
    return state