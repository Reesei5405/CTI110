# CTI 110
# 10/29/24
# P3LAB2
# Games
import random 


def main():
    print("Craps Game")
    print("roll 1 to 6")
   # die1 =int(input("First Die:"))
   # die2 = int(input("Second Die:"))
   # Random rolls

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)


    total = die1 + die2
    print("Roll:",die1, "+", die2,"is",total)



    if total ==7:
        print("You Win!")
    elif total == 11:
        print("You Lose")
    elif total == 2:
        print("You Win!")
    elif total == 12:
        print("You Lose")
    else:
        print("Point was", total)
        print("To be continued...")
    
    
# start program
main()
