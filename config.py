from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')
SND_DIR = path.join(path.dirname(__file__), 'sound')
FNT_DIR = path.join(path.dirname(__file__), 'fontes')

#dados gerais do jogo 
WIDTH = 1252

FPS = 30

HEIGHT = 556

#tamanho dos componentes do jogo
NAVE_WIDTH = 80 #Largura da nave

NAVE_HEIGHT = 90 #Altura do nave

TIRO_WIDTH = 20 #Largura dos tiros

TIRO_HEIGHT = 20 #Altura dos tiros

#estados para controle do fluxo da aplicação 
INIT = 0 
GAME = 1 
QUIT = 2 
END_SCREEN = 3
END_SCREEN2 = 4
INTRODUCTION = 5
TRANSICAO1 = 6
TRANSICAO2 = 7
TRANSICAO3 = 8
GAME2 = 9
GAME3 = 10