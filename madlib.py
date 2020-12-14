from random import randint


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
    madlib = "\nDATE:{}\n Please excuse {}\n, who is far too {} to attend {} class.\n".format(words[0], words[1],
                                                                                              words[2],
                                                                                              words[3])
    print(madlib)


def story2():
    words = input2()
    madlib = "\nDATE:{}\n {} is sick\n with the {} flu.\n Drink more {} and take {} as needed".format(words[0],
                                                                                                      words[1],
                                                                                                      words[2],
                                                                                                      words[3],
                                                                                                      words[4])
    print(madlib)


def story3():
    words = input3()
    madlib = "\nDATE:{}\n {} is authorized\n to be at {} instead of {} class.".format(words[0], words[1], words[2],
                                                                                      words[3])
    print(madlib)


def story4():
    words = input4()
    madlib = "\nDate:{}\n {} is too cool\n for {} class.\n Instead, she/he will be\n attending the {}\n".format(
        words[0], words[1], words[2],
        words[3])
    print(madlib)


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