import time
from art import text2art
from colorama import Fore, Style

print("\n")
title = text2art("freak.farm")
print(Fore.GREEN + title + Style.RESET_ALL)

class Animal:
    def __init__(self, name, kind, current_weight, healthy_weight, pronoun="it", health=100):
        self.name = name
        self.kind = kind
        self.current_weight = current_weight
        self.healthy_weight = healthy_weight
        self.pronoun = pronoun
        self.health = health
    
    def feed(self, food=None):
        print(f"\n{self.name} is currently {self.current_weight} pounds.")
        print("Commencing care...")
        time.sleep(1.5)
        initial_weight = self.current_weight
        if self.current_weight > self.healthy_weight and food.quant < 0:
            while self.current_weight > self.healthy_weight and food.quant < 0:
                weight_loss = min(abs(food.quant), self.current_weight - self.healthy_weight)
                self.current_weight -= weight_loss
                food.quant += weight_loss
                print(f"Feeding {self.name} {food.type}... making {self.pronoun} LOSE weight!")
                time.sleep(1)
                print(f"Now {self.name} is {self.current_weight} pounds.\n")
                time.sleep(.5)
        elif self.current_weight < self.healthy_weight and food.quant > 0:
            while self.current_weight < self.healthy_weight and food.quant > 0:
                weight_gain = min(food.quant, self.healthy_weight - self.current_weight)
                self.current_weight += weight_gain
                food.quant -= weight_gain
                print(f"Feeding {self.name} {food.type}...")
                time.sleep(1)
                print(f"Now {self.name} is {self.current_weight} pounds.\n")
                time.sleep(.5)
                print(f"After feeding {self.name} {food.type}, {self.pronoun} is now {self.current_weight} pounds!\n")
                time.sleep(2)
        else:
            print(f"{self.name} is all good, and {self.pronoun} does not need food.\n")
            time.sleep(1)
        print(f"OH SHIT!! Weight change for {self.name}: {initial_weight} -> {self.current_weight}\n")
        time.sleep(.5)

    def medicate(self, med=None):
        print(f"\n{self.name} currently has {self.health} health.\n")
        print("Commencing care...")
        time.sleep(1.5)
        initial_health = self.health
        if self.health < 100:
            if med:
                while self.health < 100 and med.strength > 0:
                    self.health += med.strength
                    print(f"Administering {self.name} {med.scrip}...")
                    time.sleep(1)
                    print(f"Now {self.name} has {self.health} health.\n")
                    time.sleep(.5)
                print(f"After giving {self.name} {med.scrip}, {self.pronoun} now has {self.health} health!\n")
                time.sleep(2)
        else:
            print(f"{self.name} is all good, and {self.pronoun} does not need medicine.\n")
            time.sleep(1)
        print(f"OH FUCK!! Health change for {self.name}: {initial_health} -> {self.health}\n")
        time.sleep(.5)

class Food:
    def __init__(self, type, quant, price):
        self.type = type
        self.quant = quant
        self.price = price

class Med:
    def __init__(self, scrip, strength, cost):
        self.scrip = scrip
        self.strength = strength
        self.cost = cost

def find_best_food(animal):
    weight_diff = animal.current_weight - animal.healthy_weight
    if weight_diff < -0.3 * animal.healthy_weight:
        return max(foods, key=lambda f: f.quant)
    elif animal.current_weight < animal.healthy_weight:
        return min(foods, key=lambda f: f.price)
    elif animal.current_weight > 1.3 * animal.healthy_weight:
        return max(foods, key=lambda f: f.quant)
    elif animal.current_weight > animal.healthy_weight:
        return min(foods, key=lambda f: f.price)
    return None

def find_best_med(animal):
    health_diff = 100 - animal.health
    if health_diff > 60:
        return max(meds, key=lambda m: m.strength)
    elif health_diff > 0:
        return min(meds, key=lambda m: m.cost)
    return None

