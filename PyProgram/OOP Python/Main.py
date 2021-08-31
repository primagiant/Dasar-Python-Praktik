class Hero:
    jumlahHero = 0

    def __init__(self, inputnName, inputHealth, inputDamage):
        self.name = inputnName
        self.health = inputHealth
        self.damage = inputDamage

    def Attack(self, target):
        print(target.health - self.damage)


hero1 = Hero("Apu", 200, 12)
hero2 = Hero("Batu", 300, 4)

hero1.Attack(hero2)
