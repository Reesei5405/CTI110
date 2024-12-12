'''
print("test program")
count=1
while count <= 59:
    print("count is", count)
    count = count + 1
print("done")
for number in range (1,59):
    print(number)
print("done")

# input validation
num = int(input("Type a number from 1 to 3"))
while num < 1 or num> 3:
    print("Please try again")
    num= int(input("Type a number from 1 to 3"))
print("You entered:", num)
'''
# P4LAB2
# CTI 100
# Reese
# 11/14/24


def time_table():
    num= int(input("Enter a number:"))
    while(num < 0):
        print("No negative numbers please.")
        num = int(input("Enter a number:"))
    print("you entered",num)
    # finally, do the time table
    for num2 in range(1,13):
        answer = num * num2
        print(num,"*",num2,"=",answer)
                    

    
def main():
    time_table()
    again =input("Do you want to run again?")
    while (again =="yes"):
        time_table()
        again =input("Do you want to run again?")
    print("Goodbye!")

# Start program
main()
