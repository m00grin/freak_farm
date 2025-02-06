import time
from art import text2art
from colorama import Fore, Style

print("\n")
title = text2art("freak.farm")
print(Fore.GREEN + title + Style.RESET_ALL)

class Animal:
    def __init__(self, name, kind, current_weight, healthy_weight, pronoun="it"):
        self.name = name
        self.kind = kind
        self.current_weight = current_weight
        self.healthy_weight = healthy_weight
        self.pronoun = pronoun
    
    def feed(self, food=None, med=None):
        print(f"\n{self.name} is currently {self.current_weight} pounds. Commencing care...\n")
        time.sleep(1.5)
        initial_weight = self.current_weight
        if self.current_weight > self.healthy_weight:
            if med:
                while self.current_weight > self.healthy_weight and med:
                    self.current_weight -= med.strength
                    print(f"Administering {self.name} {med.scrip}...")
                    time.sleep(1)
                    print(f"Now {self.name} is {self.current_weight} pounds.\n")
                    time.sleep(.5)
                print(f"After giving {self.name} {med.scrip}, {self.pronoun} is now {self.current_weight} pounds!\n")
                time.sleep(2)
        elif self.current_weight < self.healthy_weight:
            if food:
                while self.current_weight < self.healthy_weight and food:
                    self.current_weight += food.quant
                    print(f"Feeding {self.name} {food.type}...")
                    time.sleep(1)
                    print(f"Now {self.name} is {self.current_weight} pounds.\n")
                    time.sleep(.5)
                print(f"After feeding {self.name} {food.type}, {self.pronoun} is now {self.current_weight} pounds!\n")
                time.sleep(2)
        else:
            print(f"{self.name} is all good, and {self.pronoun} does not need food or medicine.\n")
            time.sleep(1)
        print(f"OH SHIT!! Weight change for {self.name}: {initial_weight} -> {self.current_weight}\n")
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

def find_best_care(animal):
    weight_diff = animal.current_weight - animal.healthy_weight
    if weight_diff > 0.5 * animal.healthy_weight:
        best_med = max(meds, key=lambda m: m.strength)
        return None, best_med
    elif weight_diff < -0.5 * animal.healthy_weight:
        best_food = max(foods, key=lambda f: f.quant)
        return best_food, None
    elif animal.current_weight > animal.healthy_weight:
        best_med = min(meds, key=lambda m: m.cost)
        return None, best_med
    elif animal.current_weight < animal.healthy_weight:
        best_food = min(foods, key=lambda f: f.price)
        return best_food, None
    return None, None

def feed_animals():
    for animal in animals:
        food, med = find_best_care(animal)
        if food or med:
            animal.feed(food, med)
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

def main_menu():
    while True:
        print("\n\nWelcome to the farm!\n\nHere you can observe and care for a variety of strange and beautiful creatures.\n")
        time.sleep(2)
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
                    print(f"\n{animal.name} the {animal.kind}: Current Weight = {animal.current_weight} pounds, Healthy Weight = {animal.healthy_weight} pounds.")
                    time.sleep(0.5)
        elif choice == "2":
            time.sleep(1)
            feed_animals()
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
    Animal("Spott", "Five-legged Dog", 34, 38, "she"),
    Animal("Assie Stanklin", "Hairless Donkey", 48, 42, "she"),
    Animal("Angel", "Flightless Angel", 42, 42, "she"),
    Animal("Fatty", "Washington Mountain Troll", 862, 840, "he"),
    Animal("Boney", "Cursed Skeleton Grunt", 24, 68, "he")
]

foods = [
    Food("Plain Borgar", 2, 5),
    Food("Triple Bacon Duck Fat Borgar", 8, 15),
]

meds = [
    Med("Mostly-safe Diet Pills", 2, 5),
    Med("FDA-banned Diet Pills from 1998", 8, 15),
]

main_menu()
