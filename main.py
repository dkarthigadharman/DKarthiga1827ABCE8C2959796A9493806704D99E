#leap year

"""
year % 4 == 0 &
year % 100 ! 0 /
year % 400 == 0

"""
def  isleapyear(year):
   if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
      return True
   else:
     return False     

year = 2013

if isleapyear(year):
    print ('{} is a leap year.'.format(year))
else:
  print('{} is a not leap year .'.format(year))
  