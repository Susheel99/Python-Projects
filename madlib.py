from random import randint
import pygame

# pygame setup
pygame.init()
pygame.font.init()
width, height = 500, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Madlib")

word_font = pygame.font.SysFont("timesnewroman", 30)

black = (0, 0, 0)
white = (255, 255, 255)

fps = 60
clock = pygame.time.Clock()


def write_screen(words):
    win.fill(white)

    # print text
    i = 0
    for sen in words:
        i = i + 5
        text = word_font.render(sen, 1, black)
        win.blit(text, (50, 10 * i))
    pygame.display.update()

def print_screen(words):
    run = True
    while run:
        clock.tick(fps)
        lines = words.split('$')
        write_screen(lines)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


# Functions to take inputs for a random story
def input1():
    date = input("Enter today's date:")
    name = input("Enter any name:")
    adj = input("Enter any adjective:")
    noun = input("Enter any noun,mostly any subject name:")

    return date, name, adj, noun


def input2():
    date = input("Enter today's date:")
    name = input("Enter any name:")
    part = input("Enter any part of the body:")
    fluid = input("Enter any type of fluid:")
    substance = input("Enter any eatable healthy substance:")

    return date, name, part, fluid, substance


def input3():
    date = input("Enter today's date:")
    name = input("Enter any name:")
    place = input("Enter any place:")
    noun = input("Enter any noun,mostly any subject name:")

    return date, name, place, noun


def input4():
    date = input("Enter today's date:")
    name = input("Enter any name:")
    noun = input("Enter any noun,mostly any subject name:")
    event = input("Enter any event name:")

    return date, name, noun, event


def story1():
    words = input1()
    madlib = "DATE:{}$ Please excuse {}$, who is far too {} to $attend {} class.$".format(words[0], words[1],
                                                                                              words[2],
                                                                                              words[3])
    print_screen(madlib)


def story2():
    words = input2()
    madlib = "DATE:{}$ {} is sick$ with the {} flu.$ Drink more {} and take ${} as needed".format(words[0],
                                                                                                      words[1],
                                                                                                      words[2],
                                                                                                      words[3],
                                                                                                      words[4])
    print_screen(madlib)


def story3():
    words = input3()
    madlib = "DATE:{}$ {} is authorized$ to be at {} instead $of {} class.".format(words[0], words[1], words[2],
                                                                                      words[3])
    print_screen(madlib)


def story4():
    words = input4()
    madlib = "Date:{}$ {} is too cool$ for {} class.$ Instead, she/he will be$ attending the {}$".format(
        words[0], words[1], words[2],
        words[3])
    print_screen(madlib)


def main():
    val = randint(1, 4)
    if val == 1:
        story1()
    elif val == 2:
        story2()
    elif val == 3:
        story3()
    else:
        story4()


if __name__ == '__main__':
    main()