# CTI 110
# 10/24/24
# P2HW2
# Getting four numbers mean

# ask the user to enter four numbers
x = 3.14159
formatted_x = "{:.2f}".format(x)  # formats x to 2 decimal places
(formatted_x)
num1 = float(input("Enter grade for Module 1:"))

Mean = num1
print("average:", Mean)
print("-" *32)

   
if Mean >= 90:
            grade =' A'
elif Mean >=80:
            grade = 'B'
elif Mean >=70:
            grade = 'C'
elif Mean >=60:
           grade = 'D'
if Mean <=50:
            grade = 'F'



print("Your grade is:", grade)
