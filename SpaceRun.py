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

TIRO_WIDTH = 50 #Largura dos tiros

TIRO_HEIGHT = 50 #Altura dos tiros

planeta1_fundo = pygame.image.load('imgs/Fundo1.png').convert_alpha()
planeta1_fundo = pygame.transform.scale(planeta1_fundo, (WIDTH, HEIGHT))
planeta2_fundo = pygame.image.load('imgs/Fundo2.png').convert_alpha()
planeta2_fundo = pygame.transform.scale(planeta2_fundo, (WIDTH, HEIGHT))
planeta3_fundo = pygame.image.load('imgs/Fundo3.png').convert_alpha()
planeta3_fundo = pygame.transform.scale (planeta3_fundo, (WIDTH, HEIGHT))
planeta1 = pygame.image.load ('imgs/Planeta1.png').convert_alpha()
planeta1 = pygame.transform.scale (planeta1, (PLANETA_WIDTH,PLANETA_HEIGHT))
planeta2 = pygame.image.load ('imgs/Planeta2.png').convert_alpha()
planeta2 = pygame.transform.scale (planeta2, (PLANETA_WIDTH, PLANETA_HEIGHT))
planeta3 = pygame.image.load ('imgs/Planeta3.png').convert_alpha()
planeta3 = pygame.transform.scale (planeta3, (PLANETA_WIDTH, PLANETA_HEIGHT))
naveaamiga = pygame.image.load ('imgs/Nave_amiga.png').convert_alpha()
naveaamiga = pygame.transform.scale (naveaamiga, (NAVE_WIDTH, NAVE_HEIGHT))
naveinimiga = pygame.image.load ('imgs/Nave_inimiga.png').convert_alpha()
naveinimiga = pygame.transform.scale (naveinimiga, (NAVE_WIDTH, NAVE_HEIGHT))
tiro_amigo = pygame.image.load ('imgs/Tiro amigo.png').convert_alpha()#Tiro do player 
tiro_amigo = pygame.transform.scale (tiro_amigo, (TIRO_WIDTH, TIRO_HEIGHT)) #Ajuste do tamanho da imagem do tiro do player
tiro_inimigo = pygame.image.load ('imgs/Tiro inimigo.png').convert_alpha() #Tiro do player 
tiro_inimigo = pygame.transform.scale (tiro_inimigo, (TIRO_WIDTH, TIRO_HEIGHT)) #Ajuste do tamanho da imagem do tiro do player


class amigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2
        self.rect.left = 0
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 800

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > WIDTH//2:
            self.rect.right = WIDTH//2
        if self.rect.left < 0:
            self.rect.left = 0
    def tiro(self):
        ticks = pygame.time.get_ticks()
        ticks_passados = ticks - self.ultimo_tiro
        if ticks_passados > self.intervalo_tiro:
            self.ultimo_tiro = ticks
            bala = Tiro_Amigo(self.tiro_img, self.rect.bottom, self.rect.centerx)
            self.all_sprites.add(bala)
            self.all_tiros.add(bala)

class inimigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0,HEIGHT-NAVE_HEIGHT)
        self.rect.x = WIDTH-NAVE_WIDTH
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.speedx = -3
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 800
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 1000:
            self.rect.x = 1000
        self.speedx = -3
    def tiro(self):
        ticks = pygame.time.get_ticks()
        ticks_passados = ticks - self.ultimo_tiro
        if ticks_passados > self.intervalo_tiro:
            self.ultimo_tiro = ticks
            bala = Tiro_Inimigo(self.tiro_img, self.rect.bottom, self.rect.centerx)
            self.all_sprites.add(bala)
            self.all_tiros.add(bala)



class Tiro_Amigo(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = 8  
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()

class Tiro_Inimigo(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-TIRO_WIDTH 
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = -8  
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()
        self.speedx = -8

all_sprites = pygame.sprite.Group()
all_tiros = pygame.sprite.Group()
all_inimigos = pygame.sprite.Group()
all_tiros2 = pygame.sprite.Group()



player_nave = amigo(naveaamiga, all_sprites, all_tiros, tiro_amigo)
all_sprites.add(player_nave)

for i in range(2):
    inimigo_nave = inimigo(naveinimiga,all_sprites,all_tiros2,tiro_inimigo)
    all_sprites.add(inimigo_nave)
    all_inimigos.add(inimigo_nave)
    all_tiros2.add(inimigo_nave)

velocidade = 3.5 #Velocidade 
velocidade2 = 2  #Velocidade2 
game = True
FPS = 30
clock = pygame.time.Clock()
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_nave.speedy += velocidade2
            if event.key == pygame.K_UP:
                player_nave.speedy -= velocidade2
            if event.key == pygame.K_RIGHT:
                player_nave.speedx += velocidade
            if event.key == pygame.K_LEFT:
                player_nave.speedx -= velocidade
            if event.key == pygame.K_SPACE:
                player_nave.tiro()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_nave.speedy += velocidade2
            if event.key == pygame.K_UP:
                player_nave.speedy -= velocidade2
            if event.key == pygame.K_RIGHT:
                player_nave.speedx += velocidade
            if event.key == pygame.K_LEFT:
                player_nave.speedx -= velocidade

    all_sprites.update()
    danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True)
    danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True)
    for Enemy in danos:
        i = inimigo(naveinimiga,all_sprites,all_tiros2,tiro_inimigo)
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)
    
    if danos2:
        game = False

    tela.blit(planeta1_fundo, (0, 0))
    all_sprites.draw(tela)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
