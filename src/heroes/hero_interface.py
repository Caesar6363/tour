import random as r
from colorama import Fore
from src.models.stats import HeroesStats
from ..utils.set_color import Colored

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

    def defense(self, enemy, damage):
        block = self.dodge_chance + self.block_chance
        _damage = damage - block
        _damage = max(_damage, 0)
        print(f'{self.name}({Colored.red(self.hp)}) получает {Colored.custom(_damage, Fore.GREEN)}'
              f'({Colored.custom(block, Fore.BLACK)})'
              f' урона от {enemy.name}({Colored.red(enemy.hp)})')
        print('')
        self.hp = self.hp - _damage

    def attack(self, enemy):
        damage = r.choice(enemy.damage) + r.choice(enemy.critical_damage_chance)

        print(f'{self.name}({Colored.red(self.hp)}) бьет {enemy.name} на {Colored.custom(damage, Fore.GREEN)} урона')
        enemy.defense(self, damage)

    def regen_hp(self, amount=None):
        if amount:
            self.hp += amount
            return self.hp
        self.hp = 100
        return self.hp
        
    
    def __repr__(self):
        return f"Имя: {self.name}, Ник: {self.nickname}, HP: {self.hp}, Оружие: {self.weapon_type}"


    