from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()
        # self.shelter = Queue()

    def enqueue(self,animal):
        if animal.type == 'dog':
            self.dog.enqueue(animal)
        elif animal.type == 'cat':
            self.cat.enqueue(animal)

    def dequeue(self,pref):
        if pref == 'cat':
            return self.cat.dequeue()
        elif pref == 'dog':
            return self.dog.dequeue()

class Dog:
    def __init__(self,name=None):
        self.type = "dog"
        self.name = name


class Cat:
    def __init__(self,name=None):
        self.type = "cat"
        self.name = name
