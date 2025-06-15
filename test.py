class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

# Creating an object of Student
student1 = Student("Yannick", 19)

# Calling the method to display info
student1.display_info()
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

# Creating an object of Product
product1 = Product("Laptop", 800, 5)

# Calling the method to calculate total value
print(f"Product: {product1.name}")
print(f"Total Value in Stock: ${product1.total_value()}")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")
