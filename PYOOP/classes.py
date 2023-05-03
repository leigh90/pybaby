
# Method 1
# class Employee:
#     # defining the properties and assigning values to them
#     ID = 3789
#     salary = 2500
#     department = "Human Resources"


class Employee:
    def __init__(self, ID, salary, department):  # __init__ is a method that is used to initialise the object being created using the parameters that are called when the object is first created. the double underscore is a python way of marking the method as a special python method. it males the class reusable otherwise you'd have to create a class like the way noted in method 1.
        self.id = ID
        self.salary = salary
        self.department = department

steve = Employee("AD3789", 2500,"Human Resources")
print(f" Steve is {steve.id}, {steve.salary}, {steve.department}")

# You can create a class with optional parameters by assigning default values to the  parameters during initialization
class Employee:
    def __init__(self, ID="interlakeen", salary=0, department=None):  # __init__ is a method that is used to initialise the object being created using the parameters that are called when the object is first created. the double underscore is a python way of marking the method as a special python method. it males the class reusable otherwise you'd have to create a class like the way noted in method 1.
        self.id = ID
        self.salary = salary
        self.department = department


steve = Employee("AD3789", 2500,"Human Resources")
mark = Employee() # mark object is created using the default values assigned in the class
print(f" Steve is {steve.id}, {steve.salary}, {steve.department}")
print(f" Mark is {mark.id}, {mark.salary}, {mark.department}")

# class variables are shared by all instances or objects of the classes. A change in the class variable will change the value of that property in all the objects of the class.
# instance variables are unique to each instance or object of the class. A change in the instance variable will change the value of the property in that specific object only.

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # instance variable

p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)

# There are three types of methods in Python:
# 1. instance methods
# 2. class methods
# 3. static methods

#The self argument only needs to be passed in the method definition and not when the method is called.
# Overloading refers to making a method perform different operations based on the nature of its arguments.
# Unlike in other programming languages, methods cannot be explicitly overloaded in Python but can be implicitly overloaded.
# In order to include optional arguments, we assign default values to those arguments rather than creating a duplicate method with the same name. If the user chooses not to assign a value to the optional parameter, a default value will automatically be assigned to the variable.


class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)
    
# tax() and salaryPerDay() - are instance methods.  - always take self as the first parameter to refer to the object.
Steve = Employee(3789, 2500, "Human Resources")  
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())

# Class methods
# they work with class variables and are accessible using the class name rather than its object 
# Since all class objects share the class variables, class methods are used to access and modify class variables.
# Class methods are accessed using the class name and can be accessed without creating a class object.
# To declare a method as a class method, we use the decorator @classmethod. 

class MyClass:
    classVariable = "educative"

    @classmethod
    def demo(cls):
        return cls.classVariable
    

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):    
        return cls.teamName   # cls is used to refer to the class just like self is used to refer to the object of the class. 

print(Player.getTeamName())   # Class methods are accessed using the class name and can be accessed without creating a class object.


# STATIC METHODS
# Limited to a class and not their objects
# They have no direct relation to class variables or instance variables.
# They are used as utility functions inside the class or when you dont want the inherited classes to modify a method definition.
# Static methods can be accessed using the class name or the object name.
# To declare a method as a static method, we use the decorator @staticmethod.
# It does not use a reference to the object or class, so we do not have to use self or cls.
# We can pass as many arguments as we want and use this method to perform any function without interfering with the instance or class variables.

class MyClass:

    @staticmethod
    def demo():
        print("I am a static method")


class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player('lol')
p1.demo()
Player.demo()


# Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. The purpose of a static method is to use its parameters and produce a useful result.

class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 60
height = 1.49
print(BodyInfo.bmi(weight, height))


# ACCESS MODIFIERS
# Public Attributes - can be accessed inside and outside the class. 
# All methods and properties in a class are publicly available by default. If you want to make it that a method cant be used publicly to have to declare that explicitly
# 
class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)

# the properties ID and method displayID() are public as they can be accessed in and out of the class.

# Private attributes - cannot be accessed directly from outside the class but can be accessed from inside the class.
# the goal is to keep it hidden from users and other classes. 
# a method or attribute is made private by using the double underscore prefix. 

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error

# trying to assess private attributes outside the class will yield an AttributeError like 
# Traceback (most recent call last):
#   File "classes.py", line 183, in <module>
#     print("Salary:", Steve.__salary)
# AttributeError: 'Employee' object has no attribute '__salary'


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary() # displaySalary() is a public method but it has access to a private attribute 
Steve.__displayID()  # this will generate an error because __displayID() is a private method and cannot be accessed outside the class.


# private attributes are essentialy to ensure that a method or attribute is not carelessly accessed. If you must access a private attribute use the _nameofclass notation for example

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

Steve = Employee(3769, 2500)
print(Steve._Employee__salary)
