PI=3.14159
print('This program computes the volume of a sphere.')

def sphereVolume(radius):
    volume=4/3*PI*radius**3
    return volume

def main():
    radius=float(input('Enter the radius: '))
    print('The volume is',format(sphereVolume(radius),'.2f'))

main()
