# =========================================================
# Assignment 1: Design Your Own Class
# =========================================================

# Base class (parent)
class Vehicle:
    def __init__(self, make, model):
        """Initializes the Vehicle object with make and model."""
        self.make = make
        self.model = model

    def move(self):
        """A generic move method."""
        print("This vehicle is moving.")

    def display_info(self):
        """A method to display vehicle information."""
        print(f"Vehicle: {self.make} {self.model}")

# Child class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year):
        """Initializes the Car object, including the parent's attributes."""
        super().__init__(make, model)
        self.year = year

    # Part of Activity 2: Polymorphism Challenge
    def move(self):
        """Specific move method for a Car."""
        print("The car is driving.")

# Another child class that inherits from Vehicle
class Plane(Vehicle):
    def __init__(self, make, model, passengers):
        """Initializes the Plane object, including the parent's attributes."""
        super().__init__(make, model)
        self.passengers = passengers

    # Part of Activity 2: Polymorphism Challenge
    def move(self):
        """Specific move method for a Plane."""
        print("The plane is flying.")

# =========================================================
# Activity 2: Polymorphism Challenge
# =========================================================

# Create objects from the classes
my_car = Car("Toyota", "Camry", 2022)
my_plane = Plane("Boeing", "747", 400)

# Demonstrate polymorphism by calling the same method on different objects
print("Demonstrating polymorphism:")
my_car.move()
my_plane.move()

# Demonstrate a method from the parent class
print("\nDemonstrating parent class method:")
my_car.display_info()
my_plane.display_info()