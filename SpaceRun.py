#Importar o pygame
import pygame 
import random

pygame.init()

WIDTH = 1252
HEIGHT = 556
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Run')

PLANETA_WIDTH = 480 #Largura do Planeta

PLANETA_HEIGHT = 360 #Altura do Planeta

NAVE_WIDTH = 130 #Largura da nave

NAVE_HEIGHT = 140 #Altura do nave



#planeta1_fundo = pygame.image.load(r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\jpg2png\PAISAG~1.png').convert()
#planeta1_fundo = pygame.transform.scale(planeta1_fundo, (WIDTH, HEIGHT))
#planeta2_fundo = pygame.image.load(r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\1866.png').convert()
#planeta2_fundo = pygame.transform.scale(planeta2_fundo, (WIDTH, HEIGHT))
#planeta3_fundo = pygame.image.load(r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\4Z_2104.w028.n002.36B.p30.36.png').convert_alpha()
#planeta3_fundo = pygame.transform.scale (planeta3_fundo, (WIDTH, HEIGHT))
#planeta1 = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Captura de Tela 2021-05-24 às 16.32.02.png').convert_alpha()
#planeta1 = pygame.transform.scale (planeta1, (480,560))
#planeta2 = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Captura de Tela 2021-05-24 às 16.42.46.png').convert_alpha()
#planeta2 = pygame.transform.scale (planeta2, (480, 360))
#planeta3 = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Captura de Tela 2021-05-24 às 16.43.23.png').convert_alpha()
#planeta3 = pygame.transform.scale (planeta3, (480, 360))
#naveaamiga = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Nave amiga.png').convert_alpha()
#naveaamiga = pygame.transform.scale (naveaamiga, (130, 140))
#naveinimiga = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Nave inimiga.png').convert_alpha()
#naveinimiga = pygame.transform.scale (naveinimiga, (130, 140))


planeta1_fundo = pygame.image.load('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.06.28.png').convert_alpha()
planeta1_fundo = pygame.transform.scale(planeta1_fundo, (WIDTH, HEIGHT))
planeta2_fundo = pygame.image.load('/Users/gabriela/Downloads/1866 (1).png').convert_alpha()
planeta2_fundo = pygame.transform.scale(planeta2_fundo, (WIDTH, HEIGHT))
planeta3_fundo = pygame.image.load('/Users/gabriela/Downloads/4Z_2104.w028.n002.36B.p30.36.png').convert_alpha()
planeta3_fundo = pygame.transform.scale (planeta3_fundo, (WIDTH, HEIGHT))
planeta1 = pygame.image.load ('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.32.02.png').convert_alpha()
planeta1 = pygame.transform.scale (planeta1, (480,560))
planeta2 = pygame.image.load ('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.42.46.png').convert_alpha()
planeta2 = pygame.transform.scale (planeta2, (480, 360))
planeta3 = pygame.image.load ('/Users/gabriela/Desktop/Captura de Tela 2021-05-24 às 16.43.23.png').convert_alpha()
planeta3 = pygame.transform.scale (planeta3, (480, 360))
naveaamiga = pygame.image.load ('/Users/gabriela/Downloads/Nave amiga (2).png').convert_alpha()
naveaamiga = pygame.transform.scale (naveaamiga, (130, 140))
naveinimiga = pygame.image.load ('/Users/gabriela/Downloads/Nave inimiga (2).png').convert_alpha()
naveinimiga = pygame.transform.scale (naveinimiga, (130, 140))


class amigo(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2
        self.rect.left = 0
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class inimigo(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0,HEIGHT-NAVE_HEIGHT)
        self.rect.x = WIDTH-NAVE_WIDTH

all_sprites = pygame.sprite.Group()


inimigo_nave = inimigo(naveinimiga)
player_nave = amigo(naveaamiga)
all_sprites.add(player_nave)
all_sprites.add(inimigo_nave)


FPS = 30
velocidade = 2
game = True
clock = pygame.time.Clock()
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player_nave.speedy += velocidade
        if event.key == pygame.K_UP:
            player_nave.speedy -= velocidade
        if event.key == pygame.K_RIGHT:
            player_nave.speedx += velocidade
        if event.key == pygame.K_LEFT:
            player_nave.speedx -= velocidade

    all_sprites.update()

    tela.blit(planeta1_fundo, (0, 0))
    all_sprites.draw(tela)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
