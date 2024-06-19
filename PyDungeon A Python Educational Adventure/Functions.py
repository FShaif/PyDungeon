import random
import time
from Classes import *


def welcomeScreen ():
    print("""                                                   
,------.          ,------.                                                
|  .--. ',--. ,--.|  .-.  \ ,--.,--.,--,--,  ,---.  ,---.  ,---. ,--,--,  
|  '--' | \  '  / |  |  \  :|  ||  ||      \| .-. || .-. :| .-. ||      \ 
|  | --'   \   '  |  '--'  /'  ''  '|  ||  |' '-' '\   --.' '-' '|  ||  | 
`--'     .-'  /   `-------'  `----' `--''--'.`-  /  `----' `---' `--''--' 
         `---'                              `---'                       """)
    time.sleep(1) # Delay output by 1 sec
    print("To win in this game you need to survive throughout all the turns \n"
          "while gathering as much gold as you can\n")
    time.sleep(1) # Delay output by 1 sec
    print("Will you spend your gold to get stronger?\n"
          "Or will you save it for a higher score at the end??\n")
    time.sleep(1) # Delay output by 1 sec


def game():
    global Turns # Defined globally across all functions
    Turns = 0
    global computer # We use global so it is defined for other functions outside the game() function
    computer = Player("Computer")
    global human # otherwise we get an error "not defined"
    Name = input("Enter your name to begin: \t")
    human = Human(Name)
    human.modify_attack_damage() # applying the weapon data to the player
    human.modify_defence_pt() # applying the armor data to the player

    # allow the player to decide how many turns to play before the game is forced to end
    turns_to_play = int(input("Please enter how many turns you wish to play: \t"))
    Turns = 0
    while Turns <= turns_to_play and human.health_points > 0 :
        mainMenu()
        Turns += 1 # number of turns passed increase by 1 every turn
        computer.base_health_points += 2 # The enemy gets more max health per turn
        print("Number of Turns = " + str(Turns))
        print("The computer grows stronger by 2 health point!\n")

    # This prints at the end of the game
    print("\n__Game OVER !__\n")
    print("You had " + str(human.gold) + " Gold coins")
    score = ( Turns* 100 + human.gold*10 )
    print("Your Score is: " + str(score))

# The main menu of the game
def mainMenu():
    print("Game Shop (1)")
    print("Status Screen (2)")
    print("Inventory (3)")
    print("Continue Exploring (4)")
    mainChoice = input() # takes input from player to decide what to do next

    if mainChoice == "1":
        gameShop() # player enters the shop
    elif mainChoice == "2":
        status() # prints the player's statistics
    elif mainChoice == "3":
        inventory() # players access the inventory
    elif mainChoice == "4":
        explore() # starts a random event to progress through the game (Out of 4 events)
    else:
        print("Invalid Input! please choose from (1 to 4)\n")
        mainMenu() # force the player to repeat until a valid input is entered

def gameShop(): # buy and sell items from here
    print("Welcome to the game's shop !")
    print("You currently have " + str(human.gold) + " Gold !")
    print("What do you wish to do ?")
    print("Buy? (1)")
    print("Sell? (2)")
    print("Return to Main Menu ? (3)")
    shop_choice = input() # player input

    if shop_choice == "1":
        gameShop_buy() # buying choices here
    elif shop_choice == "2":
        gameShop_sell() # selling choices here
    elif shop_choice == "3":
        print("Returning you to the Main Menu")
        mainMenu() # return to the main menu
    else:
        print("Invalid Input! please choose from (1 to 3)\n")
        # return to gameShop until user request to go back to mainMenu
        gameShop()

