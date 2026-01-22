import random
def create_character():
    name = input("Введи ім'я героя: ")
    return {
        "name": name,
        "hp": 100,
        "attack": 15,
        "gold": 0
    }
def show_status(player):
    print("\n Статус героя")
    print(f"Ім'я: {player['name']}")
    print(f"HP: {player['hp']}")
    print(f"Атака: {player['attack']}")
    print(f"Золото: {player['gold']}\n")
def choose_action():
    print("Оберіть дію:")
    print("1 — Атакувати")
    print("2 — Захищатися")
    print("3 — Втекти")
    try:
        choice = int(input("Ваш вибір: "))
        if choice not in (1, 2, 3):
            raise ValueError
        return choice
    except ValueError:
        print(" Введіть число 1, 2 або 3.")
        return None
def fight(player):
    enemy_hp = random.randint(30, 60)
    enemy_attack = random.randint(5, 12)
    print("\nВи зустріли ворога!")
    while enemy_hp > 0 and player["hp"] > 0:
        action = None
        while action is None:
            action = choose_action()
        if action == 1: 
            damage = player["attack"]
            enemy_hp -= damage
            print(f" Ви завдали {damage} шкоди ворогу!")
        elif action == 2: 
            reduced = enemy_attack // 2
            player["hp"] -= reduced
            print(f" Ви захистились і отримали {reduced} шкоди.")
        elif action == 3: 
            if random.random() < 0.5:
                print(" Ви успішно втекли!")
                return True
            else:
                print(" Втеча не вдалася!")
        if enemy_hp > 0:
            player["hp"] -= enemy_attack
            print(f"Ворог атакує та завдає {enemy_attack} шкоди!")
        print(f"HP героя: {player['hp']} | HP ворога: {enemy_hp}")
    if player["hp"] <= 0:
        return False
    print(" Ворог переможений!")
    gold = random.randint(10, 25)
    player["gold"] += gold
    print(f" Ви отримали {gold} золота!")
    return True
def end_game(player):
    if player["hp"] <= 0:
        print("\n Ви програли. Герой загинув.")
    else:
        print("\nВітаємо! Ви перемогли у цій пригоді.")
    print("Кінець гри.")
def game():
    player = create_character()
    game_running = True
    while game_running and player["hp"] > 0:
        show_status(player)
        survived = fight(player)
        if not survived:
            break
        choice = input("\nХочете продовжити гру? (y/n): ").lower()
        if choice != "y":
            game_running = False
    end_game(player)
game()
