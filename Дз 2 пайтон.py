import random
import time

class Cat:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.hunger = 50
        self.thirst = 50
        self.energy = 50
        self.toilet_need = 0

    def status(self):
        print(f"\n--- Стан {self.name} ---")
        print(f"Голод: {self.hunger} | Спрага: {self.thirst} | Енергія: {self.energy} | Потреба в лотку: {self.toilet_need}")

    def eat(self):
        print(f"[{self.name}] Їсть смачний корм...")
        self.hunger = max(0, self.hunger - 30)
        self.toilet_need += 20

    def drink(self):
        print(f"[{self.name}] П'є водичку...")
        self.thirst = max(0, self.thirst - 30)
        self.toilet_need += 15

    def play(self):
        print(f"[{self.name}] Ганяється за лазерною указкою!")
        self.energy = max(0, self.energy - 30)
        self.hunger += 20
        self.thirst += 20

    def sleep(self):
        print(f"[{self.name}] Спить і муркоче...")
        self.energy = min(100, self.energy + 40)
        self.hunger += 10

    def go_to_toilet(self):
        print(f"[{self.name}] Пішов у лоток. Полегшення!")
        self.toilet_need = 0

my_cat = Cat("Мурчик", 2, "25 см")
actions = [my_cat.eat, my_cat.drink, my_cat.play, my_cat.sleep, my_cat.go_to_toilet]

for _ in range(5):
    random_action = random.choice(actions)
    random_action()
    my_cat.status()
    time.sleep(1)
