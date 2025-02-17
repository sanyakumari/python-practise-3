# x = float(input("write the value for x:")) 
# y = float(input("write the value for y:"))

# z = round(x/y,2)
# print(f"the operation of the two number is :{z:.2f}")


# def hello(to):
#     print("hello,",to)

# name = input("What is your name:")
# hello(name)

# def main():
#     name = input("What is your name:")
#     hello()

# def hello():
#     print("hello", name)

# main() # it will show a error a name is not defined in the scope of def hello() function 





# def main():
#     x = int(input("What is x?:"))
#     print("x square is", square(x))

# def square(n):
#     return n*n

# main()



# x = int(input("Enter the number x:"))
# y = int(input("Enter the number y:"))

# if x>y:
#     print("x is greater than y")
# elif x<y:
#     print("y is greater than x")
# else:
#     print("x is equal to y")  


# def main():
#     x = int(input("Enter the number x:"))
#     if is_even(x):
#         print("x is even")
#     else:
#         print("x is odd")

# def is_even(n):
#     return True if n % 2 == 0 else False 
#     #return n % 2 == 0 
# main()

# name = input("What is your name? ")

# match name:
#     case "Harry" | "Ron" | "hermoine":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
#match not in this python version it is like switch 

# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

# i = 0 
# while i<3:
#     print("meow")
#     i = i + 1

# for i in range(3):
#     print("meow")


# while True:
#     n = int(input("What is n?"))
#     if n > 0:
#         break
    
# for _  in range(n):
#     print("meow")  # this will print meow n times
    

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("What is n?"))
#         if n > 0:
#             break
#     return n
        
# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

# students = ['hermoine','ron','harry']

# for i in range(len(students)):
#     print(i+1,students[i])


# students = {
#     'hermoine': 'gryffindor',
#     'ron': 'gryffindor',
#     'harry': 'gryffindor',
#     'draco': 'slytherin',
#     'neville': 'gryffindor'
# }

# for student in students:
#     print(student,students[student],sep=",  ")




# students = [
#    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#    {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]
# for student in students:
#     print(student ["name"], student ["house"], student ["patronus"], sep=", ")


# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()


# def main():
#     print_square(3)

# def print_square(size):
#    #for each row in square  
#     for i in range(size):
#     #for each brick in row
#         for j in range(size):
#     #print brick
#             print("#",end=" ")
#         print()
        
    
# main()  # Call the main function to start the program.  # Output: # # #

# while True:
#  try:
#      x = int(input("what's is x?"))
   
#  except ValueError:
#     print("x is not an integer")
#  else:
#     break

# print(f"x is {x}")



# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#                 pass

# main()


# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

#same code but diffrent way 
# from random import choice

# coin = choice(["heads","tails"])
# print(coin)

# import random 

# number = random.randint(1, 10)
# print(number)

# import random 
# cards = ["jack","queen","king"]
# random.shuffle(cards)
# for card in cards:
#     print(card)


# import statistics 

# print(statistics.mean([100,90]))


# import sys

# print("hello, my name is", sys.argv[1])
#it is 1 in square brakcets as 0 is for the file name hello.py then when we write the name in terminal it prints the ouptut hello my name is anshul 


# import sys

# if len(sys.argv) < 2:
#     print("too few arguments")
# elif len(sys.argv) > 2:
#     print("too many arguments")
    

# print("hello, my name is", sys.argv[1]) it will print only the first name as in print we are only print sys.argv[1]

# import sys #to run command line arguments we can just put in the name quickly 
# if len(sys.argv) < 2:
#     sys.exit("too few arguments")

# for arg in sys.argv[1:-1]:
#     print("hello,my name is", arg)  


# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])
# else:
#     print("Please provide a name as a command-line argument.")





# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent =2))

# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])  # print the track name of the first song in the response


# import sys

# from saying import goodbye 

# if len(sys.argv) == 2:
#     goodbye(sys.argv[1])


#to check your function write this code in a file called calculator.py
# def main():
#      x = int(input("What is x?:"))
#      print("x square is", square(x))

# def square(n):
#      return n+n


# if __name__ == "__main__":
#      main()




# from calculator import square

# def main():
#     test_square()

# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) !=9:
#         print("3 squared was not 9")

# if __name__ == "__main__":
#     main()


# names = []

# for _ in  range(3):
#      names.append(input("What is your name? "))

# for name in sorted(names):
#      print(f"hello, {name}")



# name = input("What is your name?")

# file = open("names.txt", "a")# replace w with a you can append any number of names you otherwise the code will replce the text everytime you write a diffrent name 
# file.write("f{name}\n")#\n is a new line so that each name looks cleaner
# file.close()

# with open("mnames.txt", "r") as file:
#     for line in file:
#         print("hello,",line.rstrip())#strip is used to remove the \n at the end of each line


