print('This program analyzes text. Enter text or enter "quit" to quit.')

def sometext():
    x=input('Please enter some text: ')
    y=''
    while x!='quit':
        y=y+x
        x=input('Please enter some text: ')
    return y

def main():
    total_of_upper=0
    total_of_lower=0
    total_of_digits=0
    total_of_white=0
    u=sometext()
    for x in u:
        if x.isspace():
            total_of_white+=1
    for x in u:
        if x.isupper():
           total_of_upper+=1
    for x in u:
        if x.islower():
            total_of_lower+=1
    for x in u:
        if x.isdigit():
            total_of_digits+=1
            
        
    print('There are',(total_of_upper),'uppercase letters in this text.')
    print('There are',(total_of_lower),'lowercase letters in this text.')
    print('There are',(total_of_digits),'digits in this text.')
    print('There are',(total_of_white),'whitespace characters in this text.')


main()
