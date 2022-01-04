import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow',
          'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    nums = 0
    while True:
        nums = input('Enter the number of racers (2 - 10): ')
        if nums.isdigit():
            nums = int(nums)
        else:
            print('Input is not numeric. Please try again :)')
            continue

        if 2 <= nums <= 10:
            return nums
        else:
            print('The number you entered is out of range. Please try again')


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        # awalnya menghadap kanan, diputarlah 90 drjt ke kiri biar ngadep atas
        racer.left(90)
        racer.penup()
        # to set position
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, - HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f'The winner is {winner}')
time.sleep(5)
