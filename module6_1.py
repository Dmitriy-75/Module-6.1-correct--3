class Animal:

    def __init__(self, name, alive, fed):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):

        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}  не стал есть {food.name}')
            self.alive = False


class Mammal(Animal):
   pass
class Predator(Animal):
    pass



class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
class Flower(Plant):
   pass

class Vegetables(Plant):
   pass


Vegetables.edible = True

a1 = Predator('Волк с Ну погоди',True,False)
a2 = Mammal('Заинька серенький (типа с песни),',True,False)
p1 = Flower('Ромашка')
p2 = Vegetables('Морковка')


print(a1.name)
print(p1.name)

print(a1.alive)   # Голодный волк жив?
print(a2.fed)     # а зайка сыт?

a1.eat(p1)
a2.eat(p2)

print(a1.alive)    # Голодный волк выжил, отказавшись от ромашки?
print(a2.fed)      # Наелся зайка морковкой?








