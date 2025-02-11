import os
import json
import time
from art import text2art
from colorama import Fore, Style

def load_data():
    if os.path.exists("freak_farm.json"):
        with open("freak_farm.json", "r") as file:
            return json.load(file)
    return {"animals": [], "foods": [], "meds": []}

# def save_data():
#     with open("freak_farm.json", "w") as file:
#         json.dump({
#             "animals": [vars(a) for a in animals],
#             "foods": [vars(f) for f in foods],
#             "meds": [vars(m) for m in meds]
#         }, file, indent=4)

print("\n")
title = text2art("freak.farm")
print(Fore.GREEN + title + Style.RESET_ALL)

class Animal:
    def __init__(self, name, kind, current_weight, healthy_weight, pronoun="it", health=100, clean=False):
        self.name = name
        self.kind = kind
        self.current_weight = current_weight
        self.healthy_weight = healthy_weight
        self.pronoun = pronoun
        self.health = health
        self.clean = clean

    def feed(self, food=None):
        print(f"\n{self.name} is currently {self.current_weight} pounds.")
        print("Commencing feeding...")
        time.sleep(1.5)
        initial_weight = self.current_weight
        while self.current_weight != self.healthy_weight:
            if self.current_weight > self.healthy_weight and food.healthy:
                self.current_weight = max(self.healthy_weight, self.current_weight - food.quant)
                print(f"Feeding {self.name} {food.type}...")
                time.sleep(1)
                print(f"Now {self.name} is {self.current_weight} pounds.\n")
                time.sleep(.5)
            else:
                self.current_weight = min(self.healthy_weight, self.current_weight + food.quant)
                print(f"Feeding {self.name} {food.type}...")
                time.sleep(1)
                print(f"Now {self.name} is {self.current_weight} pounds.\n")
                time.sleep(.5)
                print(f"After feeding {self.name} {food.type}, {self.pronoun} is now {self.current_weight} pounds!\n")
                time.sleep(2)
        print(f"OH SHIT!! Weight change for {self.name}: {initial_weight} -> {self.current_weight}\n")
#        save_data()
        time.sleep(.5)

    def medicate(self, med=None):
        print(f"\n{self.name} currently has {self.health} health.\n")
        print("Commencing care...")
        time.sleep(1.5)
        initial_health = self.health
        while self.health < 100:
            self.health = min(100, med.strength + self.health)
            print(f"Administering {self.name} {med.scrip}...")
            time.sleep(1)
            print(f"Now {self.name} has {self.health} health.\n")
            time.sleep(.5)
            print(f"After giving {self.name} {med.scrip}, {self.pronoun} now has {self.health} health!\n")
            time.sleep(2)
        print(f"OH FUCK!! Health change for {self.name}: {initial_health} -> {self.health}\n")
#        save_data()
        time.sleep(.5)

class Food:
    def __init__(self, type, quant, price, healthy):
        self.type = type
        self.quant = quant
        self.price = price
        self.healthy = healthy

class Med:
    def __init__(self, scrip, strength, cost):
        self.scrip = scrip
        self.strength = strength
        self.cost = cost

def find_best_food(animal):
    weight_diff = abs(animal.current_weight - animal.healthy_weight)
    if animal.current_weight > animal.healthy_weight:
        healthy_foods = [f for f in foods if f.healthy]
        return min(healthy_foods, key=lambda f: abs(f.quant - weight_diff))
    elif animal.current_weight < animal.healthy_weight:
        unhealthy_foods = [f for f in foods if not f.healthy]
        return min(unhealthy_foods, key=lambda f: abs(f.quant - weight_diff))
    return None

def find_best_med(animal):
    if animal.health < 100:
        health_diff = 100 - animal.health
        return min(meds, key=lambda m: abs(m.strength - health_diff))
    return None

def feed_animals():
    for animal in animals:
        food = find_best_food(animal)
        if food:
            animal.feed(food)
        else:
            print(f"\n{animal.name} is chillin, {animal.pronoun} fine.\n")
        time.sleep(2)

def medicate_animals():
    for animal in animals:
        med = find_best_med(animal)
        if med:
            animal.medicate(med)
        else:
            print(f"\n{animal.name} is chillin, {animal.pronoun} fine.\n")
        time.sleep(2)

def groom_animals():
    for animal in animals:
        if animal.clean:
            print(f"\n{animal.name} is chillin, {animal.pronoun} fine.\n")
        else:
            animal.clean = True
            print(f"{animal.name} is filthy! Commencing grooming...")
            time.sleep(2)
            print(f"\n{animal.name} has been groomed and is happy and clean!\n")
        time.sleep(2)

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
#    save_data()
    time.sleep(1)

def intro_welcome():
    print("\n\nWelcome to the farm!\n\nHere you can observe and care for a variety of strange and beautiful creatures.")
    time.sleep(2)

def animal_overview():
    time.sleep(.5)
    for animal in animals:
        print(Fore.RED + f"\n{animal.name} the {animal.kind}" + Style.RESET_ALL)
        weight_status = "(Overweight)" if animal.current_weight > animal.healthy_weight else \
                        "(Underweight)" if animal.current_weight < animal.healthy_weight else \
                        "(Healthy Weight)"
        cleanliness = "Clean & Fresh" if animal.clean else\
                      "Filthy & Gross"
        print(f"Current Weight: {animal.current_weight} pounds {weight_status}")
        print(f"Current Health: {animal.health} / 100")
        print(f"Cleanliness: {cleanliness}")
        time.sleep(1)

def main_menu():
    intro_welcome()
    while True:
        print("\n")
        print("1. Animal Overview")
        print("2. Feed Animals")
        print("3. Medicate Animals")
        print("4. Groom Animals")
        print("5. Add Animal")
        print("6. Quit")
        time.sleep(.5)
        choice = input("\nPlease choose an option: ")
        if choice == "1":
            time.sleep(1)
            animal_overview()
        elif choice == "2":
            time.sleep(1)
            feed_animals()
        elif choice == "3":
            time.sleep(1)
            medicate_animals()
        elif choice == "4":
            time.sleep(1)
            groom_animals()
        elif choice == "5":
            time.sleep(1)
            add_animal()
        elif choice == "6":
            time.sleep(0.5)
            print("\nBye bitch!")
            exit()
        else:
            print("Invalid choice. Try harder.")

data = load_data()
animals = [Animal(**a) for a in data ["animals"]]
foods = [Food(**f) for f in data ["foods"]]
meds = [Med(**m) for m in data ["meds"]]

main_menu()
