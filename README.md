
# OOP Assignment

## Assignment 1: Design Your Own Class! 🏗️

1. Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
2. Add attributes and methods to bring the class to life!
3. Use constructors to initialize each object with unique values.
4. Add an inheritance layer to explore polymorphism or encapsulation.

### Example:
```python
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, strap_material):
        super().__init__(brand, model, battery_life)
        self.strap_material = strap_material

    def show_time(self):
        print("Showing time on the smartwatch.")
```

## Activity 2: Polymorphism Challenge! 🎭

1. Create a program that includes animals or vehicles with the same action (like `move()`).
2. Make each class define `move()` differently (for example, `Car.move()` prints "Driving" 🚗, while `Plane.move()` prints "Flying" ✈️).

### Example:
```python
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

def demonstrate_movement(vehicle):
    vehicle.move()

car = Car()
plane = Plane()

demonstrate_movement(car)
demonstrate_movement(plane)
```

## Additional Information

Feel free to expand on these examples and add more features to your classes. Experiment with different attributes, methods, and inheritance structures to fully understand the concepts of Object-Oriented Programming.
