#Importar o pygame
import pygame 


pygame.init()

tela = pygame.display.set_mode((1252,556))
pygame.display.set_caption('Space Run')


game = True

planeta1_fundo = pygame.image.load('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.06.28.png').convert_alpha()
planeta1_fundo = pygame.transform.scale(planeta1_fundo, (1252, 556))
planeta2_fundo = pygame.image.load('/Users/gabriela/Desktop/1866.jpg').convert()
planeta2_fundo = pygame.transform.scale(planeta2_fundo, (1252, 556))
planeta3_fundo = pygame.image.load('/Users/gabriela/Downloads/4Z_2104.w028.n002.36B.p30.36.png').convert_alpha()
planeta3_fundo = pygame.transform.scale (planeta3_fundo, (1252, 556))
planeta1 = pygame.image.load ('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.32.02.png').convert_alpha()
planeta1 = pygame.transform.scale (planeta1, (480,560))
planeta2 = pygame.image.load ('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.42.46.png').convert_alpha()
planeta2 = pygame.transform.scale (planeta2, (480, 560))
planeta3 = pygame.image.load ('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.43.23.png').convert_alpha()
planeta3 = pygame.transform.scale (planeta3, (480, 560))
naveaamiga = pygame.image.load ('/Users/gabriela/Downloads/Nave amiga.png').convert_alpha()
naveaamiga = pygame.transform.scale (naveaamiga, (160, 240))
naveinimiga = pygame.image.load ('/Users/gabriela/Downloads/Nave inimiga.png').convert_alpha()
naveinimiga = pygame.transform.scale (naveinimiga, (240, 320))

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game = False


    tela.fill((0, 0, 0))  
    tela.blit(planeta1, (0,0))
    tela.blit(naveaamiga, (0,0))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