# names = []

# with open("names.txt") as file:#with statement ensures that the file is properly closed after its suite finishes, even if an error occurs
#     for line in file:
#         names.append(line.rstrip())#The line.rstrip() method is called, which removes the newline character from the end of the line, but the result is not stored anywhere.
# #you need append() to build your list of names, while rstrip() is used to clean each line before adding it to the list.

# for name in sorted(names):#we can reverse the list using sorted(names, reverse =True):
#     print(f"hello, {name}")#rstrip is used to remove the \n at the 


#  #to create a file through terminal csv file use command nano.csv

# with open("students.csv") as file:
#     for line in file:
#         row = line.strip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# import csv

# # Create the CSV file and write data to it
# with open('students.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'House'])  # Header row
#     writer.writerow(['Hermione', 'Gryffindor'])  # Example data
#     writer.writerow(['Harry', 'Gryffindor'])      # Example data
#     writer.writerow(['Ron', 'Gryffindor'])        # Example data
#     writer.writerow(['Draco', 'Slytherin'])       # Example data
#     writer.writerow(['Neville', 'Gryffindor'])    # Example data



# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
#shows output like Hermione is in Gryffindor


# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

                                          
# if we don't want to use def get function like used above # def get_house(student):
# #     return student["house"]

#we can use 
# for student in sorted(students, key=lambda student: student["house"], reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# import csv

# students = []
# with open("students.csv") as file:
#     reader = csv.DictReader(file)#instad of csv.reader use this to make your csv file more flexible
# #when using this type it is always necessary to use row, coloumn in first row of csv file  
#     for row  in reader:
#         student = {"name": row["name"], "house": row["house"]}
#         students.append(student)

# for student in sorted(students, key= lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")



#now to write in the csv file 

# import csv 

# name = input("What is your name? ")
# house = input("What is your house? ")

# with open("students.csv", "a") as file:#a is for append mode so we can add more and more students 
#     writer = csv.writer(file)
#     writer.writerow([name, house])#this will write in csv file
    

# import csv 

# name = input("What is your name? ")
# house = input("What is your house? ")

# with open("students.csv", "a") as file:#a is for append mode so we can add more and more students 
#     writer = csv.DictWriter(file, fieldnames=["name", "house"])
#     writer.writerow({"house": house, "name": name} )#this will write in csv file


# import sys
# from PIL import Image

# # Initialize an empty list to store images
# images = []

# # Loop through command-line arguments and open images
# for arg in sys.argv[1:]:  # Skip the first argument (script name)
#     image = Image.open(arg)
#     images.append(image)

# # Save the images as a GIF
# images[0].save(
#     "costumes.gif",
#     save_all=True,
#     append_images=images[1:],  # Append all images except the first one
#     duration=200,  # Set the duration between frames
#     loop=0  # Optional: Set the loop to infinite (0)
# )



# email = input("What is your email?").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("invalid")


# import re#The re library in Python is used for regular expressions, which are a powerful tool for pattern matching and text manipulation. Regular expressions allow you to search, extract, and manipulate text based on specific patterns
# '''Key Uses of the re Library:
# 1. Pattern Matching
# Check if a string matches a specific pattern.
# Example: Validate if an email address is in the correct format.
# 2. Searching
# Search for a pattern within a string.
# Example: Find all occurrences of a word in a text.
# '''
# email = input("What's your email?").strip()

# # if re.search(r"^[^@]+@[^@]+\.edu$", email):
# #MODIFIED VERSION OF ABOVE LINE 
# if re.search(r"^\w+@\w+\.edu$", email):
#     print("valid")

# else:
#     print("invalid")  # This will print "invalid" for all invalid emails

r'''How It Works:'''
r'''^: The pattern must start at the beginning of the string.
.+: Matches one or more characters before the @ symbol.
@: Matches the literal @ symbol.
.+: Matches one or more characters after the @ symbol.
\.: Matches the literal . symbol (escaped with a backslash).
edu : Matches the literal string edu.
$: The pattern must end at the end of the string.
[^@]+: Matches one or more characters that are not the @ symbol (username part of the email).
\w+: Matches one or more word characters (a-z, A-Z, 0-9, _) for the username part of the email.
'''
# name = input("What's your name?").strip()#strip(): Removes any leading or trailing whitespace (spaces, tabs, or newlines) from the input. For example
# if "," in name:#Purpose: Checks if the name contains a comma (,)
# #Purpose: Checks if the name contains a comma (,).
#     last, first = name.split(", ")#last,first is used as in u.s people use surname, name but if we use simple we can also train  modle in a simple manner 
#     name = f"{first} {last}"

# print(f"hello, {name}")

# import re
# name = input ("What's your name? ").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):
#    name = matches.group(2) + " " + matches.group (1)
# print (f"hello, {name}")



