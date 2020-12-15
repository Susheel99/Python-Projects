import pygame
import math

# setup
pygame.init()
width, height = 800, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game!!")

# button variables
radius = 20
gap = 15
letters = []
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + gap + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(A + i), True])

# Font
letter_font = pygame.font.SysFont('comicsans', 40)

# load images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 6

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# setup game loop
fps = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(white)

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter

        if visible:
            pygame.draw.circle(win, black, (x, y), radius, 1)
            text = letter_font.render(ltr, 1, black)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


while run:
    clock.tick(fps)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < radius:
                        letter[3] = False


pygame.quit()
