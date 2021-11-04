print('This program calculates area or volume.')
a=input('Would you like to calculate area or volume? ')
print()
if a=='area':
    b=input('Would you like to calculate the area of a triangle or a circle? ')
elif a=='volume':
    b=input('Would you like to calculate the volume of a cylinder or a sphere? ')
elif a!='area' and a!='volume':
    print("Invalid input.")
    b=()
    
if b=='triangle':
        d=float(input('Enter the base: '))
        e=float(input('Enter the height: '))
elif b=='circle':
        f=float(input('Enter the radius: '))
elif b=='cylinder':
    g=float(input('Enter the height: '))
    h=float(input('Enter the radius: '))
elif b=='sphere':
    i=float(input('Enter the radius: '))
else:
    print("Invalid input.")

if b=='triangle':
    print('The area is',format(((d*e)/2),".2f"))
elif b=='circle':
    print('The area is',format(((3.14)*(f**2)), ".2f"))
elif b=='cylinder':
    print('The volume is',format(((3.14)*(h**2)*g), ".2f"))
elif b=='sphere':
    print('The volume is',format(((4/3)*(3.14)*(i**3)), ".2f"))
else:
    print("Invalid input.")

    




