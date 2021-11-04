print('This program calculates the factorial of a number. Enter a number or -1 to quit.')

def factorial(n):
    total=1
    while n>0:
      total=total*n
      n=n-1
    return total

def main():
    n=int(input('Enter a number or -1: '))
    while n!=-1:
      print('Factorial =',(factorial(n)))
      n=int(input('Enter a number or -1: '))

main()
