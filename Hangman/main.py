import pygame

# setup
pygame.init()
width, height = 800, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game!!")

# load images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)
print(images)

# game variables
hangman_status = 6

# colors
white = (255, 255, 255)

# setup game loop
fps = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(fps)

    win.fill(white)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
