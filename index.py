# 1. Using self in Constructor

class Student:
    def __init__(self, student_name, student_marks):
        self.name = student_name
        self.marks = student_marks

    def display(self):
        print(f"Student Name: {self.name} | Marks: {self.marks}")

# Testing Student class
std1 = Student("Taha", 99)
std1.display()


# 2. Using cls with Class Variables

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

class Car:
    def __init__(self, brand_name):
        self.brand = brand_name

    def start(self):
        print(f"{self.brand} engine has been started!")

# Accessing public method and variable
car_obj = Car("Toyota")
car_obj.start()


# 4. Class Variables and Class Method

class Bank:
    bank_name = "HBL Bank"

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

Bank.set_bank_name("Al Baraka Bank")
acc1.show_bank()
acc2.show_bank()


# 5. Static Method Example

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Using the utility method
print("Sum is:", MathUtils.add(7, 12))


# 6. Constructor and Destructor Demo

class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger instance has been deleted.")

# Instantiate and delete
log = Logger()
del log


# 7. Access Modifiers

class Employee:
    def __init__(self, emp_name, salary, ssn):
        self.name = emp_name
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")

# Using the class
emp = Employee("Taha Saif", 50000, "123-45-6789")
emp.show_details()
print(emp.name)         # Public
print(emp._salary)      # Accessible but discouraged
# print(emp.__ssn)      # Will raise AttributeError


# 8. Using super()

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
t1 = Teacher("Taha Saif", "Maths")
t1.introduce()


# 9. Abstract Base Class

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

class Dog:
    def __init__(self, dog_name, breed):
        self.name = dog_name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof!")

my_dog = Dog("Buddy", "Labrador")
my_dog.bark()


# 11. Class Method Example

class Book:
    total_books = 0

    @classmethod
    def add_book(cls):
        cls.total_books += 1
        print(f"Books registered: {cls.total_books}")

Book.add_book()
Book.add_book()


# 12. Static Method Example

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print("Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(30))


# 13. Composition

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

hr = Department("HR")
e1 = Employee("Taha")
e2 = Employee("Ali")
hr.add_staff(e1)
hr.add_staff(e2)
hr.show_staff()


# 15. MRO and Diamond Problem

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

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Logging: function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    print(f"Hello {name}!")

greet("Taha")


# 17. Class Decorator

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

p = Person("Taha")
print(p.greet())
print(p.show_name())


# 18. Property Decorator

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

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return num * self.factor

m = Multiplier(4)
print("Is callable:", callable(m))
print("Result:", m(6))


# 20. Custom Exception

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
