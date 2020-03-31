year = int(input("enter the year: "))
if year % 4 == 0:
   if year % 100 == 0:
       if year % 400 == 0:
           print('%0.0f is a leap year' % year)
       else:
           print('%0.0f is not a leap year' % year)
   else:
       print('%0.0f is a leap year' % year)
else:
       print('%0.0f is not a leap year' % year)