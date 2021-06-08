#Importar o pygame
import pygame 
import random

from pygame.constants import KEYUP

pygame.init()
pygame.mixer.init()


WIDTH = 1252
HEIGHT = 556
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Run')

PLANETA_WIDTH = 480 #Largura do Planeta

PLANETA_HEIGHT = 360 #Altura do Planeta

NAVE_WIDTH = 80 #Largura da nave

NAVE_HEIGHT = 90 #Altura do nave

TIRO_WIDTH = 30 #Largura dos tiros

TIRO_HEIGHT = 30 #Altura dos tiros

assets = {}
#Imagens 
assets["planeta1_fundo"] = pygame.image.load('imgs/Fundo1.png').convert_alpha()
assets["planeta1_fundo"] = pygame.transform.scale(assets["planeta1_fundo"], (WIDTH, HEIGHT))
assets["planeta2_fundo"] = pygame.image.load('imgs/Fundo2.png').convert_alpha()
assets["planeta2_fundo"] = pygame.transform.scale(assets["planeta2_fundo"], (WIDTH, HEIGHT))
assets["planeta3_fundo"] = pygame.image.load('imgs/Fundo3.png').convert_alpha()
assets["planeta3_fundo"] = pygame.transform.scale (assets["planeta3_fundo"], (WIDTH, HEIGHT))
assets["planeta1"] = pygame.image.load ('imgs/Planeta1.png').convert_alpha()
assets["planeta1"] = pygame.transform.scale (assets["planeta1"], (PLANETA_WIDTH,PLANETA_HEIGHT))
assets["planeta2"] = pygame.image.load ('imgs/Planeta2.png').convert_alpha()
assets["planeta2"] = pygame.transform.scale (assets["planeta2"], (PLANETA_WIDTH, PLANETA_HEIGHT))
assets["planeta3"] = pygame.image.load ('imgs/Planeta3.png').convert_alpha()
assets["planeta3"] = pygame.transform.scale (assets["planeta3"], (PLANETA_WIDTH, PLANETA_HEIGHT))
assets["naveaamiga"] = pygame.image.load ('imgs/Nave_amiga.png').convert_alpha()
assets["naveaamiga"] = pygame.transform.scale (assets["naveaamiga"], (NAVE_WIDTH, NAVE_HEIGHT))
assets["naveinimiga"] = pygame.image.load ('imgs/Nave_inimiga.png').convert_alpha()
assets["naveinimiga"] = pygame.transform.scale (assets["naveinimiga"], (NAVE_WIDTH, NAVE_HEIGHT))
assets["tiro_amigo"] = pygame.image.load ('imgs/Tiro amigo.png').convert_alpha() 
assets["tiro_amigo"] = pygame.transform.scale (assets["tiro_amigo"], (TIRO_WIDTH, TIRO_HEIGHT))
assets["tiro_inimigo"] = pygame.image.load ('imgs/Tiro inimigo.png').convert_alpha() 
assets["tiro_inimigo"] = pygame.transform.scale (assets["tiro_inimigo"], (TIRO_WIDTH, TIRO_HEIGHT)) 

# Fontes
assets["pontuação"] = pygame.font.Font('fontes/PressStart2P.ttf', 25)
assets["game_over_screen"] = pygame.font.Font('fontes/PressStart2P.ttf', 55)

# Sons
assets["musica"] = pygame.mixer.music.load('sons/Musica-pygame.ogg')
pygame.mixer.music.set_volume(0.4)
assets["game_over"] = pygame.mixer.Sound('sons/Game-over.wav')
assets['proxima_fase'] = pygame.mixer.Sound('sons/Próxima fase.wav')
assets['tiro_acertado'] = pygame.mixer.Sound('sons/Tiro-acertado.wav')
assets['tiro_da_nave'] = pygame.mixer.Sound('sons/Tiro-da-nave.wav')


# Fases
class amigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro,som_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = random.randint(139, 417)
        self.rect.left = 0
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 800
        self.som_tiro = som_tiro

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
        if self.speedx > 0:
            self.speedx -= 1
        elif self.speedx < 0:
            self.speedx += 1
        if self.speedy > 0:
            self.speedy -= 1
        elif self.speedy < 0:
            self.speedy += 1
    def tiro(self):
        ticks = pygame.time.get_ticks()
        ticks_passados = ticks - self.ultimo_tiro
        if ticks_passados > self.intervalo_tiro:
            self.ultimo_tiro = ticks
            bala = Tiro_Amigo(self.tiro_img, self.rect.bottom, self.rect.centerx)
            self.all_sprites.add(bala)
            self.all_tiros.add(bala)
            self.som_tiro.play()
            
class inimigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0,HEIGHT-NAVE_HEIGHT)
        self.rect.x = WIDTH-NAVE_WIDTH
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.speedx = -3
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 10
        self.fases = 1 
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 1000:
            self.rect.x = 1000
        self.speedx = -3
        self.intervalo_tiro -= 1
        if self.intervalo_tiro <= 0:
            if self.fases == 1:
                self.intervalo_tiro = 10 + random.randint(1,100)
                self.tiro()
            if self.fases == 2:
                self.intervalo_tiro = 10 + random.randint(1,50)
                self.tiro()
            if self.fases == 3:
                self.intervalo_tiro = 10 + random.randint(1,25)
                self.tiro()
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
        self.mask = pygame.mask.from_surface(self.image)
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
        self.mask = pygame.mask.from_surface(self.image)
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

def tela_inicial(janela):
    clock = pygame.time.Clock()
    tela_de_inicio = pygame.image.load('imgs/Spacerun.png.png').convert()
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
                    state = GAME
                    jogo = False
        janela.fill((0,0,0))
        janela.blit(tela_de_inicio, tela_de_inicio_rect)
        pygame.display.flip()
    return state

