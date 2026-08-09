# find 2nd largest number

def findsecondlargestarray(arr):
    """

    :return:
    """
    n = len(arr)
    arr.sort()
    for i in range(n-2, -1, -1):
        if arr[i] != arr[n - 1]:
            return arr[i]
    return -1


arr = [10,10,10]
# print(findsecondlargestarray(arr))


############ find 3rd largest number
def findthirdlargestarray(arr):
    """

    :param arr:
    :return:
    """
    n = len(arr)
    arr.sort()
    if n >= 3:
        for ii in range(n - 3, -1, -1):
            if arr[ii] != arr[n - 1] and arr[ii] != arr[n - 2]:
                return arr[ii]
    elif n < 3:
        return -1
    else:
        return arr[n]

arr = [2,2,2]
# print(findthirdlargestarray(arr))

####### array reverse
def  arrayrev(arr):
    n = len(arr)

    temp = [0]*n
    for i in range(n):
        temp[i] = arr[n-i-1]

    for i in range(n):
        arr[i] = temp[i]

arr = [1,3,4,5,7,8]
# print(arrayrev(arr))

def square():
    for x in range(1,6):
        print("Square of", x,"is", x*x)

# square()

def loop():
    count = 1
    while count <= 5:
        print("Count is", count)
        count += 1
# loop()


def loop_controls():
    for i in range(0, 10):
        if i == 3:
            continue
        print(i)

# loop_controls()


def abcd(item):
    for ii in item:
        print(ii)

item = ["apple","orange","banana"]
# abcd(item)

# simulate an error
def error():
    num = int(input("Enter a number:"))
    print("You entered", num)

# error()

def error():
    try:
        num = int(input("Enter a number: "))
        print("You entered", num)

    except ValueError:
        print("Oops! That's not a valid number")

# error()
# Steps:
# 1. Define a basic class
# 2. Create a class instances
# 3. Add method to a class
# 4. Use class attributes
# 5. Demonstrate Inheritance

## class
# 1. Define a basic class
class Dog:
    pass

# 2. Create a class instances
my_dog = Dog()
# print(type(my_dog))

# 3. Add method to a class: Methods are functions inside a class
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
# my_dog.bark()

# 4. Use class attributes
# add attibutes to a dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!!")

abcd = Dog("Bunty", 5)
# abcd.bark()


# 5. Demonstrate Inheritance
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!!!")

# create a subclass that demonstrates a dog
class Puppy(Dog):
    def play(self):
        print(self.name, "is playful")
        print(self.age, "is his/her age")

xyz = Puppy("Sam", 4)
# xyz.play()
# xyz.bark()

"""
Mini project: Simple console calculator (beginner friendly)
Features:
- Class based calculator
- basic operations
- loop for repeated use
- history stored in a list
- save and load history stored in a text file
- simple error handling
"""

# filename
HISTORY_FILE = "calc_history.txt"

class Calculator:
    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        data = []
        try:
            with open(HISTORY_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data.append(line)
        except FileNotFoundError:
            pass
        return data

    def save_history(self):
        with open(HISTORY_FILE, "w") as f:
            for item in self.history:
                f.write(item + "\n")

    def get_number(self, message):
        while True:
            value = input(message)
            try:
                return float(value)
            except ValueError:
                print("Enter a valid number.")

    def add(self, a, b):
        return a + b
    def substract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero!")

    def calculate(self, choice):
        a = self.get_number("Enter 1st number: ")
        b = self.get_number("Enter 2nd number: ")

        if choice == "1":
            result = self.add(a, b)
            op = "+"

        if choice == "2":
            result = self.substract(a, b)
            op = "-"

        if choice == "3":
            result = self.multiply(a, b)
            op = "*"

        if choice == "/":
            result = self.divide(a, b)
            op = "/"

        else:
            return

        if result is not none:
            record = f"{a} {op} {b} = {result}"
            print("Result: ", result)
            self.history.append(record)

    def show_history(self):
        if not self.history:
            print("No calculations yet!")
            return
        print("\nPrevious Calculations:")
        for item in self.history:
            print(item)

def main():
    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4"]:
            calc.calculate(choice)
        elif choice == "5":
            calc.show_history()
        elif choice == "6":
            calc.save_history()
            print("Goodbye. History saved.")
            break
        else:
            print("Invalid choice. Try again")

main()