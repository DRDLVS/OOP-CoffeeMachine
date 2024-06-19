from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os


# Function to clear the screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Converting classes to objects
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
menu = Menu()

# Gets the 3 types of coffee available: latte/espresso/cappuccino
choices = menu.get_items()

while True:
    # Holds the coffee the user chose
    user_choice = input(f"What would you like? {choices}: ").lower()

    if user_choice == "off":
        # Clear the screen and break the loop to turn off the machine
        clear_screen()
        break
    elif user_choice == "report":
        # Print the report of the coffee maker and money machine
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        # Find the corresponding MenuItem object and access its ingredients
        selected_item = menu.find_drink(user_choice)

        if selected_item:
            # Check if resources are sufficient
            if my_coffee_maker.is_resource_sufficient(selected_item):
                # Process the payment
                if my_money_machine.make_payment(selected_item.cost):
                    # Make the coffee
                    my_coffee_maker.make_coffee(selected_item)
            else:
                print("Sorry, not enough resources.")
        else:
            print("Invalid choice. Please select a valid option.")
