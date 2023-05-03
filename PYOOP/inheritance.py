# Inheritance provides a way to create a new class from an existing class. The new class inherits all the non-private properties and methods of the existing class. 
# Parent Class (Super Class or Base Class): This class allows the reuse of its public properties in another class.
# Child Class (Sub Class or Derived Class): This class inherits or extends the superclass. A child class has all public attributes of the parent class.

class ParentClass:
    # attributes of the parent class
    pass

# the child class inherits the parent class by passing in the parent class in its definition
class ChildClass(ParentClass):
    # attributes of the child class
    pass


class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)

obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()


# The super function super()
class Vehicle:  # defining the parent class
    fuelCap = 90

# Say you have a property whose value is  defined in the parent class and want the child class to inherit the property but have a different value you use the super() function to define it. so when you call super() you use the property in the parent class.
class Car(Vehicle):  # defining the child class
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()


class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining display method in the child class
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()

# The super() method is also used to call the initializer of the parent class from inside the child class.
# Her's the interesting thing you dont initialise the child class  with it own property definitions you basically call super pass in the values for the parameters required to create the parent class and bob's your uncle

class ParentClass():
    def __init__(self, heather, bella):
        self.a = heather
        self.b = bella


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

obj = ChildClass(1, "troy", 3)
print(obj.a)
print(obj.b)
print(obj.c)        


class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Door: ", self.doors)

obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()

# TYPES OF INHERITANCE
# Single Inheritance 
# In single inheritance you only have a single class extending from another class. 
class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class
    def openTrunk(self):
        print("Trunk is now open.")


corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class
corolla.openTrunk()  # accessing method from its own class


# Multi-level Inheritance
# When a class is derived from a class which is itself derived from another class
class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class of Vehicle
    def openTrunk(self):
        print("Trunk is now open.")


class Hybrid(Car):  # child class of Car
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")


priusPrime = Hybrid()  # creating an object of the Hybrid class
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the child class


# Hierarchical inheritance
# More than one class extends from the same base/parent/super class.

class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class of Vehicle
    pass


class Truck(Vehicle):  # child class of Vehicle
    pass


corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class

volvo = Truck()  # creating an object of the Truck class
volvo.setTopSpeed(180)  # accessing methods from the parent class


# MULTIPLE INHERITANCE
# When a class is derived from more than one base class.
class CombustionEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

class NinjaEngine():
    def set_dope_level(self, dopelevel):
        self.Dopelevel = dopelevel

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine, NinjaEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)
        print("Dopeness Level:", self.Dopelevel)



car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.set_dope_level("100000000")
car.printDetails()


# HYBRID INHERITANCE
# A sweet mix of multiple and multi-level inheritance

class Engine:  # Parent class
    def setPower(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine


class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()


# Advantages of inheritance
# 1. Reusability
# 2. Maintainace
# 3. Extensibility - you can extend the features of say a product without changing its core attributes. 
# 4. Data hiding - you can keep some data private so that the derived class cant alter it. 


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdrawal(self, amount):
        self.balance = self.balance - amount


        
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,interest_rate=1):
        super().__init__(title, balance)
        self.interestRate = interest_rate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100




        
cstmr1 = SavingsAccount("Mark", 5000, 4)
