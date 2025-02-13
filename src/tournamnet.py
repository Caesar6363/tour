import random as r
from src.heroes import (
    Archer,
    Mage,
    Warrior,
    BaseHero
)

class Fight:

    def __init__(self):
        self.rounds = 0



    def tournament(self, heroes: list[BaseHero]) -> tuple[BaseHero, BaseHero]:

        if len(heroes) > 1:
            while len(heroes) > 1:

                player1 = r.choice(heroes)
                heroes.remove(player1)
                player2 = r.choice(heroes)
                heroes.remove(player2)

                self.rounds += 1
                self.input_info(player1, player2)
                win = self.duel(player1, player2)
                heroes.append(win)
                self.winner(heroes)
        else:
            print("Недостаточно участников для проведения турнира. Прорекламируйте ваш турнир:)")


    def duel(
            self,
            player1: Mage | Archer | Warrior,
            player2: Mage | Archer | Warrior
    ) -> Mage | Archer | Warrior:

        while player1.hp > 0 and player2.hp > 0:

            self.hit(player1, player2)
            if player1.hp <= 0:
                break

            self.hit(player1, player2)

            if player2.hp <= 0:
                break

            self.print_hp(player1, player2)

        if player1.hp > 0:
            player1.hp = 100
            return player1

        player2.hp = 100
        return player2


    def hit(
            self,
            player1: Mage | Archer | Warrior,
            player2: Mage | Archer | Warrior
    ):

        player2.hp -= player1.damage
        self.print_hit(player1, player2)
        player1.hp -= player2.damage
        self.print_hit(player2, player1)


    def input_info(self, player1, player2):

        print(f"Раунд {self.rounds}\nИмя первого игрока: {player1.name}, Никнейм первого игрока: {player1.nickname}\n"
              f"Имя второго игрока: {player2.name}, Никнейм второго игрока: {player2.nickname}")



    @staticmethod
    def print_hit(player1, player2):

        print(f'Игрок {player1.name} {player1.nickname} нанес удар, '
              f'Нанес урона: {player1.damage}, Оружием: {player1.weapon_type},'
              f' Игроку: {player2.name}')


    @staticmethod
    def print_hp(player1, player2):

        print(f"Здоровье игрока {player1.name} {player1.nickname}: {player1.hp}")
        print(f"Здоровье игрока {player2.name} {player2.nickname}: {player2.hp}")


    @staticmethod
    def winner(player):

        if len(player) <= 1:
            print(f"Победитель турнира: {player}")
