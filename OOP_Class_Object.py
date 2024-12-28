class Car:
    def __init__(self, color, model, condition):
        self.color = color
        self.model = model
        self.condition = condition


car1 = Car("Red", "BMW", "New")
car2 = Car("White", "Land Cruiser", "Old")

print(car1.color)
print(car1.condition)
print(car2.model)