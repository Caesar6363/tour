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

    def __repr__(self):
        return f"Имя: {self.name}, Ник: {self.nickname}, HP: {self.hp}, Оружие: {self.weapon_type}"


    