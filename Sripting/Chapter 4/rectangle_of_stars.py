a=int(input('How wide would you like the rectangle to be?'))
b=int(input('How long would you like the rectangle to be?'))
total=''
for b in range (1,b+1):
    for a in range (1,a+1):
        total=total+'*'
    print(total)
    total=''
