from endingScene import endingScene


def talkToSeverusSnape():
    print("You come upon Professor Snape")
    print("Professor Snape speaks to you: what are you doing here? You are not a student")
    print("You must answer Professor Snape.")
    print("Your answer options are: fight, flee, talk ")

    actions = ["talk", "flee", "fight"]

    userInput = ""
    while userInput not in actions:
        userInput = input()
        if userInput == "flee":
            print("You chose to run away. You run back towards the beginning")
            endingScene()
        elif userInput == "fight":
            print("You chose the foolish action of fighting Professor Snape with no wand. You died! Game over")
            quit()
        elif userInput == "talk":
            print("Professor Snape sends you forward")
            print("You walk forwards and come upon the exit! Congrats!")
            quit()
        else:
            print("You must choose a valid option")