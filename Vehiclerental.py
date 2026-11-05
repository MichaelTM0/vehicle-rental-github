#Vehcile Rental System
#a shop that rents out vehicles, people can see whats available , rent one, return one
#or see whats available
class Customer:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

class Vehicle:
    def __init__(self, make, model, year, color, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.daily_rate = daily_rate
        self.is_rented = False

    def rent(self):
        self.is_rented = True

    def return_vehicle(self):
        self.is_rented = False

    def calculate_cost(self, days):
        return self.daily_rate * days

    def display_info(self):
        status = "Rented" if self.is_rented else "Available"
        print(f"Make: {self.make} , Model: {self.model} , Year: {self.year} , Vehicle status: {status}")


class Car(Vehicle):
    def __init__(self, make, model, year, color, daily_rate, num_doors):
        super().__init__(make, model, year, color, daily_rate)
        self.num_doors = num_doors
        self.is_rented = False

    def display_info(self):
        super().display_info()
        print(f"This car has {self.num_doors} doors.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color, daily_rate):
        super().__init__(make, model, year, color, daily_rate)
        self.has_sidecar = False

    def includes_sidecar(self):
        self.has_sidecar = True


    def display_info(self):
        super().display_info()
        print("has a side car" if self.has_sidecar else "does not have a side car")


class Rentalshop:
    def __init__(self, name):
        self.name = name
        self.vehicles = []


    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)


    def show_available(self):
        for vehicle in self.vehicles:
            if vehicle.is_rented == False:
                vehicle.display_info()


    def show_rented(self):
        for vehicle in self.vehicles:
            if vehicle.is_rented == True:
                vehicle.display_info()





r1 = Rentalshop("Mikes exotic Imports")
c1 = Car("Lamborghini", "Diablo", 2000, "Black", 1500, 2)
r1.add_vehicle(c1)
c2 = Car("Ferrari", "812 Superfast", 2020, "Blue", 1700, 2)
r1.add_vehicle(c2)
c3 = Car("Porsche", "911 Turbo S", 2026, "Green", 1700, 2)
r1.add_vehicle(c3)
m1 = Motorcycle("BMW", "R 1300 GS Adventure", 2026, "Red", 1000)
r1.add_vehicle(m1)
m2 = Motorcycle("Honda", "Rebel 500", 2026, "Green Metalic", 1000)
r1.add_vehicle(m2)
m3 = Motorcycle("Yamaha", "YZF-R9", 2025, "Blue", 1000)
r1.add_vehicle(m3)



def main():
    print("\n" + "=" * 50)
    print("             Vehicle Rental Portal")
    print("=" * 50)


    while True:
        print("="*50)
        print("1. View Available Vehicles")
        print("2. Rent a vehicle")
        print("3. Return a Vehicle")
        print("4. View Rented Vehicles")
        print("5. Exit")

        choice = input("Please choose an option(1-5): ")

        if choice == "1":
            r1.show_available()
        elif choice == "2":
            for number, vehicle in enumerate(r1.vehicles, start=1):
                print(number, end=") ")
                vehicle.display_info()

            pick = int(input("Which number? "))
            vehicle = r1.vehicles[pick - 1]
            vehicle.rent()
            print("Enjoy your rental!")

        elif choice == "3":
            for number, vehicle in enumerate(r1.vehicles, start=1):
                print(number, end=") ")
                vehicle.display_info()

            pick = int(input("Which number? "))
            vehicle = r1.vehicles[pick -1]
            vehicle.return_vehicle()
            print(f"Thanks for renting from {r1.name} !")

        elif choice == "4":
            r1.show_rented()

        elif choice == "5":
            print("Thanks for renting from us! Goodbye!")
            break
        else:
            print("Please list pick a valid option(1-5)")


if __name__ == "__main__":
    main()




        
        




                





    
    
    
       