def feed_animals():
    for animal in animals:
        food = find_best_food(animal)
        if food:
            animal.feed(food)
        else:
            print(f"\n{animal.name} is chillin, {animal.pronoun} fine.\n")
        time.sleep(1)
        time.sleep(1)

def medicate_animals():
    for animal in animals:
        med = find_best_med(animal)
        if med:
            animal.medicate(med)
        else:
            print(f"\n{animal.name} is chillin, {animal.pronoun} fine.\n")
        time.sleep(1)
        time.sleep(1)

def add_animal():
    print("\nAdding a new animal...\n")
    name = input("Enter the animal's name: ")
    time.sleep(.3)
    kind = input("Enter the animal's kind: ")
    time.sleep(.3)
    while True:
            try:
                current_weight = int(input("Enter the animal's current weight (in pounds): "))
                if current_weight <= 0:
                    time.sleep(.5)
                    print("\nEnter a positive number for the weight, dumbass.")
                else:
                    break
            except ValueError:
                time.sleep(.5)
                print("\nInvalid input. You do know what numbers are, right? Enter one of those.")
            print("\n")
    time.sleep(.3)
    while True:
        try:
            healthy_weight = int(input("Enter the animal's healthy weight (in pounds): "))
            if healthy_weight <= 0:
                time.sleep(.5)
                print("\nEnter a positive number for the weight!! Like, come on!\n")
            else:
                break
        except ValueError:
            time.sleep(.5)
            print("\nInvalid input. I swear to god... A NUMBER.\n")
    time.sleep(.3)
    pronoun = input("Enter the animal's pronoun (e.g., 'he', 'she', 'it'): ").lower()
    time.sleep(.6)
    new_animal = Animal(name, kind, current_weight, healthy_weight, pronoun)
    animals.append(new_animal)
    print(f"\n{name} the {kind}'s freaky ass has been added to the farm!\n")
    time.sleep(1)

def intro_welcome():
    print("\n\nWelcome to the farm!\n\nHere you can observe and care for a variety of strange and beautiful creatures.")
    time.sleep(2)

def main_menu():
    intro_welcome()
    while True:
        print("\n")
        print("1. Animal Overview")
        print("2. Care for Animals")
        print("3. Add Animal")
        print("4. Quit")
        time.sleep(.5)
        choice = input("\nPlease choose an option: ")
        if choice == "1":
            time.sleep(1)
            if not animals:
                print("\nNo animals to display.")
            else:
                for animal in animals:
                    print(Fore.RED + f"\n{animal.name} the {animal.kind}" + Style.RESET_ALL)
                    print(f"-Current Weight = {animal.current_weight} pounds\n-Healthy Weight = {animal.healthy_weight} pounds")
                    time.sleep(0.7)
        elif choice == "2":
            time.sleep(1)
            feed_animals()
            medicate_animals()
        elif choice == "3":
            time.sleep(1)
            add_animal()
        elif choice == "4":
            time.sleep(0.5)
            print("\nBye bitch!")
            exit()
        else:
            print("Invalid choice. Try harder.")

animals = [
    Animal("Spott", "Five-legged Dog", 34, 38, "she", 98),
    Animal("Assie Stanklin", "Hairless Donkey", 48, 42, "she", 95),
    Animal("Angel", "Flightless Angel", 42, 42, "she", 100),
    Animal("Fatty", "Washington Mountain Troll", 862, 840, "he", 68),
    Animal("Boney", "Cursed Skeleton Grunt", 24, 68, "he", 21)
]

foods = [
    Food("KFC Double Down", 7, 5),
    Food("200 Fucking McGriddles", 17, 60),
    Food("Wet Kale Salad", -8, 15),
    Food("Flint Water Soup", -17, 1000)
]

meds = [
    Med("Great Value Tylenol", 4, 5),
    Med("Swedish Elixir",41, 15000)
]

main_menu()
