import pygame 
from config import FPS, QUIT, TRANSICAO1
from assets import TELA_INTRODUCAO, TELA_INTRODUCAO_RECT, load_assets
def tela_de_introducao(janela):
    assets = load_assets()
    clock = pygame.time.Clock()
    jogo = True
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = TRANSICAO1
                    jogo = False
        janela.fill((0,0,0))
        janela.blit(assets[TELA_INTRODUCAO], assets[TELA_INTRODUCAO_RECT])
        pygame.display.flip()
    return state