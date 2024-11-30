#Parentheses > Exponentiation > Multiplication = Division = Integer Division = Modulo > Addition = Subtraction

'''
minutes = 856
hours = minutes // 60
remaining_minutes = minutes%60
print(f"Time remaining: {hours} : {remaining_minutes}")
'''
'''
jack_age = 23
alex_age = 42
lana_age = 34
print(min(jack_age, alex_age, lana_age))
'''
'''
def minmax(a,b):
  if a > b:
    print(a)
    print(b)
  else:
    if b > a:
      print(b)
      print(a)
    else:
      print(a)
      print(b)

a = int(input(3))
b = int(input(4))
minmax(a,b)
'''
'''
num = -12
if num < 0:
  num*=-1
  print((num))
  print("The number is positive")
else:
  num*=-1
  print(num)
  print("The number is negative")
  '''
'''
A = 7
B = 9
H = 2
if A <= H <= B:
  print("Normal")
if H < A:
    print("Deficiency")
else:
  if H > B:
    print("Excess")
'''
'''
#Leap Year
# Write a program that checks if a year is leap.
# A year is considered leap if it is divisible by 4 and NOT divisible by 100, or if it is divisible by 400. So, 2000 is leap and 2100 isn't.
# Output either "Leap" or "Ordinary" depending on the input.
year = 2000
if year%4 == 0 and year%100 != 0 or year%400 == 0:
  print("Leap")
else:
  print("Ordinary")
'''
'''
# Write your code here
print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
print("Income: $5405.0")
print("Staff expenses:")
staff = int(input())
print("Other expenses:")
other = int(input())
net = 5405 - staff - other
print(f"Net income: ${net}")
'''
bubblegum, toffee, iceCream, milkChocolate, doughnut, pancake = 202, 118, 2250, 1680, 1075, 80
income = sum([bubblegum, toffee, iceCream, milkChocolate, doughnut, pancake])
print("""Earned amount:
Bubblegum: ${}
Toffee: ${}
Ice cream: ${}
Milk chocolate: ${}
Doughnut: ${}
Pancake: ${}

Income: ${}""")