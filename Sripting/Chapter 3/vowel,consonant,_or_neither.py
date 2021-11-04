print('This program determines whether a character is a vowel, a consonant, or neither.')
print()
letter=input('Enter a character: ')
if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        print((letter),'is a vowel.')
else:
        if ((letter=='q') or (letter=='w') or (letter=='r') or (letter=='t') or (letter=='y') or (letter=='p') or (letter=='s') or (letter=='d') or (letter=='f') or (letter=='g') or (letter=='h') or (letter=='j') or (letter=='k') or (letter=='l') or (letter=='z') or (letter=='x') or (letter=='c') or (letter=='v') or (letter=='b') or (letter=='n') or (letter=='m')):              
                print((letter),'is a consonant.')
        else:
                print((letter),'is neither a vowel nor a consonant.')
        
                
