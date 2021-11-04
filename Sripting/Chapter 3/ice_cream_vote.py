print('This program calculates valid voting results.')
a=int(input('Class 1: '))
b=int(input('Class 2: '))
c=int(input('Class 3: '))
print()
print('Groups to average:')
print((a),(b),(c))
if a>=10 and b>=10 and c>=10 and (a+b+c)>50:
    print('Results were acceptable.')
    print('Average group size was ',format((a+b+c)/3,'.2f'),'.',sep='')
else:
    print('Results were not acceptable.')

