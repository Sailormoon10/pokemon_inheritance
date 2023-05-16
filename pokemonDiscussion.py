from random import random


class Pokemon:
    basic_attack = 'tackle'
    damage = 40

    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.paralyzed = False

    def __str__(self):
        return f"Name: {self.name}" \
               f"\nTrainer: {self.trainer}\nLevel: {self.level}" \
               f"\nHP: {self.hp}\nParalyzed: {self.paralyzed}"

    def speak(self):
        return self.name + '!'

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            return f'{self.name} used {self.basic_attack}!'
            other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            return self.name, ' fainted!'


class BugType(Pokemon):
    basic_attack = 'signal beam'
    probability = 0.1

    def __init__(self, name, trainer, hp):
        super().__init__(name, trainer)
        self.hp = hp
        self.confusion = False

    def __str__(self):
        return f"Type: Bug Pokemon" \
               f"\nName: {self.name}" \
               f"\nTrainer: {self.trainer}\nLevel: {self.level}" \
               f"\nHP: {self.hp}\nConfusion: {self.confusion}"

    def attack(self, other):
        super().speak()
        return f'{self.name} used {self.basic_attack} on {other.name}!'
        other.receive_damage(self.damage)
        if random() < self.probability and type(other) != BugType:
            other.confusion = True
            return other.name + " is confused!"


charizard = Pokemon("Charizard", "Liza")
venomoth = BugType('Venomoth', 'Amy', 70)

print(venomoth, '\n')
print(charizard)

"""Output:
Type: Bug Pokemon
Name: Venomoth
Trainer: Amy
Level: 1
HP: 70
Confusion: False 

Name: Charizard
Trainer: Liza
Level: 1
HP: 50
Paralyzed: False
"""
