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
                print(f"Игрок {player1.name} {player1.nickname} проигрывает бой и вылетает с турнира")
                break

            self.hit(player1, player2)

            if player2.hp <= 0:
                print(f"Игрок {player2.name} {player2.nickname} проигрывает бой и вылетает с турнира")
                break
            print()
            self.print_hp(player1, player2)

        if player1.hp > 0:
            player1.hp = 100
            return player1

        player2.hp = 100
        return player2

    @staticmethod
    def hit(
            player1: Mage | Archer | Warrior,
            player2: Mage | Archer | Warrior
    ):
        r_damage_p1 = r.choice(player1.damage)
        r_crit_damage_p1 = r.choice(player1.critical_damage_chance)
        sum_damage_crit1 = r_damage_p1 + r_crit_damage_p1
        sum_dodge_block1 = player2.dodge_chance + player2.block_chance
        player1_damage = sum_damage_crit1 - sum_dodge_block1
        player1_damage = max(player1_damage, 0)

        player2.hp -= player1_damage
        # self.print_hit(player1, player2)
        print()
        print(f'Игрок {player1.name} {player1.nickname} нанес удар, '
              f'Нанес урона: {r_damage_p1}, крит {r_crit_damage_p1} Оружием: {player1.weapon_type},'
              f' Игроку: {player2.name}')
        print(f'Игрок {player2.name} {player2.nickname} '
              f'получил с удара {sum_damage_crit1} урона, '
              f'но смог заблокировать {sum_dodge_block1} урона. '
              f'Полученный урон {player1_damage}')

        r_damage_p2 = r.choice(player2.damage)
        r_crit_damage_p2 = r.choice(player2.critical_damage_chance)
        sum_damage_crit2 = r_damage_p2 + r_crit_damage_p2
        sum_dodge_block2 = player1.dodge_chance + player1.block_chance
        player2_damage = sum_damage_crit2 - sum_dodge_block2
        player2_damage = max(player2_damage, 0)
        player1.hp -= player2_damage
        # self.print_hit(player2, player1)
        print()
        print(f'Игрок {player2.name} {player2.nickname} нанес удар, '
              f'Нанес урона: {r_damage_p2}, крит {r_crit_damage_p2} Оружием: {player1.weapon_type},'
              f' Игроку: {player1.name}')
        print(f'Игрок {player1.name} {player1.nickname} '
              f'получил с удара {sum_damage_crit2} урона, '
              f'но смог заблокировать {sum_dodge_block2} урона. '
              f'Полученный урон {player2_damage}')



    def input_info(self, player1, player2):
        print()
        print(f"Раунд {self.rounds}\n\nИмя первого игрока: {player1.name}, Никнейм первого игрока: {player1.nickname}\n"
              f"Имя второго игрока: {player2.name}, Никнейм второго игрока: {player2.nickname}")


    #
    # @staticmethod
    # def print_hit(player1, player2):

        # time.sleep(2)
        # damage = r.choice(player1.damage)
        # crit = r.choice(player1.critical_damage_chance)
        # print(f'Игрок {player1.name} {player1.nickname} нанес удар, '
        #       f'Нанес урона: {damage}, крит {crit} Оружием: {player1.weapon_type},'
        #       f' Игроку: {player2.name}')


    @staticmethod
    def print_hp(player1, player2):
        # time.sleep(2)
        print(f"Здоровье игрока {player1.name} {player1.nickname}: {player1.hp}")
        print(f"Здоровье игрока {player2.name} {player2.nickname}: {player2.hp}")


    @staticmethod
    def winner(player):

        if len(player) <= 1:
            # time.sleep(2)
            print()
            print(f"Победитель турнира: {player[0].name} {player[0].nickname}")
