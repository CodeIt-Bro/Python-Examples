#Program to convert Celsius to Fahrenheit 

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print('%0.1f celsius = %0.1f Fahrenheit' % (celsius, fahrenheit))

#Program to convert Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: ")) 
celsius = (fahrenheit - 32) / 1.8 
print('%0.1f Fahrenheit = %0.1f Celsius' % (fahrenheit, celsius))