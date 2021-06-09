import pygame 
from config import WIDTH, HEIGHT, QUIT, INIT, INTRODUCTION, TRANSICAO1, TRANSICAO2, TRANSICAO3, GAME, GAME3, GAME2, END_SCREEN, END_SCREEN2
from tela_inicial import tela_inicial
from tela_introducao import tela_de_introducao
from tela_troca_as_fases import tela_troca_fase1, tela_troca_fase2, tela_troca_fase3
from telas_do_jogo import tela_do_jogo1, tela_do_jogo2, tela_do_jogo3
from telas_finais import tela_final1, tela_final2

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Run')


state = INIT

while state != QUIT:
    if state == INIT:
        state = tela_inicial(tela)
    elif state == INTRODUCTION:
        state = tela_de_introducao(tela)
    elif state == TRANSICAO1:
        state = tela_troca_fase1(tela)
    elif state == TRANSICAO2:
        state = tela_troca_fase2(tela)
    elif state == TRANSICAO3:
        state = tela_troca_fase3(tela)
    elif state == GAME:
        state = tela_do_jogo(tela)
    elif state == GAME2:
        state = tela_do_jogo2(tela)
    elif state == GAME3:
        state = tela_do_jogo3(tela)
    elif state == END_SCREEN:
        state = tela_final1(tela)
    elif state == END_SCREEN2:
        state = tela_final2(tela)
    else:
        state = QUIT

# ===== Finalização ===== #
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

