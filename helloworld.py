msg = "\n\nQuiz: What Type of Fruit Are You?\n"
print (msg)

#Questions 

repeat = ""
while repeat != "no":
    repeat = input("Would you like to play this game? \nyes\nno\n")
    points = 0
    if repeat == "yes":
        Q1 = ""
        while Q1 != "A" or Q1 != "B":
            Q1 = input("\nSweet or Sour? \nA) Sweet \nB) Sour\n")
            if Q1 == "A":
                points += 1
                break 
            elif Q1 == "B":
                points += 2 
                break 

        Q2 = ""
        while Q2 != "A" or Q2 != "B":
            Q2 = input("Tropical getaway or Countryside? \nA) Tropical getaway \nB) Countryside\n")
            if Q2 == "A":
                points += 1
                break 
            elif Q2 == "B":
                points += 2 
                break 

        Q3 = ""
        while Q3 != "A" or Q3 != "B" or Q3 != "C" or Q3 != "D":
            Q3 = input("What color would you choose? \nA) Red \nB) Yellow \nC) Green \nD) Blue\n")
            if Q3 == "A":
                points += 1
                break
            elif Q3 == "B":
                points += 2
                break
            elif Q3 == "C":
                points += 3
                break
            elif Q3 == "D":
                points += 4
                break


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
            fruit = "Pineapple"
        elif points == 8:
            fruit = "Grape"
        else:
            fruit = "Blueberry"
        print ("Your fruit is a(n) " + fruit + "\n\n")
        points = 0; 
    
    elif repeat == "no":
        print ("\nThank you for playing.\n")
        break