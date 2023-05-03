# # The ability of an object to take different forms e.g a shape can be a circle, squeare, rectangle, triangle
# # 

# # Implementation


class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def get_area(self):
        return (self.width * self.height)
    

class Circle():
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def get_area(self):
        return (self.radius * self.radius * 3.142)
    

shapes = [Rectangle(6,10), Circle(7)]
print("rectangle ", (shapes[0].sides))
print("rectangle ", (shapes[1].sides))

print("circle area", shapes[0].get_area())
print("rectangle area", shapes[1].get_area())


class Shape:
    def __init__(self) -> None:
        self.sides = 0

    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self,width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.sides = 4

    def get_area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        self.sides = 0

    def get_area(self):
        return self.radius * self.radius * 3.142
    


# #   overloading operators in python
class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):  # overloading the `+` operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp
    
    def __sub__(self, other):  # overloading the `-` operator
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp
    
obj1 = Com(3 + 7)
obj2 = Com(2,5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)


# # DUCK TYPING to achieve polymorphism without inheritance

class Dog:
    def Speak(self):
        print("Woof woof")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    def Sound(self, animal):
        animal.Speak()


sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)



# # Abstract Base classes -define a set of methods and properties that a class must implement in order to be considered a duck-type instance of that class.
class Shape:  # Shape is a child class of ABC
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)
    
    def perimeter(self):
        return (4 * self.length)
    


shape = Shape()
# square = Square(4)


# #To define an abstract base class, we use the abc module. The abstract base class is inherited from the built-in ABC class. We have to use the decorator @abstractmethod above the method that we want to declare as an abstract method.
# from abc import ABC, abstractmethod

class ParentClass(ABC):
    @abstractmethod
    def method(self):
        pass


# for example
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length


# shape = Shape() # leads to this error->TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# this code will not compile since Shape has abstract methods without
# method definitions in it


class Parent:
    def prn(self):
        print("Parent")


class Child(Parent):
    def __init__(self):
        self.a = Parent()

    def prn(self):
        print("Child")


temp = Child()
temp.a.prn()