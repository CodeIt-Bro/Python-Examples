num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
num3 = float(input("enter 3rd number: "))

if (num1 > num2) and (num1 > num3):
   largest_num = num1
elif (num2 > num1) and (num2 > num3):
   largest_num = num2
else:
   largest_num = num3
print("the largest number= ", largest_num)