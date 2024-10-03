# CTI 110
# P1LAB2 - Receipt
# Reese
# 10/1/24


print('P1LAB2')
# For today, let's do a resturant
# that only sells burgers and fries

num_burgers = 0
num_fries = 0
burger_cost = 4.99
fry_cost = 1.99
print('Can I take your order')

num_burgers = int(input ("How many burgers? "))
answer = input("Would you like that with fries?")
if answer == "yes":
    num_fries = int(input ("How many orders of fries would you like?"))

input("would that be all?")

#Add up all the totals
burger_total = num_burgers * burger_cost
fry_total = num_fries * fry_cost
meal_total = burger_total + fry_total

# print the receipt
print("-" * 25)
print(num_burgers,"🍔 burgers\t$",format( burger_total, ".2f") )
print(num_fries,"🍟 fry\t\t$",format( fry_total, ".2f") )
print("-" * 25)
print("Total\t\t$",meal_total)
