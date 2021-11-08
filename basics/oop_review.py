
# OOP inheritance example

class Character:
    
    def __init__(self, name, max_health=100, max_damage=10):
        self.name = name
        self.max_health = max_health
        self.max_damage = max_damage

    def attack(self):
        print(f"{self.name} attacks for {self.max_damage}!")


class Knight(Character):

    def __init__(self, name, max_health=100, max_damage=10):
        Character.__init__(self, name, max_health, max_damage)


knight = Knight("Simon")

knight.attack()

