#CTI 101
# P3LAB1 - Choose you own adventure
# Reese
# 10/22/24

def main():
    print("Choose your own adventure")
    go_home()

def go_home():
   
    print("you decide to go home")
    print("But should get some food")
    print("1.  Order pizza")
    print("2.  Get Chinese")
    print("3. Get Zaxbys")
    choice = int(input())
    if choice == 1:
        get_pizza()
    if choice == 2:
        get_chinese()
    if choice == 3:
        get_zaxbys()



def get_pizza():
    
    print("The driver doesn't get the food to you on time so it's free.")
def get_chinese():
   
    print("GOOD ENDING")
def get_zaxbys():
   
    print("Your Dasher is on the way.")
    
    print("print you decided to doordash Zaxbys")
    print("While waiting you can either watch TV or play the game")
    print("1. Get on the game")
    print("2. Go watch tv")
    choice = int(input())
    if choice == 1:
        get_on_game()
    if choice == 2:
        go_watch_tv() 



def get_on_game():
    pass
    print("You hop on with the boys and start raging.", " When the dasher arrives he hears screaming.", "The dasher quickly leaves the premises after leaving the food at the door.")
def go_watch_tv():
    pass
    print("You put on a scary movie and the dasher shows up at the jumpscare.")
    print("Your dasher stabs you as soon as you open the door.")
    print("Your dasher is a serial killer that's on the run.")
    print("You lose.")


# start the program
main()