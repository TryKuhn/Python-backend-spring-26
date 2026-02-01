from pathlib import Path


class User:
    def __init__(self, nickname: str, strength: int, agility: int, intelligence: int, luck: int, health: int,
                 experience: int):
        self.nickname = nickname
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.luck = luck
        self.health = health
        self.experience = experience

        self.__max_health = 20

    def get_max_health(self):
        return self.__max_health


class Item:
    def __init__(self, id: int, count: int, path_to_image: Path):
        self.__id = id
        self.count = count
        self.__path_to_image = path_to_image

    def add_count(self, count: int):
        if count < 0:
            raise ValueError("Count to add must be non-negative")
        self.count += count

    def remove_count(self, count: int):
        if count < 0:
            raise ValueError("Count to remove must be non-negative")
        if count > self.count:
            raise ValueError("Cannot remove more items than available")
        self.count -= count


class Health(Item):
    def __init__(self, id: int, count: int, path_to_image: Path, health_points: int):
        super().__init__(id, count, path_to_image)

        if health_points < 0:
            raise ValueError("Health points must be non-negative")

        self.health_points = health_points

    def eat_food(self, user: User):
        user.health = min(self.health_points + user.health, user.get_max_health())


class Strength(Item):
    def __init__(self, id: int, count: int, path_to_image: Path, strength_points: int):
        super().__init__(id, count, path_to_image)
        self.strength_points = strength_points


class Experience(Item):
    pass


class Agility(Item):
    pass


class Intelligence(Item):
    pass


class Luck(Item):
    pass
