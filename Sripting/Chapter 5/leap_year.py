print('This program determines if a year is a leap year.')

def isLeapYear(a):
    if a%4==0 and a%100!=0 or a%400==0:
        return True

def main():
    year=int(input('Enter a year: '))
    if isLeapYear(year) is True:
        print(year,'is a leap year.')
    else:
        print(year,'is not a leap year.')

main()
