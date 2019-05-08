import pygame

# Abre la ventana de juego
pygame.init()

# Establecemos el largo y alto de la pantalla
dimensiones = (400, 500)
pantalla = pygame.display.set_mode(dimensiones)
juego=True
x=100
while juego==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Si el usuario hizo click sobre salir
            juego = False # Marcamos que hemos acabado y abandonamos este bucle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-=1
            if event.key == pygame.K_s:
                juego=False


    pantalla.fill((255,255,255))
    
    pygame.display.flip()
