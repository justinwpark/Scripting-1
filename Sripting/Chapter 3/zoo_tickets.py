print('This program calculates the price to enter a zoo based on age.')
age=int(input('Enter your age: '))
print('You entered age',(age))
if age<=2:
        print('Admission is free.')
else:
    if age>=3 and age<=10:
        print('Admission is $5.')
    else:
        if age>=11 and age<=20:
            print('Admission is $10.')
        else:
            if age>=21 and age<=59:
                print('Admission is $20.')
            else:
                if age>=60:
                    print('Admission is $10.')
