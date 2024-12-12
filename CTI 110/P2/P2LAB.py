# Ivan Reese
# 10/17/24
# P2LAB2 - List

# ask the user to enter four numbers
print("Please enter four numbers(enter after each)")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

Numbers=[num1, num2, num3, num4]
print("you entered these numbers:", Numbers)

print("There are", len(Numbers),"numbers.")
print("Smallest:", min(Numbers))
print("Largest:", max(Numbers))
print("The total is: ", sum(Numbers))
average = sum(Numbers) /len(Numbers)
print("The average:", average)



# Part 2 Turtle - Graphics
for number in Numbers:
    print(number)

# Next, draw using for loops
