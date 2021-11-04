print('This program calculates a letter grade average.')
print('Enter scores, or -1 to quit.')
print()
a=float(input('Enter numeric score: '))
total=0
b=0
while a!=-1:
    total=total+a
    b=b+1
    a=float(input('Enter numeric score: '))
x=total/b
if x>=90:
    print('Grade: A')
elif x>=80:
    print('Grade: B')
elif x>=70:
    print('Grade: C')
elif x>=60:
    print('Grade: D')
else:
    print('Grade: F')
    
