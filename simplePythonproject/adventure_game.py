import time
import random
choice = ['breaks apart and the jewels fall out of reach',
          'holds together and you now have a large treasure']

pick1or2 = ""


def choose(pick1or2):
    if pick1or2 == 1:
        cave()
    elif pick1or2 == 2:
        mine()


def print_pause(inputText):
    print(inputText)
    time.sleep(0.75)


def intro():
    print_pause('the game is about to begin')
    print_pause('you are walking outdoors and see a cave')
    print_pause('you decide to enter the cave')


def cave():
    pick1or2 = input('''you find a pot of gold in the back of the cave.
    do you want to try to carry it out?
    please enter 1 for yes or 2 for no ''')
    if pick1or2 == "1":
        print_pause('''you carry the treasure out of the cave
         and see a house in the distance''')
        house()
    elif pick1or2 == "2":
        print_pause('you keep walking forward')
        caveMore()
    elif pick1or2 != "1" or "2":
        print_pause('''that is an invalid response,
        please review the question and acceptable answers''')
        cave()


def mine():
    print_pause('''you enter a mine that contains rare jewels.
    the chest holding the jewels looks unsteady.''')
    pick1or2 = input('''do you want to try to carry out the jewels?
    please enter 1 for yes or 2 for no ''')
    if pick1or2 == "1":
        print_pause('you try to pick up the chest and the chest '
                    + random.choice(choice))
        print_pause('you now head toward the exit of the cave')
        house()
    elif pick1or2 == "2":
        print_pause('you now head toward the exit of the cave')
        field()
    elif pick1or2 != "1" or "2":
        print_pause('''that is an invalid response,
        please review the question and acceptable answers''')
        mine()


def caveMore():
    print_pause('''you go deeper in cave
    and find an opening to a field''')
    pick1or2 = input('''do you want to exit the cave to the field?
    please enter 1 for yes or 2 for no ''')
    if pick1or2 == "1":
        field()
    elif pick1or2 == "2":
        mine()
    elif pick1or2 != "1" or "2":
        print_pause('''that is an invalid response,
        please review the question and acceptable answers''')
        caveMore()


def field():
    pick1or2 = input('''you see a hole with treasure in the field?
    do you want to collect it?
    please enter 1 for yes or 2 for no ''')
    if pick1or2 == "1":
        print_pause('''you collect the treasure
        and begin to count see that it is worth:''')
        print_pause(random.randint(100, 50000))
        print_pause('you win. game over.')
        gameOver()
    elif pick1or2 == "2":
        print_pause('you walk back to your house with nothing. ')
        house()
    elif pick1or2 != "1" or "2":
        print_pause('''that is an invalid response,
        please review the question and acceptable answers''')
        field()


def house():
    pick1or2 = input('''you enter a house and find dinner.
    do you want to eat the dinner?
    please enter 1 for yes or 2 for no ''')
    if pick1or2 == "1":
        print_pause('''you eat the dinner and fall asleep
        you lose. game over.''')
        gameOver()
    elif pick1or2 == "2":
        field()
    elif pick1or2 != "1" or "2":
        print_pause('''that is an invalid response,
        please review the question and acceptable answers''')
        house()


def gameOver():
    pick1or2 = input('''the game is over. do you want to play again?
     please enter 1 for yes or 2 for no ''')
    if pick1or2 == "1":
        print_pause('prepare to play again')
        gameStart()
    elif pick1or2 == "2":
        print_pause('thanks for playing')
    elif pick1or2 != "1" or "2":
        print_pause('''that is an invalid response,
        please review the question and acceptable answers''')
        gameOver()


def gameStart():
    intro()
    cave()


gameStart()
