def talkToAlbusDumbledore(): #uses dictionary for options - Albus Dumbledore function
    print("Professor Dumbledore sees you. He starts to talk to you")
    print("Hello young traveler! Who might you be?")

    name = input()

    print("You answered Professor Dumbledore with your name: " + name)
    print("Professor Dumbledore responds with: if you are looking to leave the castle young " + name + " you must pick a door.")
    print("Some doors are more treacherous than others")
    print("Which door do you pick?")
    print("1, 2, 3, 4, 5, 6") # must be a number

    option = int(input("Your choice is: ")) # converts user input to integer - input & dictionary together did not work without this code

    door_dict = { # Door dictionary #only one true option to make it out of this section - option 6
        1: "Danger lies behind this door - a troll stands in your way - you must go back",
        2: "Treachery lies behind this door - you fell into devil's snare - game over!",
        3: "An empty classroom - how disappointing - go back",
        4: "You see the ghosts of Hogwarts enjoying a Death Day celebration - you cannot proceed",
        5: "The house elves are tidying this room - back away",
        6: "This is a hidden portal to the exit! Congratulations - you have found your way out"
    }
    userInputs = [1, 2, 3, 4, 5, 6] # defined this to use in while loop
    userInput = "" # initially empty
    while userInput not in userInputs:
        if option == 1:
            # having trouble letting the user choose more than one option
            # after second choice, game starts over
            # issue resolved with while loop
            print(door_dict[1])
            print("Choose again!")
            option = int(input("Next Guess: "))
        elif option == 2: # immediate death
            print(door_dict[2])
            print("Immediate death!")
            quit()
        elif option == 3:
            print(door_dict[3])
            option = int(input("Next Guess: "))
        elif option == 4:
            print(door_dict[4])
            option = int(input("Next Guess: "))
        elif option == 5:
            print(door_dict[5])
            option = int(input("Next Guess: "))
        elif option == 6: # only true option to exit game
            print(door_dict[6])
            quit()
        else:
            print("You must choose a valid option")



