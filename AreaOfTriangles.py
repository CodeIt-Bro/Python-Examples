#base = input('Enter the base of the triangle:');  # Taking base input from user
#base = float(base);  # Converting string input data to float type
#height = input('Enter the height of the triangle');  # Taking height input user
#height = float(height);  # Converting string input data to float type
#Area = float((base * height) / 2);  # Calculateing the area of the triangle using (Base * Height)/2
#print('Area of triangle', Area);  # Outputting the area of the triangle

import math
Side1 = float(input('Enter the first side of the triangle = ')) #First side of the triangle
Side2 = float(input('Enter the second side of the triangle = ')) #Second side of the triangle
Side3 = float(input('Enter the third side of the triangle = ')) #Third side of the triangle
S = float(((Side1+Side2+Side3)/2)) #Calculating semi perimeter
Area = float((S*(S-Side1)*(S-Side2)*(S-Side3))) #Solving Heron's expression within square root
Area = math.sqrt(Area) #Calculating the square root to find the area
print("Area of the triangle = ", Area) #Outputting the area of the triangle.