print('This program reads 7 characters and prints how many are vowels.')
x1=input('Enter a character: ')
x2=input('Enter a character: ')
x3=input('Enter a character: ')
x4=input('Enter a character: ')
x5=input('Enter a character: ')
x6=input('Enter a character: ')
x7=input('Enter a character: ')
total=0
if x1=='a' or x1=='e' or x1=='i' or x1=='o' or x1=='u':
    total=total+1
if x2=='a' or x2=='e' or x2=='i' or x2=='o' or x2=='u':
    total=total+1
if x3=='a' or x3=='e' or x3=='i' or x3=='o' or x3=='u':
    total=total+1
if x4=='a' or x4=='e' or x4=='i' or x4=='o' or x4=='u':
    total=total+1
if x5=='a' or x5=='e' or x5=='i' or x5=='o' or x5=='u':
    total=total+1
if x6=='a' or x6=='e' or x6=='i' or x6=='o' or x6=='u':
    total=total+1
if x7=='a' or x7=='e' or x7=='i' or x7=='o' or x7=='u':
    total=total+1
if total==0:
    print('there are',(total),'vowels')
else:
    if total==1:
        print('In this set of characters there is',(total),'vowel.')
    else:
        if total>=2:
            print('In this set of characters there are',(total),'vowels.')
    
