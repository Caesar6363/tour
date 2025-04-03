import random as r


names = ["Ульрих", "Ричард", "Раймунд", "Уильям", "Эдуард ", "Бертран ", "Готфрид ", "Жак"]
nicknames = ["Гордый", "Бодрый", "Справедливый", "Лысый", "Смелый", "Быстрый", "Великий", "Одноглазый"]
weapon_types = ["Меч", "Двуручный_меч", "Парные_клинки", "Секира", "Булава", "Рапира",
                "Сабля", "Палка", "Лук", "Арбалет", "Сюрикен", "Рогатка"]

class HeroesStats:

    name: str = r.choice(names)
    nickname: str = r.choice(nicknames)
    hp: int = 100
    weapon_type: str = r.choice(weapon_types)
    mana_pool: int = 50
    damage: list = [10, 11, 12, 13, 14, 15]
    armor: int = 50
    dodge_chance: int = r.randint(0, 5)
    block_chance: int = r.randint(0, 8)
    critical_damage_chance: list = [10, 11, 12, 13, 14, 15]


    def __init__(self):
        self.name = r.choice(names)
        self.nickname = r.choice(nicknames)
        self.hp = 100
        self.weapon_type = r.choice(weapon_types)
        self.mana_pool = 50
        self.damage = [10, 11, 12, 13, 14, 15]
        self.armor = 50
        self.dodge_chance = r.randint(0, 5)
        self.block_chance = r.randint(0, 8)
        self.critical_damage_chance = [10, 11, 12, 13, 14, 15]
