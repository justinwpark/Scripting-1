print('This program identifies the largest of three numbers.')
print()
a=int(input('Enter integer: '))
b=int(input('Enter integer: '))
c=int(input('Enter integer: '))

if a>=b and a>=c:
    print('The largest number is ',(a),'.',sep='')
else:
    if b>=a and b>=c:
        print('The largest number is ',(b),'.',sep='')
    else:
        if c>=a and c>=b:
            print('The largest number is ',(c),'.',sep='')
        

    
