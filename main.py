from character import Player, Monster

class Game:
    def __init__(self):
        self.player=Player("Hero",100,15,50)
        self.monster=Monster("Goblin",50,8,"Dragon")

    def __str__(self):
        return f"{self.player} <-vs-> {self.monster}"

    def start_game_loop(self):
        while self.player.is_alive() and self.monster.is_alive():
            print("\n--- Player's Turn ---")
            choice=input("Choose your action:\n1. Attack\n2. Cast Spell\nChoice:")
            if choice=="1":
                self.player.attack(self.monster)
            elif choice=="2":
                self.player.cast_spell(self.monster)
            else:
                print("Invalid choice. Skipping turn.")
                continue

            if not self.monster.is_alive():
                print(f"You defeated the {self.monster.name}!")
                break

            print("\n--- Monster's Turn ---")

            self.monster.attack(self.player)

            if not self.player.is_alive():
                print(f"You have been defeated by the {self.player.name}!")
                break

if __name__=='__main__':
    game=Game()
    game.start_game_loop()




