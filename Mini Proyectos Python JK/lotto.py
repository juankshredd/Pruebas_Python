print("Welcome To Lotto Games Lucky Number Picker Program")
input ("Press Enter To Continue. . .")
print("----------------------------------------")
print()
import random
print("Lotto Games Lucky Pick Set 1")
print ("\nLotto 6/42:\n")
randomlist = []
for i in range(0,6):
        n= random.randint(1,42)
        randomlist.append(n)
print(randomlist)
 # check if i is unique and has a value from 1 to 42
print ("\nMega Lotto 6/45:\n")
import random
randomlist = []
for i in range(0,6):
    n= random.randint(1,45)
    randomlist.append(n)
print(randomlist)
 # check if it is unique and has a value from 1 to 45
print ("\nSuper Lotto 6/49:")
import random
randomlist = []
for i in range(0,6):
    n= random.randint(1,49)
    randomlist.append(n)
print(randomlist)
 # check if its unique and has a value from 1 to 49
print ("\nGrand Lotto 6/55:")
import random
randomlist = []
for i in range(0,6):
    n= random.randint(1,55)
    randomlist.append(n)
print(randomlist)
 # check if its unique and has a value from 1 to 55
print ("\nUltra Lotto 6/58:")
import random
randomlist = []
for i in range(0,6):
    n= random.randint(1,58)
    randomlist.append(n)
print(randomlist)
 # check if its unique and has a value from 1 to 58
print("--------------------------------------")
print("\nDo you want to generate new set of Lucky Picked Numbers?\n")
print ('-Enter "yes" to generate new set of Lucky Picked Numbers')
print ('-Enter "no" to exit the program')
print()
choice=input("Your Answer:")
if choice== "yes":
    print ("--------------------------------------")
    print("\nLotto Games Lucky Pick Set 2") 
elif choice =="no":
    print("\nThank You For Using Lotto Game Lucky Picker Program,Goodbye!")
    exit()
else:
    print("Invalid Response!")
    choice=input("Answer again:")