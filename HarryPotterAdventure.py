# INF360 - Programming in Python
# Jasmine Irvin
# Midterm Project

# 25 points Does the program execute with no errors.
# 25 points Does the program solve a problem or create something new.
# 25 points The program should contain: Good flow control, good use of functions,
# code should be as clean as possible (i.e. writing the smallest amount
# of code necessary to complete the function), and contain examples of
# lists or dictionaries.
# 25 points The midterm project should be well documented. Make use of block
# and line comments to describe the program as a whole, individual
# functions, and major areas of the project.

from beginningScene import beginningScene

if __name__ == "__main__": # main section to run game - initial text and gets user input for name
    while True:
        print("Welcome to the Harry Potter Adventure Game!")
        print("As an excited traveler, you have decided to explore the vast halls of Hogwarts.")
        print("However, your exploration does not come without dangers.")
        print("Dangers are not limited to just being lost.")
        print("There are all manners of creatures, people, and dangerous plants to get around.")
        print("With that out of the way, let's start with your name: ")
        name = input()
        print("Good luck, " + name + ".")
        print("I hope you make it out alive!")
        beginningScene()

# This is my text adventure game where the traveler makes their way through the halls of Hogwarts
# there are several routes the user can choose to take

# future iterations should include OOP, formatting user input (lower and upper function to make sure it does not break program, and more functionality
