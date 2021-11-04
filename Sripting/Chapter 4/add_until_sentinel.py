print('Enter a list of numbers, using a negative number to indicate that you are done.')
a=float(input('Enter a number: '))
total=0
while a>=0:
    total=total+a
    a=float(input('Enter a number: '))
print()
print('The total is',total)

