a=int(input('How many days did you work? '))
print('Day     Salary')
print('--------------')
x=.01
day=1
total=0
c=.01
for a in range (1,(a+1)):
    print((day),'       ','$',format(x,'.2f'),sep='')
    x=x*2
    day=day+1
    total=total+c
    c=c*2
print()
print()
print('Total salary: $',format(total,'.2f'),sep='')
      
      
      
