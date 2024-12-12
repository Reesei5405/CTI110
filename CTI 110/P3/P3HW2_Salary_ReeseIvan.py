# CTI110
# P3HW2
# 11/12/24
# P3HW2_Salary_ReeseIvan

name =input("Enter employee's name:")
hour =float(input("Enter number of hours worked:"))
pay =float(input("Enter employee's pay rate:"))

print("-" * 40)

print("Employee name:", name)

otp = hour + hour/2
rhp = hour * pay
gp = otp + rhp
if hour >= 40:
        ot= hour -40
        
print("hours worked        Pay Rate     Over time    OverTime Pay      RegHour Pay        Gross Pay")
print("-" * 80)
print(f' {hour}            ${pay:<10.2f}     {ot:<10.2f}        ${otp:<10.2f}         ${rhp:<10.2f}    ${gp:<10.2f}')
