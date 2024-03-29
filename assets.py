import pygame
import os
from config import WIDTH, HEIGHT, NAVE_HEIGHT, NAVE_WIDTH, TIRO_HEIGHT, TIRO_WIDTH
SOM_TIRO = 'tiro_da_nave'
MUSICA_ENTRADA = 'musica_entrada'
TELA_INTRODUCAO = "tela_instrucoes"
TELA_INTRODUCAO_RECT = "tela_instrucoes_rect"
PLANETA1 = 'planeta1' 
PLANETA2 = 'planeta2'
PLANETA3 = 'planeta3'
PLANETA1_RECT = 'planeta1_rect' 
PLANETA2_RECT = 'planeta2_rect'
PLANETA3_RECT = 'planeta3_rect'
MUSICA_TRANSICAO = 'musica_transicao'
PLANETA1_FUNDO = 'planeta1_fundo'
PLANETA2_FUNDO = 'planeta2_fundo'
PLANETA3_FUNDO = 'planeta3_fundo'
NAVE_AMIGA = 'naveaamiga'
NAVE_INIMIGA = 'naveinimiga'
TIRO_AMIGO = 'tiro_amigo'
TIRO_INIMIGO = 'tiro_inimigo'
MUSICA = 'musica'
PROXIMA_FASE = 'proxima_fase'
TIRO_ACERTADO = 'tiro_acertado'
TIRO_DA_NAVE = 'tiro_da_nave'
YOU_LOSE = 'you_lose'
YOU_WIN = 'you_win'
PONTUACAO = "pontuação"
TELA_ESTRELAS = 'tela_estrelas'
TELA_ESTRELAS_RECT = 'tela_estrelas_rect'
def load_assets ():
    assets = {}
    #Imagens 
    assets["planeta1_fundo"] = pygame.image.load('imgs/Fundo1.png').convert_alpha()
    assets["planeta1_fundo"] = pygame.transform.scale(assets["planeta1_fundo"], (WIDTH, HEIGHT))
    assets["planeta2_fundo"] = pygame.image.load('imgs/Fundo2.png').convert_alpha()
    assets["planeta2_fundo"] = pygame.transform.scale(assets["planeta2_fundo"], (WIDTH, HEIGHT))
    assets["planeta3_fundo"] = pygame.image.load('imgs/Fundo3.png').convert_alpha()
    assets["planeta3_fundo"] = pygame.transform.scale (assets["planeta3_fundo"], (WIDTH, HEIGHT))
    assets["planeta1"] = pygame.image.load ('imgs/Planeta1.png').convert_alpha()
    assets["planeta1"] = pygame.transform.scale (assets["planeta1"], (WIDTH,HEIGHT))
    assets["planeta1_rect"] = assets["planeta1"].get_rect()
    assets["planeta2"] = pygame.image.load ('imgs/Planeta2.png').convert_alpha()
    assets["planeta2"] = pygame.transform.scale (assets["planeta2"], (WIDTH,HEIGHT))
    assets["planeta2_rect"] = assets["planeta2"].get_rect()
    assets["planeta3"] = pygame.image.load ('imgs/Planeta3.png').convert_alpha()
    assets["planeta3"] = pygame.transform.scale (assets["planeta3"], (WIDTH,HEIGHT))
    assets["planeta3_rect"] = assets["planeta3"].get_rect()
    assets["naveaamiga"] = pygame.image.load ('imgs/Nave_amiga.png').convert_alpha()
    assets["naveaamiga"] = pygame.transform.scale (assets["naveaamiga"], (NAVE_WIDTH, NAVE_HEIGHT))
    assets["naveinimiga"] = pygame.image.load ('imgs/Nave_inimiga.png').convert_alpha()
    assets["naveinimiga"] = pygame.transform.scale (assets["naveinimiga"], (NAVE_WIDTH, NAVE_HEIGHT))
    assets["tiro_amigo"] = pygame.image.load ('imgs/Tiro amigo.png').convert_alpha() 
    assets["tiro_amigo"] = pygame.transform.scale (assets["tiro_amigo"], (TIRO_WIDTH, TIRO_HEIGHT))
    assets["tiro_inimigo"] = pygame.image.load ('imgs/Tiro inimigo.png').convert_alpha() 
    assets["tiro_inimigo"] = pygame.transform.scale (assets["tiro_inimigo"], (TIRO_WIDTH, TIRO_HEIGHT)) 
    assets["tela_estrelas"] = pygame.image.load ('imgs/tela_fundo.png').convert()
    assets["tela_estrelas"] = pygame.transform.scale(assets["tela_estrelas"], (WIDTH,HEIGHT))
    assets["tela_estrelas_rect"] = assets["tela_estrelas"].get_rect()
    assets["tela_instrucoes"] = pygame.image.load('imgs/tela_instrucoes.jpg').convert()
    assets["tela_instrucoes"] = pygame.transform.scale(assets["tela_instrucoes"], (WIDTH,HEIGHT))
    assets["tela_instrucoes_rect"] = assets["tela_instrucoes"].get_rect()
    # Fontes
    assets["pontuação"] = pygame.font.Font('fontes/PressStart2P.ttf', 25)
    assets["game_over_screen"] = pygame.font.Font('fontes/PressStart2P.ttf', 55)

    # Sons
    assets["musica"] = pygame.mixer.music.load('Sons/Musica-pygame.ogg')
    pygame.mixer.music.set_volume(0.4)
    assets["game_over"] = pygame.mixer.Sound('Sons/Game-over.wav')
    assets['proxima_fase'] = pygame.mixer.Sound('Sons/Próxima fase.wav')
    assets['tiro_acertado'] = pygame.mixer.Sound('Sons/Tiro-acertado.wav')
    assets['tiro_da_nave'] = pygame.mixer.Sound('Sons/Tiro-da-nave.wav')
    assets['you_lose'] = pygame.mixer.Sound('Sons/you_lose.wav')
    assets['you_win'] = pygame.mixer.Sound('Sons/you_win.wav')
    assets['musica_entrada'] = pygame.mixer.Sound('Sons/musica_entrada.wav')
    assets['musica_transicao'] = pygame.mixer.Sound('Sons/musica_transicao.wav')
    return assets