#username = url.replace("https://twitter.com/", "")#.replace("what do you want to replace","with what you want to replace with")



# import re

# url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)#what do you want subsitute,with what,where
# #r is raw string used to match the url for twitter as it contains backlashes
# '''Suppose we want to match a string that contains a backslash (\) character. Without a raw string, we would have to escape the backslash with another backslash (\\):'''
# print(f"Username: {username}")



# import re

# url = input("URL: ").strip()

# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
#   #(the ? makes the s optional).
#   #  (?:www\.)? matches an optional www. subdomain (the ?: makes it a non-capturing group).#sometimes people directly https://twitter.com/username (no www.)
#   #  ([a-z0-9_]+) matches one or more alphanumeric characters or underscores(the + means "one or more").
#     print(f"Username:", matches.group(1))


#object oriented programming 

# def main():
#     student = get_student() #instead of name,house use student as student is a tuple containg name,house
#    #if there are some value which already value are defined eg.
#     if student[0] == "Padma":
#         student[1] == "Ravenclaw"
#     print(f"Hello, {student[0]} you are from {student[1]}")#student[0] tuple 1st element is name similarly house 

# def get_student():
#     name = input("What's your name? ").strip()
#     house = input("What's your house? ").strip()
#     return (name,house) #it is one thing with two value inside it it is a tuple
# if __name__ == "__main__":
#     main()


#classes we create are like basically mold create house
#object are the specific type we need to create 
#attritube are the instance variable of the classes 

# class Student:
#     def __init__(self, name, house, patronus):
#         self.name = name  # Uses the setter for name
#         self.house = house  # Uses the setter for house
#         self.patronus = patronus  # Uses the setter for patronus

#     # Getter and Setter for name
#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self._name = name

#     # Getter and Setter for house
#     @property
#     def house(self):
#         return self._house

#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house

#     # Getter and Setter for patronus
#     @property
#     def patronus(self):
#         return self._patronus

#     @patronus.setter
#     def patronus(self, patronus):
#         self._patronus = patronus

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🐴"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell terrier":
#                 return "🐶"
#             case _:
#                 return "/"


# def get_student():
#     name = input("What's your name? ")
#     house = input("What's your house? ")
#     patronus = input("Patronus: ")

#     return Student(name, house, patronus)


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
#     print("Expecto Patronum!")
#     print(student.charm())


# if __name__ == "__main__":
#     main()
'''__init__ that initializes the object's attributes.
__init__ Method: A special method that's called when an object is created from the class.'''
'''self Parameter:
 
The self parameter is a reference to the current instance of the class.
It is used to access the attributes and methods of the class.

In Python, raise is a keyword that is used to throw an exception. An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
for value error However, it's generally better to specify an exception type when using the raise statement. This makes it easier to catch and handle specific exceptions in your code.

Methods are the function inside a class

'''

#if we use dictionary method instead of class we can't control what goes inside eg.we can add any house in our code with dictionary but with class we can use raise method to take that if the given option house is not there it is an error


#dectorartors modify the behaviour of other function


'''Without getter and setter functions, the attributes of an object are tightly coupled to the rest of the code, making it harder to change or modify the object's behavior without affecting other parts of the program.
Getter function:always one argument 

A getter function is a method that returns the value of an attribute. It is used to access the attribute's value.

Setter function:always two argument 

A setter function is a method that sets the value of an attribute. It is used to modify the attribute's value.




'''





# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor","ravenclaw","slytherin"]
#     def sort(self,name):
#         print(name, "is in", random.choice(self.houses))

# hat = Hat()
# hat.sort("Harry")  # Output: Harry is in Gryffindor





#USING @classmethod 
# import random

# class Hat:
#     # Class attribute (shared by all instances)
#     houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]

#     def __init__(self):
#         pass  # No instance-specific initialization needed
#              #The class is simple and straightforward, and no additional initialization is needed. 
#     # Instance method (requires an instance of the class)
#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

#     # Class method (can be called on the class itself)
#     @classmethod#Class Method: A method that can be called on the class itself, without needing to create an instance of the class.
#     def sort_student(cls, name):
#         print(name, "is in", random.choice(cls.houses))
# #cls Parameter: A reference to the class itself (instead of self, which refers to the instance).

# # Using the instance method
# hat = Hat()
# hat.sort("Harry")  # Output: Harry is in Gryffindor (or another random house)

# # Using the class method
# Hat.sort_student("Hermione")  # Output: Hermione is in Ravenclaw (or another random house)
# #Purpose: Calls the sort_student class method directly on the Hat class.
# #staticmethod 




# class Wizard:
#    def _init__(self, name) :
#      if not name:
#          raise ValueError("Missing name")
#      self.name = name

# class Student (Wizard):
#     def __init__(self, name, house):
#              super().__init__(name)
#              self.house = house
# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init(name)
#         self.subject = subject
    
