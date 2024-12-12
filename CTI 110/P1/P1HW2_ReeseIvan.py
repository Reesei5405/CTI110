# CTI 110
# Ivan Reese
# 10/8/24
# P1HW2

print("This program calculates and displays travel expenses")
print()
budget=int(input("Enter Budget:") )
print()
Destination=(input("Enter your travel destination:") )
print()
Gas=int(input("How much do you think you will spend on gas?") )
print()
Hotel=int(input("Approximately, how much will you need for accomodation/hotel?") )
print()
Food=int(input("Last, how much do you need for food?") )
print()
total=Gas + Hotel + Food
Remaining_Balance = budget - total
print("-" * 12, "Travel Expenses",  "-" * 12)

print()
print("Location:", Destination)

print("Initial Budget:", budget)

print("Fuel:", Gas)

print("Accomodation", Hotel)

print("Food", Food)

print("total:", total)

print("Remaining Balance:", Remaining_Balance)
