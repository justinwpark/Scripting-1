print('This program calculates an average grade.')

def average(a,b,c):
    return (format((a+b+c)/3,'.1f'))

def main():
    ID=input('Enter the student ID number and last name: ')
    x=int(input('Grade 1: '))
    y=int(input('Grade 2: '))
    z=int(input('Grade 3: '))
    avg=average(x,y,z)
    print()
    x1=''
    for x in ID:
        if x.isalpha():
            x1+=x
    print(x1,(avg))

main()
