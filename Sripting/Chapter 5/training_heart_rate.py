def THR(age, restRate):   
    maxh=220-age
    step2=maxh-restRate
    result=(step2*.6)+restRate
    print('Your training heart rate is:',format(result,'.2f'))

def main():
    age=int(input('Enter your age: '))
    restRate=int(input('Enter your resting heart rate: '))
    THR(age, restRate)

main()
