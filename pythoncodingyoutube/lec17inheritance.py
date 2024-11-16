class vehicle:
    def general_usage(self):
        print("general use: transportation")

class car(vehicle):
    def _init_(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific use: commute to work, vacation with family")

class motorcycle(vehicle):
    def __init__(self):
        print("I am motorcycle")
        self.wheels = 2
        self.has_roof = True

    def specific_usage(self):
        print("Specific use: road trip, racing")

c = car()
c.general_usage()
c.specific_usage()

# m = motorcycle()
# m.general_usage()
# m.specific_usage()


# isinstance and issubclass methods

print(isinstance(c,motorcycle))
print(isinstance(c,car))


print(issubclass(car,vehicle))
print(issubclass(car,motorcycle))


# Isinstance
# output for (c,motorcycle) is false since c is for car n motorcycle is not part of car.
# output for (c,car) is true since car is part of c.

# Issubclass
# issubclass(car,vehicle) is true since car is subclass of vehicle.
# output for (car,motorcycle) is false since car is not a subclass of motorcycle.

#Benefits of Inheritance
# Extensibility
# Readability
# We can reuse the code from parent class.

