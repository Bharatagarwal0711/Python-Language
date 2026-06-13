# Question 1
class Student:

    def __init__(self,Name:str,Age:int,Course:str):
        self.Name = Name
        self.Age = Age
        self.Course = Course

    def show(self):
        print(f"Name = {self.Name}")
        print(f"Age = {self.Age}")
        print(f"Course = {self.Course}")

S1 = Student("Bharat",21,"B.Tech")
S1.show()



# Question 2
class Car:

    def __init__(self,Brand:str,Model:str,Price:float):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price

    def show(self):
        print(f"Brand = {self.Brand}")
        print(f"Model = {self.Model}")
        print(f"Price = {self.Price}")
        print()

C1 = Car("BMW","M4",7000000)
C2 = Car("Audi","A8",7200000)
C1.show()
C2.show()



# Question 3
class Employee:

    def __init__(self,Employee_id:str,Name:str,Salary:float):
        self.Employee_id = Employee_id
        self.Name = Name
        self.Salary = Salary

    def show(self):
        print(f"Employee_id = {self.Employee_id}")
        print(f"Name = {self.Name}")
        print(f"Salary = {self.Salary}")

E1 = Employee("E21","Bhara1",100000)
E1.show()




# Question 4
class Rectangle:

    def __init__(self,length:float,width:float):
        self.length = length
        self.width = width

    def Area(self):
        print(f"Area = {self.length*self.width}")

R1 = Rectangle(10,20)
R1.Area()




# Question 5
import math

class Circle:

    def __init__(self,radius:float):
        self.radius = radius

    def Area(self):
        print(f"Area = {math.pi*self.radius**2}")

C1 = Circle(10)
C1.Area()



# Question 6
class BankAccount:
    
    def __init__(self,account_holder:str,balance:float):
        self.account_holder = account_holder
        self.balance = balance

    def Deposite(self,amount:float):
        self.balance += amount

        print(f"Updated Balancce After Deposite = {self.balance}")
        print()

    def Withdraw(self,amount:float):
        self.balance -= amount

        print(f"Updated Balance After Withdraw = {self.balance}")
        print()

A1 = BankAccount("XYZ",10000)
A1.Deposite(15000)
A1.Withdraw(10000)



# Question 7
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

D1 = Dog()
D1.sound()



# Question 8
class Person:

    def __init__(self,Name:str,Age:int):
        self.Name = Name
        self.Age = Age


class Student(Person):
    def __init__(self,Name:str,Age:int,roll_no:int):
        super().__init__(Name,Age)
        self.roll_no = roll_no

    def show(self):
        print(f"Name = {self.Name}")
        print(f"Age = {self.Age}")
        print(f"Roll no. = {self.roll_no}")

S1 = Student("Amit",21,10)
S1.show()



# Question 9
class Calculator:

    def add(self,num1:float,num2:float)->float:
        return num1 + num2
    
    def subtract(self,num1:float,num2:float)->float:
        return num1 - num2
    
    def multiply(self,num1:float,num2:float)->float:
        return num1 * num2
    
    def Divide(self,num1:float,num2:float)->float:
        return num1 / num2

C1 = Calculator()
num1 = float(input("Enter Number 1 = "))
num2 = float(input("Enter Number 2 = "))

print(f"Addition =  {C1.add(10,20)}")
print(f"Subtraction = {C1.subtract(10,20)}")
print(f"Multiplication = {C1.multiply(10,20)}")
print(f"Division = {C1.Divide(10,20)}")



# Question 10
class LibraryBook:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book_info(self):
        print("Book Name :", self.book_name)
        print("Author    :", self.author)
        print("Price     :", self.price)
        print()


B1 = LibraryBook("The Alchemist", "Paulo Coelho", 299)
B2 = LibraryBook("Atomic Habits", "James Clear", 499)
B3 = LibraryBook("Python Crash Course", "Eric Matthes", 650)

B1.display_book_info()
B2.display_book_info()
B3.display_book_info()