def tela_troca_fases(janela):
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
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
        font = pygame.font.SysFont(None, 130)
        font2 = pygame.font.SysFont(None, 50)
        gameover = font.render('Você eliminou os inimigos desse planeta! Se prepare para o próximo!', True, (255, 0, 0))  
        jogue_novamente = font2.render("Para ir para a próxima fase pressione ENTER",True, (255,255,255))
        janela.fill((0, 0, 0))  
        janela.blit(gameover, (90 , 139))
        janela.blit(jogue_novamente,(350,400))
        pygame.display.flip()
    return state

def tela_final(janela):
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state= END_SCREEN
                    jogo = False
        font = pygame.font.SysFont(None, 130)
        font2 = pygame.font.SysFont(None, 50)
        gameover = font.render('GAME OVER! YOU LOSE', True, (255, 0, 0))  
        score = font2.render('PONTUAÇÃO FINAL: {}'.format(pontuacao),True, (0,255,0))
        jogue_novamente = font2.render("PARA JOGAR NOVAMENTE PRESSIONE [ENTER]",True, (255,255,255))
        janela.fill((0, 0, 0))  
        janela.blit(gameover, (90 , 139))
        janela.blit(score, (475, 250))
        janela.blit(jogue_novamente,(350,400))
        pygame.display.flip()
    return state

all_sprites = pygame.sprite.Group()
all_tiros = pygame.sprite.Group()
all_inimigos = pygame.sprite.Group()
all_tiros2 = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_tiros'] = all_tiros
groups['all_inimigos'] = all_inimigos
groups['all_tiros2'] = all_tiros2


player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
all_sprites.add(player_nave)

pygame.mixer.music.play(loops=-1)

state = True
QUIT = False

while state != QUIT:
    kills = 0       # Eliminações do player
    vidas = 3       # Vidas da Nave
    pontuacao = 0   # Pontuação do player
    velocidade = 10 # Velocidade 

    INIT = 0 
    GAME = 1 
    QUIT = 2 
    END_SCREEN = 3
    state = INIT

    controle = True
    controle1 = True
    controle2 = True
    controle3 = True
    controle4 = True
    game = True

    FPS = 30
    clock = pygame.time.Clock()

    fases = assets["planeta1_fundo"]

    while state != QUIT:
        clock.tick(FPS)
        if state == INIT:
            state = tela_inicial(tela)
        if state == GAME: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = QUIT
                if event.type == pygame.KEYDOWN:
                    # Ao pressionar alguma dessas teclas o player se movimenta
                    if event.key == pygame.K_w:
                        player_nave.speedy -= velocidade
                    if event.key == pygame.K_a:
                        player_nave.speedx -= velocidade
                    if event.key == pygame.K_s:
                        player_nave.speedy += velocidade
                    if event.key == pygame.K_d:
                        player_nave.speedx += velocidade
                    # Ao pressionar a barra de espaço o player realiza o disparo
                    if event.key == pygame.K_SPACE:
                        player_nave.tiro()

        if vidas == 0:
            assets["game_over"].play()
            state = tela_final(tela)
            if state == END_SCREEN:
                break

        if controle == True:
            for i in range(2):
                inimigo_nave = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
                all_sprites.add(inimigo_nave)
                all_inimigos.add(inimigo_nave)
                all_tiros2.add(inimigo_nave)
                controle = False   

        all_sprites.update()
        danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True, pygame.sprite.collide_mask)
        danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True, pygame.sprite.collide_mask)
        
        for Enemy in danos:
            i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
            if fases == assets["planeta2_fundo"]:
                i.fases = 2
            if fases == assets["planeta3_fundo"]:
                i.fases = 3
            all_sprites.add(i)
            all_inimigos.add(i)
            all_tiros2.add(i)
            kills += 1 
            pontuacao += 5
        if kills == 1: 
            fases = assets["planeta2_fundo"]
            if controle1:
                i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
                all_sprites.add(i)
                all_inimigos.add(i)
                all_tiros2.add(i)
                i.fases = 2
                controle1 = False
        elif kills == 2:
            fases = assets["planeta3_fundo"]
            if controle2:
                i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
                all_sprites.add(i)
                all_inimigos.add(i)
                all_tiros2.add(i)
                i.fases = 3
                controle2 = False
        elif kills == 3:
            game = False
        if fases == assets["planeta2_fundo"] and controle3:
            assets['proxima_fase'].play()
            controle3 = False
        elif fases == assets["planeta3_fundo"] and controle4:
            assets['proxima_fase'].play()
            controle4 = False
        if danos:
            assets['tiro_acertado'].play()
        if danos2:
            vidas-= 1
            if vidas != 0:
                player_nave.kill()
                player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
                all_sprites.add(player_nave)
        tela.fill((0,0,0))
        tela.blit(fases, (0, 0))
        all_sprites.draw(tela)

       

        # Colocando a Pontuação
        pontuacao_tela = assets['pontuação'].render("{:03d}".format(pontuacao), True, (0, 255, 0))
        text_rect = pontuacao_tela.get_rect()
        text_rect.midtop = (WIDTH/2 ,  10)
        tela.blit(pontuacao_tela, text_rect)

        # Colocando as vidas
        vida_tela = assets['pontuação'].render(chr(9827) * vidas, True, (255, 0, 0))
        text_rect = vida_tela.get_rect()
        text_rect.bottomright = (WIDTH, HEIGHT - 10)
        tela.blit(vida_tela, text_rect)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
  
# ===== Finalização ===== #
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
