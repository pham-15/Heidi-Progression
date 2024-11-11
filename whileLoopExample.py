# Adjust questions to use while loops
# Make the game ask user if they want to play again

color = ""
while color != "A" or color != "B":
    color = input("Which of the following is your favorite color: \nA) Red \nB) Blue\n")
    if color == "A":
        print("Red is your favorite color")
        break
    elif color == "B":
        print("Blue is your favorite color")
        break
    else:
        print("Your input was invalid, try again")