print('This program converts a phrase into an acronym.')

def main():
    x=input('Please enter a phrase or "quit": ')
    while x!='quit':
        y=acronym(x)
        print('The acronym for this phrase is ',(y),'.',sep='')
        x=input('Please enter a phrase or "quit": ')

def acronym(x):
    a=x.replace(' and ', ' ')
    a=a.upper()
    arc=''
    y=a.find(' ')
    while y!=-1:
        arc=arc+a[ :1]
        y=a.find(' ')
        a=a[y+1:]
    return arc

main()
