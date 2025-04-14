import random as r
from src.heroes import Archer, Mage, Warrior, BaseHero

from src.models.stats import HeroesStats


class HeroesGenerator:

    @staticmethod
    def _get_challenger():

        intelligence = r.randint(20, 100)
        agility = r.randint(20, 100)
        strength = r.randint(20, 100)

        hero = [
            Mage(HeroesStats(), intelligence),
            Archer(HeroesStats(), agility),
            Warrior(HeroesStats(), strength),
        ]

        return r.choice(hero)

    def get_heroes(self, challenger: int) -> list[BaseHero]:

        return [self._get_challenger() for _ in range(challenger)]
