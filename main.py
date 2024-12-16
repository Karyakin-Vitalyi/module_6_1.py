# Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверяем начальные значения
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик
print(a1.alive)  # True
print(a2.fed)  # False

# Выполняем действия
a1.eat(p1)  # Волк с Уолл-Стрит пытается съесть цветок
a2.eat(p2)  # Хатико ест фрукт

# Проверяем конечные значения
print(a1.alive)  # False
print(a2.fed)  # True


