import random as r
from src.heroes import (
    Archer,
    Mage,
    Warrior,
    BaseHero
)
from colorama import Fore

class Fight:

    def __init__(self):
        self.rounds = 0

    @staticmethod
    def get_players(heroes: list[BaseHero]) -> list[BaseHero] | None:
        if len(heroes) <= 1:
            return print("Нет участников для проведения турнира. Прорекламируйте ваш турнир:)")

        player1 = r.choice(heroes)
        heroes.remove(player1)
        player2 = r.choice(heroes)
        heroes.remove(player2)

        return [player1, player2]

    def tournament(self, heroes: list[BaseHero]):
        
        [player1, player2] = self.get_players(heroes)

        self.rounds += 1
        self.input_info(player1, player2)
        win = self.duel(player1, player2)
        self.winner(win)



    @staticmethod
    def duel(
            player1: Mage | Archer | Warrior,
            player2: Mage | Archer | Warrior
    ) -> Mage | Archer | Warrior:
        
        while player1.hp > 0 and player2.hp > 0:
            if player2.hp > 0:
                player1.attack(player2)
                if player2.hp <= 0:
                    print(f'{player2.name} покинул турнир')
                    player2.set_dead(True)
                    player1.regen_hp()

                    return player1

            if player1.hp > 0:
                player2.attack(player1)
                if player1.hp <= 0:
                    print(f'{player1.name} покинул турнир')
                    player1.set_dead(True)
                    player2.regen_hp()
                    return player2

        # Реализовать хп регенерацию в соответствие с Димой идея
        # Победивший 100 хп
        # Проигравший регенерацию со временем


    def input_info(self, player1, player2):
        print(f"Раунд {self.rounds}\n\nИмя первого игрока: {player1.name}, Никнейм первого игрока: {player1.nickname}\n"
              f"Имя второго игрока: {player2.name}, Никнейм второго игрока: {player2.nickname}\n")


    @staticmethod
    def print_hp(player1, player2):
        print(Fore.GREEN + f"Здоровье игрока {player1.name} {player1.nickname}: {player1.hp}")
        print(Fore.GREEN + f"Здоровье игрока {player2.name} {player2.nickname}: {player2.hp}")


    @staticmethod
    def winner(player):
        print(f"Победитель турнира: {player.name} {player.nickname} {player.hp}")
