from talkToHarryPotter import talkToHarryPotter
from talkToSeverusSnape import talkToSeverusSnape


def beginningScene(): # the first scene and changes for directions
    directions = ["left", "right", "forward"]
    print("You come upon the first staircase in Hogwarts.")
    print("You can choose to go forward or go left or right around the staircase")
    print("Which direction would you like to go?")
    userInput = ""

    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            talkToHarryPotter()
        elif userInput == "right":
            talkToSeverusSnape()
        elif userInput == "forward":
            print("This is a dead end! Start over")
            quit()
        else:
            print("You must enter a valid option.")