def gameShop_buy(): # All buy choices are controlled from here
    print("What do you wish to buy?")
    print("Buy Weapons (1)")
    print("Buy Armors (2)")
    print("Buy Potions (3)")
    print("Return to the game's shop menu ? (4)")
    shop_buy_choice = input()

    if shop_buy_choice == "1":
        print("Choose which weapon you want to buy: ")
        for i in range(len(human.list0fWeapons)): # for the length of the list
            print(str(i + 1) + ":", human.list0fWeapons[i]) # print the items in the list while numbered
        print('Choose "5" to return to previus menu')

        weapon_choice = int(input("Enter a number: \t"))
        if weapon_choice in range(1, 5): # if a weapon number from the list was choosen
            weapon_choice = human.list0fWeapons[weapon_choice - 1]
            if human.gold >= weapon_choice.price: # if the player has enough gold
                human.gold -= weapon_choice.price # deduct the weapon price from the player's gold
                weapon_choice.amount += 1
                print(human.name + " bought " + weapon_choice.name + " for " + str(weapon_choice.price) + " gold !")
                gameShop_buy()
            else: # if the player doesn't have enough gold
                print("You don't have enough gold to purchase this weapon !")
                print("You only have " + str(human.gold) + " gold at this moment")
                gameShop_buy()
        elif weapon_choice == 5:
            print("Returning to previus Menu")
            gameShop_buy()

        else:
            print("Invalid input! please enter a valid number")
            gameShop_buy()

    elif shop_buy_choice == "2":
        print("Choose which armor you want to Buy: ")
        for i in range(len(human.list0fArmors)): # for the length of the list
            print(str(i + 1) + ":", human.list0fArmors[i]) # print all the armors while numbered
        print('Choose "5" to return to previus menu')

        armor_choice = int(input("Enter a number: \t"))
        if armor_choice in range(1, 5): # if the players choice was one of the armors
            armor_choice = human.list0fArmors[armor_choice - 1]
            if human.gold >= armor_choice.price: # if the player has enough gold
                human.gold -= armor_choice.price # deduct the armor's price from the players gold
                armor_choice.amount += 1
                print(human.name + " bought " + armor_choice.name + " for " + str(armor_choice.price) + " gold !")
                gameShop_buy()
            else: # if the player's gold is not enough
                print("You don't have enough gold to purchase this armor !")
                print("You only have " + str(human.gold) + " gold at this moment")
                gameShop_buy()
        elif armor_choice == 5:
            print("Returning to previus Menu")
            gameShop_buy()
        else:
            print("Invalid input! please enter a valid number !")
            gameShop_buy()

    elif shop_buy_choice == "3":
        print("Choose which potion you want to Buy: ")
        for i in range(len(human.list0fPotions)):
            print(str(i + 1) + ":", human.list0fPotions[i])
        print('Choose "4" to return to previous menu')

        potion_choice = int(input("Enter a number: \t"))
        if potion_choice in range(1, 4):
            potion_choice = human.list0fPotions[potion_choice - 1]
            if human.gold >= potion_choice.price:
                human.gold -= potion_choice.price
                potion_choice.amount += 1
                print(human.name + " bought " + potion_choice.name + " for " + str(potion_choice.price) + " gold !")
                gameShop_buy()
            else:
                print("You don't have enough gold to purchase this potion !")
                print("You only have " + str(human.gold) + " gold at this moment")
                gameShop_buy()
        elif potion_choice == 4:
            print("Returning to previous menu")
            gameShop_buy()
        else:
            print("Invalid input! please enter a valid number !")
            gameShop_buy()

    elif shop_buy_choice == "4":
        print("Returning you to the game's shop menu")
        gameShop()
    else:
        print("Invalid Input! please choose from (1 to 4)\n")
        gameShop_buy()
        # return to gameShop until user requests to go back to mainMenu


