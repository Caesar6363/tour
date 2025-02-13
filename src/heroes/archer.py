from src.heroes.hero_interface import BaseHero
from src.models.stats import HeroesStats

class Archer(BaseHero):
    def __init__(
            self,
            stats: HeroesStats,
            agility: int
    ):
        super().__init__(stats)

        self.agility = agility

    def __repr__(self):
        return (f"Имя: {self.name}, Ник: {self.nickname}, HP: {self.hp}, Оружие: {self.weapon_type}, "
                f"Ловкость: {self.agility}, Урон {self.damage}")
