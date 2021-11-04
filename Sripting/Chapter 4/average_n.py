print('This program averages numbers.')
print()
a=int(input('How many numbers? '))
total=0
for a in range (1,(a+1)):
    b=float(input('Number: '))
    total=total+b
print()
print('The average is',format(total/a,'.1f'))
    
