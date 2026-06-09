import time
from player import create_player


def start_game():
    player = create_player()

    print("Welcome to Lost Celta.")
    time.sleep(2)
    print("You can feel a coil around your soul.")

    print("We welcome you.")

    while True:
        options = input(
            "1. Delve deeper into New Kyrsa\n"
            "2. View your current Stats and Talents\n"
            "3. View your inventory\n"
            "4. Quit\n"
            "> "
        )

        if options == "1":
            print("You enter the mist... something watches you.")
            time.sleep(2)

        elif options == "2":
            print("Your current stats are:")
            print("Strength:", player["strength"])
            print("Agility:", player["agility"])
            print("HP:", player["hp"])

        elif options == "3":
            print("Your inventory:", player["inventory"])

        elif options == "4":
            print("Quitting the game.")
            break

        else:
            print("Invalid option.")