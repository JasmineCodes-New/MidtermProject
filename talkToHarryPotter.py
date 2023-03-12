from talkToAlbusDumbledore import talkToAlbusDumbledore
from talkToSeverusSnape import talkToSeverusSnape


def talkToHarryPotter(): # talk to Harry Potter function - user can choose directions to travel
    directions = ["right", "left"]
    print("You come upon Harry Potter! Ask him which direction you should take: right or left")
    userInput = ""
    while userInput not in directions:
        print("Options are right, left, or backwards. ")
        userInput = input()
        if userInput == "right":
            talkToAlbusDumbledore()
        elif userInput == "left":
            talkToSeverusSnape()
        elif userInput == "backwards":
            print("If you choose backwards: the game will end")
            print("You are choosing to exit the game")
            print("Goodbye!")
            quit()
        else:
            print("You must choose a valid option: left or right.")
