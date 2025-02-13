from src.heroes.hero_interface import BaseHero
from src.models.stats import HeroesStats
class Mage(BaseHero):
    def __init__(
            self,
            stats: HeroesStats,
            intelligence: int
    ):
        super().__init__(stats)

        self.intelligence = intelligence

    def __repr__(self):
        return (f"Имя: {self.name}, Ник: {self.nickname}, HP: {self.hp}, Оружие: {self.weapon_type}, "
                f"Интеллект: {self.intelligence}, Урон {self.damage}")

