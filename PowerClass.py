class Power:
    Energy = "50%"

    def __init__(self, speed, strength, agility):
        self.speed = speed
        self.strength = strength
        self.agility = agility

    def __str__(self):
        return f"({self.agility}, {self.speed}, {self.strength})"

    def __eq__(self, other):
        return self.speed == other.speed and self.strength == other.strength

    def __gt__(self, other):
        return self.speed > other.speed and self.strength > other.strength


power = Power(2.2, 100, 2000)
other = Power(2.2, 4, 3)
print(power.agility)
