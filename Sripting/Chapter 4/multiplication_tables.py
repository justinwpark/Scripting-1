a=int(input('Which number would you like to see the multiplication table for? '))
b=int(input('What is the lowest number for the table? '))
c=int(input('What is the highest number for the table? '))
x=(a*b)
for b in range (b,c+1):
    print((a),'*',(b),'=',(x))
    b=b+1
    x=x+a
