from src.heroes.hero_interface import BaseHero
from src.models.stats import HeroesStats

class Warrior(BaseHero):
    def __init__(
            self,
            stats: HeroesStats,
            strength: int
    ):
        super().__init__(stats)

        self.strength = strength

    def __repr__(self):
        return (f"Имя: {self.name}, Ник: {self.nickname}, HP: {self.hp}, Оружие: {self.weapon_type}, "
                f"Сила: {self.strength}, Урон {self.damage}")
