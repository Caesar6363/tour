import random as r
from src.heroes import (
    Archer,
    Mage,
    Warrior,
    BaseHero
)

from src.models.stats import HeroesStats


class HeroesGenerator:

    @staticmethod
    def _get_challenger():

        intelligence = 100
        agility = 40
        strength = 200


        hero = [Mage(HeroesStats(), intelligence),
                Archer(HeroesStats(), agility),
                Warrior(HeroesStats(), strength)]


        return r.choice(hero)





    def get_heroes(self, challenger: int) -> list[BaseHero]:

        return [self._get_challenger() for _ in range(challenger)]

