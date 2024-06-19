# OOP Coffee Machine

This project simulates a coffee machine using Object-Oriented Programming (OOP) in Python.

## Project Description

The coffee machine project is an implementation of a basic coffee vending machine that allows users to select and purchase different types of coffee. The machine tracks resources such as water, milk, and coffee, and processes user payments.

## Features

- **Select Coffee:** Choose from three types of coffee: latte, espresso, and cappuccino.
- **Resource Management:** Tracks the amount of water, milk, and coffee available.
- **Payment Processing:** Accepts coins and checks if the payment is sufficient.
- **Reports:** Generates a report of the machine's current status, including resources and money collected.

## Classes and Methods

### Menu Class

- `get_items()`: Returns all available coffee types.
- `find_drink(order_name)`: Searches for a drink by name and returns a `MenuItem` object.

### MenuItem Class

- **Attributes**:
  - `name`: The name of the drink (e.g., "latte").
  - `cost`: The price of the drink.
  - `ingredients`: A dictionary of ingredients and amounts required to make the drink.

### CoffeeMaker Class

- `report()`: Prints a report of the current resources.
- `is_resource_sufficient(drink)`: Checks if there are enough resources to make the drink.
- `make_coffee(order)`: Deducts the required resources to make the drink.

### MoneyMachine Class

- `report()`: Prints the current amount of money collected.
- `make_payment(cost)`: Processes the payment and returns True if the payment is sufficient.

## Usage

Run the `main.py` script to start the coffee machine simulation. Follow the prompts to select a coffee, insert coins, and get your drink.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DRDLVS/OOP-CoffeeMachine.git
