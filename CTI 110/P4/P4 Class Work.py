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