# wizard = Wizard("Albus")
# student = Student("Harry", "Gryffindor")
# professor = Professor("Dumbledore", "Transfiguration")










# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts
    
#     def __str__(self):#A special method that returns a string representation of the object. It is called when the object is printed or converted to a string.
#         return f"{self.galleons} Galleons, {self.sickles}  Sickles, {self.knuts} Knuts"

# potter = Vault(100, 50, 25)#Creates an instance of the Vault class with the following values:galleons = 100 sickles = 50 knuts = 25
# print(potter)


# weasly = Vault(25, 50, 100)
# print(weasly)  # Output: 25 Galleons, 50 Sickles
# #Purpose: Creates a Vault object with the specified amount of Galleons, Sickles, and

# galleons = potter.galleons + weasly.galleons
# sickles = potter.sickles + weasly.sickles
# knuts = potter.knuts + weasly.knuts

# total = Vault(galleons, sickles, knuts)
# print(total)
# #Output: 125 Galleons, 100 Sickles, 125 Knuts









# students = [
#     {"name": "Hermoine", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Neville", "house": "Gryffindor"},
#     {"name": "Luna", "house": "Ravenclaw"},
#     {"name": "Cedric", "house": "Hufflepuff"},
#     {"name": "Cho", "house": "Ravenclaw"},
#     {"name": "Ginny", "house": "Gryffindor"},
#     {"name": "Severus", "house": "Slytherin"},
# ]

# houses = [] #or we cal we list() to create empty list both same 
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
#we can do the same code above using set()
# houses = set()
# for student in students:
#     houses.add(student["house"])#we use append for list similarly we use add for list 

# #Lists can contain duplicate items.
# #Sets cannot contain duplicate items.



# for house in sorted(houses):
#  print(house) #Output: Gryffindor, Hufflepuff, Ravencl




# balance = 0 

# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:",balance)

# def deposit(n):
#     global balance#if we use global balnce we can change the value of balance which was initialized as 0 and was global variable as it is defined outside function 
#     balance += n

# def withdraw(n):
#    global balance
#    balance -= n

# if __name__ == "__main__":
#   main()









# class Account:
#     def __init__(self):
#         self._balance = 0  # Use a different name for the instance attribute
    
#     @property
#     def balance(self):#When using properties, ensure that the instance attribute has a different name (e.g., _balance) to avoid conflicts.
#         return self._balance  # Access the private attribute
    
#     def deposit(self, n):
#         self._balance += n  # Modify the private attribute
    
#     def withdraw(self, n):
#         self._balance -= n  # Modify the private attribute


# def main():
#     account = Account()
#     print("Balance:", account.balance)  # Output: Balance: 0
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balance:", account.balance)  # Output: Balance: 50


# if __name__ == "__main__":
#     main()



# import sys

# if len(sys.argv) == 1:
#     print("meow")

# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")

# else:
#     print("usage: meows.py")



# import argparse#: A Python module used to handle command-line arguments. It makes it easy to write user-friendly command-line interfaces.

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# args = parser.parse_args ()#This method processes the command-line arguments and stores them in the args object.

# for _ in range(args.n):
#    print ("meow")
'''The argparse module automatically adds a --help (or -h) argument to your script, which displays a help message describing the script's purpose and the available command-line arguments.'''
#When you run the script with --help, argparse intercepts this argument and prints the help message instead of executing the rest of the script.





# def total(galleons, sickles, knuts):
#      return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print (total (**coins), "Knuts")#total(**coins) is equivalent to total(galleons=100, sickles=50, knuts=25)
'''**coins is used for unpacking a dictionary into keyword arguments. This is often referred to as dictionary unpacking or keyword argument unpacking. It allows you to pass the key-value pairs of a dictionary as keyword arguments to a function.
nstead of manually passing each key-value pair as a keyword argument, you can pass the entire dictionary using **'''












#MAP Function whose purpose is to allow you to map that is apply some function to every elemnt of  some sequence 

# def main():
#     yell("This", "is", "CS50")

# def yell(*words) :
#     uppercased = map(str.upper, words)#map() applies str.upper to each word in words and returns a map object.
#     print(*uppercased)#The * operator unpacks the map object into individual arguments to print()


# if __name__ == "__main__":
#     main()




#enumerate :-enumerate is a built-in function that allows you to loop over a sequence (such as a list, tuple, or string) and have an automatic counter/index along with the values.



# students = ["Hermoine", "Harry", "Ron"]

# for i, student in enumerate(students):
#     print(i + 1, student)






# the yield function is used to define generators, which are a type of iterable. Generators are useful when you need to generate a sequence of values, but you don't need to store all the values in memory at once.

# def generate_sheep(n):
#     for _ in range(n):
#         yield "🐑"

# for sheep in generate_sheep(5):
#     print(sheep)