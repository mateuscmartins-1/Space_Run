#Importar o pygame
import pygame 


pygame.init()

tela = pygame.display.set_mode((1252,556))
pygame.display.set_caption('Space Run')


game = True

planeta1 = pygame.image.load(r'C:\Users\mateu\OneDrive\Documents\Insper\Dessoft\Projeto Final\Space Run\Space_Run\Imagens - dessoft\jpg2png\PAISAG~1.png').convert()
planeta1 = pygame.transform.scale(planeta1, (1252, 556))
while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game = False


    tela.fill((0, 0, 0))  
    tela.blit(planeta1, (0,0))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

