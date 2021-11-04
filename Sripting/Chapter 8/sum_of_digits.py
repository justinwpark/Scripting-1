print('This program adds together numbers.')

def main():
    a=input('Please enter a string of numbers:')
    total=0
    for x in a:
        total=total+int(x)
    print('The sum of these digits is ',(total),'.',sep='')

main()
