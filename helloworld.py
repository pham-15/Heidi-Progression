msg = "\n\nQuiz: What Type of Fruit Are You?\n"
print (msg)

#points 
points = 0

#Questions 

Q1 = input("Sweet or Sour? \nA) Sweet \nB) Sour\n")
if Q1 == "A":
    points += 1
elif Q1 == "B":
    points += 2
else: 
    print("The answer you put in is not an answer choice please try again.\n")
    Q1 = input("Sweet or Sour? \nA) Sweet \nB) Sour\n")
    if Q1 == "A":
        points += 1
    elif Q1 == "B":
        points += 2

Q2 = input("Tropical getaway or Countryside? \nA) Tropical getaway \nB) Countryside\n")
if Q2 == "A":
    points += 1
elif Q2 == "B":
    points += 2
else: 
    print("The answer you put in is not an answer choice please try again.\n")
    Q2 = input("Tropical getaway or Countryside? \nA) Tropical getaway \nB) Countryside\n")
    if Q2 == "A":
        points += 1
    elif Q2 == "B":
        points += 2

Q3 = input("What color would you choose? \nA) Red \nB) Yellow \nC) Green \nD) Blue\n")
if Q3 == "A":
    points += 1
elif Q3 == "B":
    points += 2
elif Q3 == "C":
    points += 3
elif Q3 == "D":
    points += 4
else:
    print("The answer you put in is not an answer choice please try again.\n")
    Q3 = input("What color would you choose? \nA) Red \nB) Yellow \nC) Green \nD) Blue\n")
    if Q3 == "A":
        points += 1
    elif Q3 == "B":
        points += 2
    elif Q3 == "C":
        points += 3
    elif Q3 == "D":
        points += 4


print ("\n\nThe total point: " + str(points) + "\n")

fruit = ""
if points == 3:
    fruit = "Apple"
elif points == 4:
    fruit = "Papaya"
elif points == 5:
    fruit = "Grapefruit"
elif points == 6:
    fruit = "Orange"
elif points == 7:
    fruit = "Apple"
elif points == 8:
    fruit = "Grape"
else:
    fruit = "Blueberry"
print ("Your fruit is a(n) " + fruit)