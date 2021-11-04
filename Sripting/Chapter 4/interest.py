a=int(input('Initial investment: '))
b=float(input('Interest rate: '))
c=int(input('Years: '))
total=a
for c in range (1,(c+1)):
    total=total+((b*.01)*(a))
    a=total
print('Your account will total $', format(total,'.2f'),' after ', (c),' years.',sep='')

