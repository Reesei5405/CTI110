#CTI 110
#P4LAB2
#11/08/2024
#Reese
#mutiplication_program


def mtp():
    
    n = int (input("enter the number:"))
    if n <0:
            print("This program does not handle negative numbers")
    elif n >=0:      
        for i in range(1,13):
            print(n,"*",i,"=",n*i)
    rpt = input("Would you like to choose a different number? yes or no: ").lower()
    if rpt == "yes":
        mtp()
    elif rpt== "no":
      
           

