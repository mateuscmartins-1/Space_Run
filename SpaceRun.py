#Importar o pygame
import pygame 


pygame.init()

WIDTH = 1252
HEIGHT = 556
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Run')


game = True

planeta1_fundo = pygame.image.load(r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\jpg2png\PAISAG~1.png').convert()
planeta1_fundo = pygame.transform.scale(planeta1_fundo, (WIDTH, HEIGHT))
planeta2_fundo = pygame.image.load(r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\1866.png').convert()
planeta2_fundo = pygame.transform.scale(planeta2_fundo, (WIDTH, HEIGHT))
planeta3_fundo = pygame.image.load(r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\4Z_2104.w028.n002.36B.p30.36.png').convert_alpha()
planeta3_fundo = pygame.transform.scale (planeta3_fundo, (WIDTH, HEIGHT))
planeta1 = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Captura de Tela 2021-05-24 às 16.32.02.png').convert_alpha()
planeta1 = pygame.transform.scale (planeta1, (480,560))
planeta2 = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Captura de Tela 2021-05-24 às 16.42.46.png').convert_alpha()
planeta2 = pygame.transform.scale (planeta2, (480, 360))
planeta3 = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Captura de Tela 2021-05-24 às 16.43.23.png').convert_alpha()
planeta3 = pygame.transform.scale (planeta3, (480, 360))
naveaamiga = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Nave amiga.png').convert_alpha()
naveaamiga = pygame.transform.scale (naveaamiga, (160, 150))
naveinimiga = pygame.image.load (r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\Nave inimiga.png').convert_alpha()
naveinimiga = pygame.transform.scale (naveinimiga, (160, 150))


class amigo(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2
        self.rect.left = 0
    def update(self):

        self.rect.y += self.speedx

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top > 0:
            self.rect.top = 5


player_nave = amigo(naveaamiga)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            


    tela.fill((0, 0, 0))  
    tela.blit(planeta1_fundo, (0,0))
    tela.blit(player_nave.image, player_nave.rect)
    tela.blit(planeta2,(0,0))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

