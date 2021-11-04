def factorial(n):
    total=1
    while n>0:
      total=total*n
      n=n-1
    return total

def Combinations(n,k):
    comb=(factorial(n))//(factorial(k)*(factorial(n-k))) 
    return comb

def main():
    n=int(input('Enter an Integer: '))
    k=int(input('Enter another Integer: '))
    print('Combinations(',n,',',k,') = ',(Combinations(n,k)),sep='')

main()

