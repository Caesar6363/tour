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
    damage: int = r.randint(10, 20)
    armor: int = 150
    dodge_chance: int = r.randint(1, 6)
    block_chance: int = r.randint(1, 10)
    critical_damage_chance: int = r.randint(1, 20)


    def __init__(self):
        self.name = r.choice(names)
        self.nickname = r.choice(nicknames)
        self.hp = 100
        self.weapon_type = r.choice(weapon_types)
        self.mana_pool = 50
        self.damage = r.randint(10, 20)
        self.armor = 150
        self.dodge_chance = r.randint(1, 6)
        self.block_chance = r.randint(1, 10)
        self.critical_damage_chance = r.randint(1, 20)


