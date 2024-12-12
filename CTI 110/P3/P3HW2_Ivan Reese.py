# CTI 110
# P3HW2
# Ivan Reese
# Salary Calulater

print ("$$$This is my employee salary calculater$$$")
print ("-------------------------------------------")
name = input("Enter Employee's Name:")
hours = float(input("How many hours has worked?:"))
pay = float(input("Please enter your hourly pay rate:$"))
print ("-----------------------------------------")
print ("Employee's Name:",(name))

otp = hours + hours / 2
rhp = hours * pay
gp = otp + rhp
if hours >= 40:
    ot = hours - 40
print (" Hours Worked     Pay Rate          OverTime     Over Time Pay     RegHour Pay     Gross Pay")
print ("===============================================================================================")
print (f' {hours}            ${pay:<10.2f}         {ot:<10.2f}  ${otp:<10.2f}       ${rhp:<10.2f}     ${gp:<10.2f}')






