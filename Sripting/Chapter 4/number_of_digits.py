print('This program determines the number of digits in a number.')
print('Enter a number, or 0 to quit.')
a=int(input('Enter a number: '))
b=a
total=0


while a!=0:   
    while b!=0:
        b=b//10
        total=total+1
    if total==1:
        print('There is',total,'digit in',a)
    else:
        print('There are',total,'digits in',a)
    print()
    a=int(input('Enter a number: '))
    b=a
    total=0

    
