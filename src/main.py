from src.heroes_generator import HeroesGenerator
from src.tournamnet import Fight



def main():
    generator = HeroesGenerator()
    heroes = generator.get_heroes(2)


    fight = Fight()
    fight.tournament(heroes)

main()
