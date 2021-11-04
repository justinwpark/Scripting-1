PI=3.14159
print('This program computes the surface area of a sphere.')

def sphereArea(radius):
    area=4*PI*radius**2
    return area

def main():
    radius=float(input('Enter the radius: '))
    print('The surface area is',format(sphereArea(radius),'.2f'))

main()


     
