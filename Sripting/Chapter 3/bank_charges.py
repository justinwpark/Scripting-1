a= int(input('How many checks written for the month: '))
b=20
c=39
d=59
e=60
if a<=0:
    print("Please enter a positive number.")
else:
    if a<=b:
        print('Number of Checks:',(a))
        print('Total Fees: $',format(((a*.10)+10),'.2f'),sep='')
    else:
        if a<=c:
            print('Number of Checks:',(a))
            print('Total Fees: $',format(((a*.08)+10),'.2f'),sep='')
        else:
            if a<=d:
                print('Number of Checks:',(a))
                print('Total Fees: $',format(((a*.06)+10),'.2f'),sep='')
            else:
                print('Number of Checks:',(a))
                if a>=e:
                        print('Total Fees: $',format(((a*.04)+10),'.2f'),sep='')
