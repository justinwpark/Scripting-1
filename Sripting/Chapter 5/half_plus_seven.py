print('Dating age calculator.')
def half_plus_seven(age):
    prop=age/2+7
    return prop

def main():
    num1=int(input('Enter your age: '))
    print('Your age is',(num1))
    print('Minimum age is', half_plus_seven(num1))

main()
