# CTI 110
# Ivan Reese
# 10/10/24
# P2LAB1
# Variables and Expressions
hotdog = 0
drink = 0
hotdog_cost = 1.50
drink_cost = 2.00
answer = (input("Hello would you like to buy a hotdog?") )
hotdog = int(input("How many hotdog's would you like?"))
answer = input ("Would you like a drink with that?")
if answer == "yes":
   drink = int(input("How many?"))

input("Would that be all?")


# Add totals

hotdog_total = hotdog * hotdog_cost
drink_total = drink * drink_cost
meal_total = hotdog_total + drink_total
# Receipt
print("-" * 25)
print(hotdog, "hotdogs\t$", format(hotdog_total, ".2f")  )
print()
print(drink, "drinks\t$", format(drink_total, ".2f")  )
print()
print("-" * 25)
print("total\t$", meal_total)
