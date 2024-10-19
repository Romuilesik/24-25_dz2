import random

class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 50
        self.energy = 100
        self.money = 50

    def study(self):
        self.knowledge += 10
        self.energy -= 15
        print(f"{self.name} is studying. Knowledge: {self.knowledge}, Energy: {self.energy}")

    def work(self):
        self.money += 20
        self.energy -= 20
        print(f"{self.name} is working. Money: {self.money}, Energy: {self.energy}")

    def rest(self):
        self.energy += 20
        self.money -= 10
        print(f"{self.name} is resting. Energy: {self.energy}, Money: {self.money}")

    def status(self):
        print(f"{self.name} - Knowledge: {self.knowledge}, Energy: {self.energy}, Money: {self.money}")

    def live_a_year(self):
        for day in range(365):
            if self.money < 20:
                self.work()
            elif self.knowledge < 60:
                self.study()
            else:
                action = random.choice([self.study, self.rest, self.work])
                action()
            if self.energy < 30:
                self.rest()
            print(f"Day {day+1} - {self.name}'s status:")
            self.status()

student = Student("John")
student.live_a_year()
