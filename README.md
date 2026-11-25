# Vehicle Rental System

A command-line vehicle rental application built in Python using object-oriented programming. A rental shop holds an inventory of cars and motorcycles that customers can browse, rent, and return, with the shop tracking which vehicles are available and which are out.

This project was built to practice OOP fundamentals: **inheritance**, **composition**, and **polymorphism**.

## Features

* **Browse inventory** — view all available vehicles, or all currently rented ones
* **Rent a vehicle** — pick a vehicle from a numbered list and mark it as rented
* **Return a vehicle** — return a rented vehicle so it becomes available again
* **Two vehicle types** — Cars (with a number of doors) and Motorcycles (with an optional sidecar), each displaying its own details
* **Rental cost calculation** — cost based on a daily rate and number of days
* **Menu-driven interface** that loops until the user exits

## Requirements

* Python 3.6 or newer
* No external packages — uses only the Python standard library

## Getting Started

1. Clone the repository (update the URL with your own if the repo name differs):

   ```bash
   git clone https://github.com/MichaelTM0/vehicle-rental-system.git
   cd vehicle-rental-system
   ```

2. Run the program:

   ```bash
   python Vehiclerental.py
   ```

3. Choose an option from the menu to browse, rent, or return vehicles.

## Usage

```
==================================================
             Vehicle Rental Portal
==================================================
1. View Available Vehicles
2. Rent a vehicle
3. Return a Vehicle
4. View Rented Vehicles
5. Exit
Please choose an option (1-5):
```

## How It Works

The program is organized around four classes:

* **`Vehicle`** — the parent class holding everything shared by all vehicles: make, model, year, color, daily rate, and rental status, plus the core methods (`rent`, `return_vehicle`, `calculate_cost`, `display_info`).
* **`Car(Vehicle)`** and **`Motorcycle(Vehicle)`** — child classes that inherit all of `Vehicle`'s behavior and add their own details (doors for cars, a sidecar for motorcycles). Each overrides `display_info()` to show its own extra information.
* **`RentalShop`** — manages the whole inventory. It holds a list of vehicle objects and provides methods to add vehicles and show which are available or rented.
* **`Customer`** — represents a renter.

This demonstrates the three core OOP concepts:

* **Inheritance (IS-A):** a `Car` *is a* `Vehicle`, so it inherits renting and returning rather than redefining them.
* **Composition (HAS-A):** a `RentalShop` *has* vehicles — it stores a list of `Vehicle` objects rather than inheriting from them.
* **Polymorphism:** calling `display_info()` works the same way on any vehicle, but each type prints its own details — a car shows its doors, a motorcycle shows its sidecar.

Vehicles are added to the shop at startup. The menu loop shows the inventory as a numbered list, and the user picks a vehicle by number to rent or return it.

## What I Learned

* Modeling a real-world system with a parent class and specialized child classes
* Method overriding and polymorphism — the same method call behaving differently per type
* Composition — a shop that manages a list of objects it does not inherit from
* Using `enumerate()` to present a numbered menu and indexing a list to select an item
* Converting user input (strings) to the right type and translating a 1-based choice to a 0-based index
* Building a menu loop around a collection of objects

## Author

**Michael Murchie**

* GitHub: [MichaelTM0](https://github.com/MichaelTM0)
* LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
