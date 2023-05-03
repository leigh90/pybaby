# One can observe that classes contain properties and that objects are created to manipulate and access these properties. 
# To make this object-oriented system more reliable and error free, it is a good practice to limit access to the class members at times.
# Information hiding refers to the concept of hiding the inner workings of a class and simply providing an interface through which the outside world can interact with the class without knowing what’s going on inside.
# The purpose is to implement classes in such a way that the instances (objects) of these classes should not be able to cause any unauthorized access or change in the original contents of a class. 
# One class does not need to know anything about the underlying algorithms of another class. However, the two can still communicate.


# Data hiding can be divided into two primary components:

# Encapsulation
# Abstraction
# Encapsulation in OOP refers to binding data and the methods to manipulate that data together in a single unit, that is, class.
# ncapsulation is usually done to hide the state and representation of an object from outside. 
# A good way is to make all variables in a class private to restrict access by the rest of the code to that class
# Once you do this you need to create public methods that can communictae with that class. These methods are called getters and setters. 

# ADVANTAGES OF ENCAPSULATION

# Classes make the code easy to change and maintain.
# Properties to be hidden can be specified easily.
# We decide which outside classes or functions can access the class properties.

# GETTERS AND SETTERS
# A getter method allows you to read a property's value
# A setter method allows you to modify a property's value



class User:
    def __init__(self, username=None):
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return(self.__username)
    


Jonathan = User("Jonathan")
print("Before setting:", Jonathan.getUsername())
Jonathan.setUsername("rideordie")
print("After setting", Jonathan.getUsername())

# anyone can access, change, or print the password and userName fields directly from the main code.
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
                and (self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")

# A better implementation
Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"   # because the password property is publc the password can be easily changed
Steve.login("steve", "6789")

class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower())
                and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.__userName.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")


# created a new User object and stored the password and username
Steve = User("Steve", "12345")
Steve.login("steve", "12345")  # Grants access because credentials are valid

# does not grant access since the credentails are invalid
Steve.login("steve", "6789")
Steve.__password  # compilation error will occur due to this line


