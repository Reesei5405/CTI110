# CTI 110
# 10/24/24
# P2HW2
# Getting four numbers mean

# ask the user to enter four numbers

num1 = float(input("Enter grade for Module 1:"))
num2 = float(input("Enter grade for Module 2:"))
num3 = float(input("Enter grade for Module 3:"))
num4 = float(input("Enter grade for Module 4:"))
num5 = float(input("Enter grade for module 5:"))
num6 = float(input("Enter grade for module 6:"))
Numbers=[num1, num2, num3, num4, num5, num6]


print("-"*12, "Results", "-"* 12)
print("Lowest Grade:", min(Numbers))
print("Highest Grade:", max(Numbers))
print("Sum of Grade: ", sum(Numbers))
average = sum(Numbers) /len(Numbers)
print("average:", average)
print("-" *32)
