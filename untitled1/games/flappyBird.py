import pygame
pygame.init()

pygame.display.set_mode((600,400))
pygame.display.set_caption("FlapPyBird")

gameOff=False

while not gameOff:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                print(event)
                gameOff=True
            else:
                print(event)


pygame.quit()
quit()