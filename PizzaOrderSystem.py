import csv
from datetime import datetime


# Menu

def print_menu():
    with open('Menu.txt', 'r', encoding="utf-8") as f:
        menu = f.read()
        print(menu)


# Super class

class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza!"
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Create a list of pizza bases and sauces

class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Classic Pizza"
        self.cost = 75


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 90


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.cost = 80


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Plain Pizza"
        self.cost = 95


# super class
class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description


class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "with Olives"
        self.cost = 5


class Mushrooms(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "with Mushrooms"
        self.cost = 7


# subclass
class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "with Goat Cheese"
        self.cost = 10


class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "with Meat"
        self.cost = 12


class Onions(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "with Onions"
        self.cost = 4


class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "with Corn"
        self.cost = 10


def place_order(pizza_choice, sauce_choice, name, card_number, card_password, card_cvv, description):
    # pizza choice

    if pizza_choice == "1":
        pizza = ClassicPizza()

    elif pizza_choice == "2":
        pizza = MargheritaPizza()

    elif pizza_choice == "3":
        pizza = TurkPizza()

    elif pizza_choice == "4":
        pizza = PlainPizza()

    else:
        print("Invalid choice. Please choose a valid pizza number")
        print_menu()
        return

    # Sauce Choice

    if sauce_choice == "11":
        sauce = Olives(pizza=pizza)
    elif sauce_choice == "12":
        sauce = Mushrooms(pizza=pizza)
    elif sauce_choice == "13":
        sauce = GoatCheese(pizza=pizza)
    elif sauce_choice == "14":
        sauce = Meat(pizza=pizza)
    elif sauce_choice == "15":
        sauce = Onions(pizza=pizza)
    elif sauce_choice == "16":
        sauce = Corn(pizza=pizza)
    else:
        print("Invalid choice. Please choose a valid sauce number.")

        print_menu()
        return

    # Order cost:

    total_cost = int(pizza.cost) + int(sauce.cost)
    print(f"Total Cost: {total_cost}")

    # Order time:

    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save Order information:

    with open("order_database.csv", mode="w", newline="") as f:
        db = csv.writer(f)
        db.writerow(
            [name, card_cvv, card_number, card_password, description, pizza.get_description(), sauce.get_description(),
             total_cost, order_time])

    print("Your order has been received, Thank You!")


print_menu()

# get information for pizza and sauce:

pizza_choice = input("Please choose a pizza base (1-4):  ")

sauce_choice = input("Please choose a pizza sauce  (11-16):  ")

# get information from user:

name = input("Name:")
card_number = input("Card number:")
card_password = input("Password:")
card_cvv = input("CVV:")
description = input("Order description: ")

place_order(pizza_choice, sauce_choice, name, card_number, card_password, card_cvv, description)