# follows the same idea as the gameShop_buy function
def gameShop_sell(): # All sell choices are controlled from here
    print("What do you wish to sell?")
    print("Know that you will lose half the item's gold value if you sell it")
    print("Example: Common Sword bought for 30g will sell for 15g only!")
    print("Sell Weapons (1)")
    print("Sell Armors (2)")
    print("Sell Potions (3)")
    print("Return to the game's shop menu ? (4)")
    shop_sell_choice = input()

    if shop_sell_choice == "1":
        print("Choose which weapon you want to sell: ")
        for i in range(len(human.list0fWeapons)):
            print(str(i + 1) + ":", human.list0fWeapons[i])
        print('Choose "5" to return to previus menu')

        weapon_choice = int(input("Enter a number: \t"))
        if weapon_choice in range(1, 5):
            weapon_choice = human.list0fWeapons[weapon_choice - 1]
            if weapon_choice.amount > 0: # if the player has at least 1 of the weapon
                human.gold += (weapon_choice.price//2) # increase the player's gold by half the item's price
                weapon_choice.amount -= 1
                print(human.name + " sold " + weapon_choice.name + " for " + str(weapon_choice.price//2) + " gold !")
                print("You now have " + str(human.gold) + " Gold !")
                gameShop_sell()
            else:
                print("You don't have any of this weapon to sell !")
                gameShop_sell()
        elif weapon_choice == 5:
            print("Returning to previus Menu")
            gameShop_sell()

        else:
            print("Invalid input! please enter a valid number")
            gameShop_sell()

    elif shop_sell_choice == "2":
        print("Choose which armor you want to sell: ")
        for i in range(len(human.list0fArmors)):
            print(str(i + 1) + ":", human.list0fArmors[i])
        print('Choose "5" to return to previus menu')

        armor_choice = int(input("Enter a number: \t"))
        if armor_choice in range(1, 5):
            armor_choice = human.list0fArmors[armor_choice - 1]
            if armor_choice.amount > 0:
                human.gold += (armor_choice.price//2)
                armor_choice.amount -= 1
                print(human.name + " sold " + armor_choice.name + " for " + str(armor_choice.price//2) + " gold !")
                print("You now have " + str(human.gold) + " Gold !")
                gameShop_sell()
            else:
                print("You don't have any of this armor to sell !")
                gameShop_sell()
        elif armor_choice == 5:
            print("Returning to previus Menu")
            gameShop_sell()
        else:
            print("Invalid input! please enter a valid number !")
            gameShop_sell()

    elif shop_sell_choice == "3":
        print("Choose which potion you want to Sell: ")
        for i in range(len(human.list0fPotions)):
            print(str(i + 1) + ":", human.list0fPotions[i])
        print('Choose "4" to return to previous menu')

        potion_choice = int(input("Enter a number: \t"))
        if potion_choice in range(1, 4):
            potion_choice = human.list0fPotions[potion_choice - 1]
            if potion_choice.amount > 0:
                human.gold += (potion_choice.price//2)
                potion_choice.amount -= 1
                print(human.name + " sold " + potion_choice.name + " for " + str(potion_choice.price//2) + " gold !")
                print("You now have " + str(human.gold) + " Gold !")
                gameShop_sell()
            else:
                print("You don't have any of this potion to sell !")
                gameShop_sell()
        elif potion_choice == 4:
            print("Returning to previous menu")
            gameShop_sell()
        else:
            print("Invalid input! please enter a valid number !")
            gameShop_sell()

    elif shop_sell_choice == "4":
        print("Returning you to the game's shop menu")
        gameShop()
    else:
        print("Invalid Input! please choose from (1 to 4)\n")
        gameShop_sell()


def status(): # prints the player status (HP, DMG, DODGE, equipped items, etc.)
    print("Number of Turns passed " + str(Turns) )
    print("Your Current Statistics:")
    print(human)
    mainMenu()


def inventory(): # change equipment and use potions from this menu
    print("You currently have a " + human.current_weapon.name + " and a " + human.current_armor.name + "  equipped")
    print("Equip a Weapon (1)")
    print("Equip an Armor (2)")
    print("Use a Potion (3)")
    print("Return to Main Menu (4)")


    inventory_choice = input()
    if inventory_choice == "1":
        for i in range(len(human.list0fWeapons)):
            print(str(i+1) + ":", human.list0fWeapons[i])

        weapon_to_equip_choice = int(input('Choose which weapon to equip\nChoose "5" to go back to previous menu\n'))

        if weapon_to_equip_choice in range(1,5):
            weapon_to_equip_choice = human.list0fWeapons[weapon_to_equip_choice-1]
            if weapon_to_equip_choice.amount > 0:
                human.current_weapon.amount += 1
                weapon_to_equip_choice.amount -= 1
                human.current_weapon = weapon_to_equip_choice
                print(human.name + " equipped " + weapon_to_equip_choice.name)

                human.modify_attack_damage() # Apply the new weapon's data to the player's statistics
            else:
                print("You currently don't have any " + weapon_to_equip_choice.name + " available to equip" )

        elif weapon_to_equip_choice == 5:
            print("Returning to inventory menu")
        else:
            print("Invalid Input ! Returning you to Inventory")

        inventory()

    elif inventory_choice == "2":
        for i in range(len(human.list0fArmors)):
            print(str(i+1) + ":", human.list0fArmors[i])


        armor_to_equip_choice = int(input('Choose which armor to equip\nChoose "5" to go back to previous menu\n'))

        if armor_to_equip_choice in range(1,5):
            armor_to_equip_choice = human.list0fArmors[armor_to_equip_choice-1]
            if armor_to_equip_choice.amount > 0:
                human.current_armor.amount += 1
                armor_to_equip_choice.amount -= 1
                human.current_armor = armor_to_equip_choice
                print(human.name + " equipped " + armor_to_equip_choice.name)

                human.modify_defence_pt() # Apply the new armor's data to the player's statistics
            else:
                print("You currently don't have any " + armor_to_equip_choice.name + " available to equip" )

        elif armor_to_equip_choice == 5:
            print("Returning to inventory menu")

        else:
            print("Invalid Input! Returning you to Inventory")

        inventory()

    elif inventory_choice == "3":
        if human.health_points < human.base_health_points:
            for i in range(len(human.list0fPotions)):
                print(str(i+1) + ":", human.list0fPotions[i])


            potion_to_use_choice = int(input('Choose which potion do you want to use\n'
                                             'Choose "4" to go back to previous menu\n'))

            if potion_to_use_choice in range(1,4):
                potion_to_use_choice = human.list0fPotions[potion_to_use_choice-1]
                if potion_to_use_choice.amount > 0:
                    potion_to_use_choice.amount -= 1
                    human.health_points = human.base_health_points \
                        if (human.health_points + potion_to_use_choice.restore_hp)> 100 \
                        else human.health_points + potion_to_use_choice.restore_hp

                    print(human.name + " used " + potion_to_use_choice.name +
                          " and restored " + str(potion_to_use_choice.restore_hp) + " Health Points !" )
                    print("You currently have "+ str(human.health_points) + " / " + str(human.base_health_points))

                else:
                    print("You currently don't have any " + potion_to_use_choice.name + " available to use" )
            elif potion_to_use_choice == 4:
                print("Returning to inventory menu")
            else:
                print("Invalid input, Returning you to Inventory")
        else:
            print("You are already at max health "+ str(human.health_points) + " / " + str(human.base_health_points))
        inventory()

    elif inventory_choice == "4":
        print("Returning you to main menu ")
        mainMenu()
    else:
        print("Invalid Input! please choose from (1 to 4)\n")
        inventory()


def explore(): # the main method to progress through the game
    random_encounter = random.randint(1,10)
    if random_encounter == 1:
        print(human.name +" got 50 gold !")
        human.gold += 50 # increase player gold by said amount
        human.get_reward()
    elif random_encounter == 2 or random_encounter == 3:
        print("You entered and empty room\n your turn was wasted !\n")
    elif random_encounter == 4 or random_encounter == 5:
        fight()
        print(human.name +" got 20 gold !")
        human.gold += 20
        human.get_reward()
    elif random_encounter == 6 or random_encounter == 7 or random_encounter == 8 or random_encounter == 9 or random_encounter == 10:
        fight()
        print(human.name + " got 10 gold !")
        human.gold += 10


def fight():
    print("An Enemy Has Appeared !!!")
    computer.health_points = computer.base_health_points
    while human.health_points > 0 and computer.health_points > 0:
        print(human.name +" : "+ str(human.health_points) + " / " + str(human.base_health_points))
        print(computer.name +" : "+ str(computer.health_points) + " / " + str(computer.base_health_points))
        print("What will you do ?")
        print('(1) Attack "Attempt to defeat the enemy')
        print("(2) Check enemy statistics")
        print('(3) Use a potion "You will forfit your turn" ')
        print('(4) Run "Sacrifice your turn for a chance to runaway')
        player_choice = input()


        if player_choice == "1":
            human.attack(computer)
            computer.attack(human)

        elif player_choice == "2":
            print(computer)

        elif player_choice == "3":
            if human.health_points < human.base_health_points:
                for i in range(len(human.list0fPotions)):
                    print(str(i + 1) + ":", human.list0fPotions[i])

                potion_to_use_choice = int(input('Choose which potion do you want to use\nPress "4" to cancel\n') )

                if potion_to_use_choice in range(1, 4):
                    potion_to_use_choice = human.list0fPotions[potion_to_use_choice - 1]
                    if potion_to_use_choice.amount > 0:
                        potion_to_use_choice.amount -= 1
                        human.health_points = human.base_health_points \
                            if (human.health_points + potion_to_use_choice.restore_hp) > 100 \
                            else human.health_points + potion_to_use_choice.restore_hp

                        print(human.name + " used " + potion_to_use_choice.name +
                              " and restored " + str(potion_to_use_choice.restore_hp) + " Health Points !")

                        computer.attack(human)
                    else:
                        print("You currently don't have any " + potion_to_use_choice.name + " available to use")
                elif potion_to_use_choice == 4:
                    pass
                else:
                    print("Invalid input ! , please enter a valid input (1-4)")
            else:
                print(
                    "You are already at max health " + str(human.health_points) + " / " + str(human.base_health_points))

        elif player_choice == "4":
            run_attempt = random.randint(1,3)
            if run_attempt == 1:
                print("You have successfully ran away !")
                break
            else:
                print("You failed to escape !\nThe Enemy attacks!")
                computer.attack(human)
        else:
            print("Invalid Input ! Please Choose a valid input (1-4)")


