
#1. Using self Assignment

# Assignment:
# Create a class Student with attributes name and marks.
# Use the self keyword to initialize these values via a constructor.
# Add a method display() that prints student details.


class Student:
    def __init__(self, student_name, student_marks):
        self.name = student_name
        self.marks = student_marks

    def display(self):
        print(f"Student Name: {self.name} | Marks: {self.marks}")

# Testing Student class
std1 = Student("Fayaz ALI", 33)
std1.display()


# 2. Using cls with Class Variables


# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.



class Counter:
    total_instances = 0

    def __init__(self):
        Counter.total_instances += 1

    @classmethod
    def show_total(cls):
        print(f"Total objects created so far: {cls.total_instances}")

# Creating instances
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
Counter.show_total()


# 3. Public Members Access

# Assignment:
# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class


class Car:
    def __init__(self, brand_name):
        self.brand = brand_name

    def start(self):
        print(f"{self.brand} engine has been started!")

# Accessing public method and variable
car_obj = Car("HAVAL")
car_obj.start()


# 4. Class Variables and Class Method

# Assignment:
# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that
# allows changing the bank name. Show that it affects
# all instances of the class.


class Bank:
    bank_name = "MEEZAN"

    @classmethod
    def set_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Updated Bank Name: {cls.bank_name}")

    def show_bank(self):
        print(f"Bank Associated: {self.bank_name}")

# Creating objects
acc1 = Bank()
acc2 = Bank()
acc1.show_bank()
acc2.show_bank()

Bank.set_bank_name("Al Falah ")
acc1.show_bank()
acc2.show_bank()


# 5. Static Method Example

# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Using the utility method
print("Sum is:", MathUtils.add(7, 12))


# 6. Constructor and Destructor Demo

# Assignment:
# Create a class Logger that prints a message when an object is created (constructor)
# and another message when it is destroyed (destructor).


class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger instance has been deleted.")

# Instantiate and delete
log = Logger()
del log


# 7. Access Modifiers


# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.



class Employee:
    def __init__(self, emp_name, salary, ssn):
        self.name = emp_name
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")

# Using the class
emp = Employee("Fayaz ALI", 3330, "746289")
emp.show_details()
print(emp.name)         # Public
print(emp._salary)      # Accessible but discouraged
# print(emp.__ssn)      # Will raise AttributeError


# 8. Using super()

# Assignment:
# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, and use
# super() to call the base class constructor.


class Person:
    def __init__(self, pname):
        self.name = pname

class Teacher(Person):
    def __init__(self, pname, subject):
        super().__init__(pname)
        self.subject = subject

    def introduce(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

# Testing inheritance
t1 = Teacher("Abrar ALI", "CS")
t1.introduce()


# 9. Abstract Base Class

# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

# Testing abstract inheritance
rect = Rectangle(6, 4)
print("Area of rectangle:", rect.area())


# 10. Instance Methods

# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method
# bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, dog_name, breed):
        self.name = dog_name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof!")

my_dog = Dog("Buddy", "Labrador")
my_dog.bark()


# 11. Class Method Example

# Assignment:
# Create a class Book with a class variable total_books. Add a class method 
# increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0

    @classmethod
    def add_book(cls):
        cls.total_books += 1
        print(f"Books registered: {cls.total_books}")

Book.add_book()
Book.add_book()


# 12. Static Method Example

# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c)
# that returns the Fahrenheit value.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print("Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(30))


# 13. Composition

# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object
# to the Car class during initialization. Access a method of the Engine class via the
# Car class.


class Engine:
    def start(self):
        print("Engine is now running.")

class Car:
    def __init__(self, engine_obj):
        self.engine = engine_obj

    def run(self):
        self.engine.start()
        print("Car is ready to go!")

eng = Engine()
vehicle = Car(eng)
vehicle.run()


# 14. Aggregation

# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a 
# Department object store a reference to an Employee object that exists independently
# of it.


class Department:
    def __init__(self, dept_name):
        self.name = dept_name
        self.staff = []

    def add_staff(self, emp):
        self.staff.append(emp)

    def show_staff(self):
        print(f"Department: {self.name}")
        for e in self.staff:
            print("-", e.name)

class Employee:
    def __init__(self, emp_name):
        self.name = emp_name

hr = Department("Manager")
e1 = Employee("Fayaz")
e2 = Employee("Nabeel ALI")
hr.add_staff(e1)
hr.add_staff(e2)
hr.show_staff()


# 15. MRO and Diamond Problem

# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        print("In A")

class B(A):
    def show(self):
        print("In B")

class C(A):
    def show(self):
        print("In C")

class D(B, C):
    pass

d = D()
d.show()
print("MRO:", D.__mro__)


# 16. Function Decorator


# Assignment:
# Write a decorator function log_function_call that prints "Function is being called"
# before a function executes. Apply it to a function say_hello().


def log_call(func):
    def wrapper(*args, **kwargs):
        print("Logging: function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    print(f"Hello {name}!")

greet("Nabeel ALI")


# 17. Class Decorator

# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet()
# method returning "Hello from Decorator!". Apply it to a class Person.


def add_greeting(cls):
    def greet(self):
        return "Hello from decorated class!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return f"My name is {self.name}"

p = Person("Nabeel")
print(p.greet())
print(p.show_name())


# 18. Property Decorator

# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the 
# price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, cost):
        self._price = cost

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = val

    @price.deleter
    def price(self):
        del self._price
        print("Price has been deleted")

item = Product(200)
print(item.price)
item.price = 350
print(item.price)
del item.price


# 19. __call__ and callable()

# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__()
# method that multiplies an input by the factor. Test it with callable() and by 
# calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return num * self.factor

m = Multiplier(4)
print("Is callable:", callable(m))
print("Result:", m(6))


# 20. Custom Exception

# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that
# raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 18:
        raise InvalidAgeError("You must be at least 18.")
    print("Age accepted.")

try:
    validate_age(16)
except InvalidAgeError as err:
    print("Error:", err)


# 21. Making a Class Iterable

# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and 
# __next__() to make the object iterable in a for-loop, counting down to 0.


class Countdown:
    def __init__(self, start_num):
        self.num = start_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current

cd = Countdown(5)
for i in cd:
    print(i)
