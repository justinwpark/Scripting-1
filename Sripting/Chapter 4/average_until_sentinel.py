print('This program averages numbers.')
a=float(input('Number: '))
total=0
b=0
while a!=-1:
    total=total+a
    b=b+1
    a=float(input('Number: '))
print()
print('The average is',format(total/b,'.2f'))

    
