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
word_font = pygame.font.SysFont('comicsans', 50)

# load images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# game variables
word = "DEVELOPER"
guessed = []
hangman_status = 0

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
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, black)
    win.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter

        if visible:
            pygame.draw.circle(win, black, (x, y), radius, 1)
            text = letter_font.render(ltr, 1, black)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    win.fill(white)
    text = word_font.render(message, 1, black)
    win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


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
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You WON the HANGMAN game!!")
        break

    if hangman_status == 6:
        display_message("You LOST the HANGMAN game!!")
        break

pygame.quit()
