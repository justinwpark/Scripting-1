print('This program adds odd numbers, and multiplies even numbers.')
print('Enter 0 or a negative number to exit.')
a=int(input('Enter a positive integer: '))
total=0
while a>0:
    if a%2==0:
        total=total*a
    else:
        total=total+a
    a=int(input('Enter a positive integer: '))
print('The final number is',total)
    
    
