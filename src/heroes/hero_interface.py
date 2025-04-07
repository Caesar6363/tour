import random as r
from typing import Self
from src.models.stats import HeroesStats
class BaseHero:

    def __init__(
            self,
            stats: HeroesStats
    ):

        self.name = stats.name
        self.nickname = stats.nickname
        self.hp = stats.hp
        self.weapon_type = stats.weapon_type
        self.mana_pool = stats.mana_pool
        self.damage = stats.damage
        self.armor = stats.armor
        self.dodge_chance = stats.dodge_chance
        self.block_chance = stats.block_chance
        self.critical_damage_chance = stats.critical_damage_chance

    def defense(self, mySelf, damage):
        _damage = damage - (self.dodge_chance + self.block_chance)
        print(f'{self.name}({self.hp}) блокирует {mySelf.name} и получает {_damage} урона')
        print('')
        self.hp = self.hp - _damage

    def attack(self, enemy):
        player2 = enemy
        damage = r.choice(player2.damage) + r.choice(player2.critical_damage_chance)

        print(f'{self.name}({self.hp}) бьет {player2.name} на {damage} урона')
        player2.defense(self, damage)
    
    def __repr__(self):
        return f"Имя: {self.name}, Ник: {self.nickname}, HP: {self.hp}, Оружие: {self.weapon_type}"


    