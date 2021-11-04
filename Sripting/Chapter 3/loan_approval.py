print('This program determines whether you may get a loan.')
a=int(input('Please enter your income in dollars: '))
b=int(input('Please enter your credit rating: '))
c=input('Please enter if you are using collateral (yes or no): ')
if (a>=50000 and b>=600) or (c=='yes'):
    print('Approved!')
else:
    print('We are sorry, but you are not approved.')
