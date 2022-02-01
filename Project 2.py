a = int(input("projectmarks"))
b = int(input("internalmarks"))
c = int(input("externalmarks"))
if a>=50 and b>=50 and c>=50:
    total=(70*a/100+b*20/100+10*c/100)
    print("Total marks:",total)
    if total>=90:
        print("A grade")
    elif total>=75:
        print("B grade")
    else:
        print("C grade")
if a<50:
    print("You failed in the Project",a)
if b<50:
    print("You failed in the internal",b)
if c<50:
    print("you failed in the external",c)
    
    