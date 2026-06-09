def create_player():
    name = input("Enter your name: ")
    player = {
        "name": name,
        "hp": 100,
        "maxHp": 500,
        "agility": 10,
        "strength": 1,
        "inventory": [],
        "talents": [],
        "power": 20
    }

    return player