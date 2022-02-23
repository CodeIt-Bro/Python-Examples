# Program to check if a number is prime or not

#Take input from user to check 
num = int(input("Enter a number to check: "))

#Setting up a flag to update prime number status
check = False

#Checking if a number is prime or not with conditional and loop statements
if num>1:
    for i in range(2, num):
        if(num%i) == 0:
            check = True
            break

#Displaying if a number is prime or not
if check:
    print("Number is not a prime number")

else:
    print("Number is a prime number")