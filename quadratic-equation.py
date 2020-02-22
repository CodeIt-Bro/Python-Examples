import cmath # import complex math module
a = float(input("Enter the value of a= "))
b = float(input("Enter the value of b= "))
c = float(input("Enter the value of c= "))
d = (b**2) - (4*a*c) ## calculate the discriminant
sol1 = (-b-cmath.sqrt(d))/(2*a) # Calculating the first solution
sol2 = (-b+cmath.sqrt(d))/(2*a) # Calculating the second solution
print('The solution of your quadratic equation are {0} and {1}'.format(sol1,sol2))