def captalize(s):
    s=s.split(" ")
    for i in range(0,len(s)):
        s[i]=s[i].capitalize()
    s=' '.join(s)
    return s
    
y=True
while(y):
    x=input("Enter the String you want to captalise:")
    print(captalize(x))
    print()
    c=input("do you want to captalise another  string:(Y/N)")
    if c=='y'or c=='Y':
        y=True
    else:
        y=False

