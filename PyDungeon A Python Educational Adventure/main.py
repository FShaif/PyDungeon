from Functions import *
import time

# Written by Fahad Shaif PB0086      &&      Marwan Abdullah QA0067

welcomeScreen() # Welcome Screen to greet the player

continue_playing = True
while (continue_playing is True):

    # game code runs here
    game()

    # ask the player to play again otherwise exit loop
    response = input("Play Again? Enter N to quit\n")
    if (response.lower() == "n"):
        break


time.sleep(0.5)
print("\n\nThank you for playing PyDungeon!\n")
time.sleep(0.5)
print("this game was brought to you by: ")
print("Fahad Shaif PB0086")
time.sleep(0.5)
print("Under the guidance of Eng. Sami")
time.sleep(0.5)
