import json
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        pass
    def make_sound(self):
        pass

    def to_json(self):
        return json.dumps({"name": self.name, "age": self.age})
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("Kar-Kar")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("Urrrr Urrrr Urrrr")


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("Shhhhhhhhhhhhhh")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animalsList = {Bird("Bird", 6), Mammal("Mammal", 6), Reptile("Reptile",7) }
animal_sound(animalsList)

class Worker():
    def __init__(self, mame, age):
        self.mame = mame
        self.age = age
    def to_json(self):
        return json.dumps({"mame": self.mame, "age": self.age})
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)
class Zoo():
    def __init__(self):
        self.__AnimalsLict = list()
        self.__WorkersList = list()
    def add_worker(self, name, age):
        self.__WorkersList.append(Worker(name, age))
        print(name + " теперь работает в зоопарке.")
    def add_animal(self, name, age):
        self.__AnimalsLict.append(Animal(name, age))
        print(name + " теперь живет в зоопарке.")

    def write_to_file(self, filename):
        users_json = [Animal.to_json() for Animal in self.__AnimalsLict]
        products_json = [Worker.to_json() for Worker in self.__WorkersList]

        with open(filename, "w") as file:
            json.dump({"users": users_json, "products": products_json}, file)

    def load_from_file(self, filename):
        # Чтение из файла и десериализация
        with open(filename, "r") as file:
            data = json.load(file)
            self.__AnimalsLict = [Animal.from_json(user) for user in data["users"]]
            self.__WorkersList = [Worker.from_json(product) for product in data["products"]]
    def print(self):
        animals_name = "Звери: "
        workers_name = "Рабочие: "
        for user in self.__AnimalsLict:
            animals_name = animals_name + str(user.name) + " "
        for user in self.__WorkersList:
            workers_name = workers_name + str(user.mame) + " "
        print(animals_name,"////////",  workers_name)
    def clear_all(self):
        self.__AnimalsLict.clear()
        self.__WorkersList.clear()

class ZooKeeper(Worker):
    def __init__(self, name, age):
        super().__init__(name, age)
    def feed_animal(self, animal):
        print(self.mame + " кормит "+animal.name)

class Veterinarian(Worker):
    def __init__(self, name, age):
        super().__init__(name, age)
    def heal_animal(self, animal):
        print(self.mame + " лечит "+animal.name)

ourZoo = Zoo()
ourZoo.add_animal("Кеша", 3)
ourZoo.add_animal("Гоша", 4)
ourZoo.add_animal("Маркоша", 5)

ourZoo.add_worker("Петя", 25)
ourZoo.add_worker("маша", 25)

Bird = Bird("Птичка", 6)
Vet = Veterinarian("Витя",30)
ZK = ZooKeeper("Коля",30)

Vet.heal_animal(Bird)
ZK.feed_animal(Bird)


ourZoo.write_to_file("output1.txt")
ourZoo.print()
ourZoo.clear_all()
ourZoo.print()
ourZoo.load_from_file("output1.txt")
ourZoo.print()