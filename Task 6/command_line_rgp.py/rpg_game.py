# This is Task 6 project
""" 6. Command-Line RPG Game
 ● Description      : Design a role-playing game where players explore a text-based world, fight
                      enemies, and collect items to progress.
 ● Challenges:
                    ○ Create a dynamic map with different locations and events.
                    ○ Implement a combat system with health, attack, and defense stats.
                    ○ Saveandload game progress.
 ● Skills:           Object-oriented programming, file handling, and game mechanics.
6. Command-Line RPG Game
                    ● Restriction: Text-based interface only (no graphical user interface).
                    ● Reason: Bylimiting the project to a command-line interface, students are forced to
                    focus on game mechanics like combat, item management, and world-building. This
                    helps build logical thinking and complex program structures without the distraction of
                    graphics. The project teaches how to design games that depend entirely on logic and
                    text-based feedback.
 ● Learning Outcome  : Students will learn to develop interactive games, utilize
                        object-oriented programming (OOP) for characters and items, and implement game
                        mechanics like turn-based combat and inventory systems."""

import json
import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15, 5)
        self.inventory = {"Potion": 3}
        self.location = "Village"

    def use_item(self, item):
        if item == "Potion" and self.inventory.get("Potion", 0) > 0:
            self.heal(20)
            self.inventory["Potion"] -= 1
            print(f"\nYou used a Potion! Health: {self.health}/{self.max_health}")
        else:
            print("\nYou don't have that item!")

class Enemy(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

class RPGGame:
    def __init__(self):
        self.player = Player(input("Enter your character's name: "))
        self.map = {
            "Village": ["Forest", "Cave"],
            "Forest": ["Village", "Castle"],
            "Cave": ["Village"],
            "Castle": ["Forest"]
        }
        self.enemies = {
            "Forest": Enemy("Goblin", 50, 10, 2),
            "Cave": Enemy("Troll", 80, 12, 3),
            "Castle": Enemy("Dark Knight", 120, 18, 5)
        }

    def save_game(self):
        data = {
            "name": self.player.name,
            "health": self.player.health,
            "inventory": self.player.inventory,
            "location": self.player.location
        }
        with open("savegame.json", "w") as file:
            json.dump(data, file)
        print("\nGame Saved!")

    def load_game(self):
        try:
            with open("savegame.json", "r") as file:
                data = json.load(file)
                self.player.name = data["name"]
                self.player.health = data["health"]
                self.player.inventory = data["inventory"]
                self.player.location = data["location"]
            print("\nGame Loaded!")
        except FileNotFoundError:
            print("\nNo saved game found.")

    def travel(self):
        print(f"\nCurrent Location: {self.player.location}")
        print(f"Available Places: {', '.join(self.map[self.player.location])}")
        destination = input("Where do you want to go? ").capitalize()
        
        if destination in self.map[self.player.location]:
            self.player.location = destination
            print(f"\nYou traveled to {destination}.")
            self.explore()
        else:
            print("\nInvalid location!")

    def explore(self):
        if self.player.location in self.enemies:
            print(f"\nA wild {self.enemies[self.player.location].name} appears!")
            self.fight(self.enemies[self.player.location])
        else:
            print("\nThis place seems peaceful.")

    def fight(self, enemy):
        while self.player.is_alive() and enemy.is_alive():
            print(f"\n{self.player.name} - HP: {self.player.health}/{self.player.max_health}")
            print(f"{enemy.name} - HP: {enemy.health}/{enemy.max_health}")
            action = input("Attack (A) / Use Potion (P): ").upper()

            if action == "A":
                damage = max(0, self.player.attack - enemy.defense)
                enemy.take_damage(damage)
                print(f"\nYou attacked {enemy.name} for {damage} damage!")

            elif action == "P":
                self.player.use_item("Potion")
            
            if enemy.is_alive():
                enemy_damage = max(0, enemy.attack - self.player.defense)
                self.player.take_damage(enemy_damage)
                print(f"\n{enemy.name} attacked you for {enemy_damage} damage!")

        if self.player.is_alive():
            print(f"\nYou defeated {enemy.name}!")
            del self.enemies[self.player.location]  # Remove enemy after defeat
        else:
            print("\nYou were defeated... Game Over!")
            exit()

    def start(self):
        while self.player.is_alive():
            print("\n1. Travel")
            print("2. Check Inventory")
            print("3. Save Game")
            print("4. Load Game")
            print("5. Quit")
            choice = input("\nEnter choice: ")

            if choice == "1":
                self.travel()
            elif choice == "2":
                print("\nInventory:", self.player.inventory)
            elif choice == "3":
                self.save_game()
            elif choice == "4":
                self.load_game()
            elif choice == "5":
                print("\nThanks for playing!")
                break
            else:
                print("\nInvalid choice!")

if __name__ == "__main__":
    game = RPGGame()
    game.start()
