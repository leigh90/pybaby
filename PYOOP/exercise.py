class Rectangle():
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return (self.__length + self.__width) * 2
    

siri = Rectangle(7,9)
print(siri.area())
print(siri.perimeter())





class Student:
    __name = None
    __rollnumber = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return(self.__name)
    
    def set_rollnumber(self, rollnumber):
        self.__rollnumber = rollnumber

    def get_rollnumber(self):
        return(self.__rollnumber)
    