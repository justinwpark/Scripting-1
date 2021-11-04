print('This program determines the number of letters or numbers that are in their correct place.')
x1=input('Enter character 1: ')
x2=input('Enter character 2: ')
x3=input('Enter character 3: ')
x4=input('Enter character 4: ')
x5=input('Enter character 5: ')
total=0
if (x1=='a' or x1=='1'):
    total=total+1
if (x2=='b' or x2=='2'):
    total=total+1
if (x3=='c' or x3=='3'):
    total=total+1
if (x4=='d' or x4=='4'):
    total=total+1
if (x5=='e' or x5=='5'):
    total=total+1
print('The number of letters or numbers in their correct places is',(total))
