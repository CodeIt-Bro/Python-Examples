terms = int(input("Enter the number of terms till which you want to find the sum: "))
n = terms
if terms < 0:
    print("Enter positive numbers of terms")
else:
    sum = 0
    while (terms > 0):
        sum = sum + terms
        terms = terms - 1
print("Sum of", n, "terms =", sum)
