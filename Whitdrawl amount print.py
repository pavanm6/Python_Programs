#WAP to accept withdraw amount and print number of notes:
# 200,100,50,20,10


amount=int(input("Enter amount"))
a=0
b=0
c=0
d=0
e=0
if amount%10==0:
    if amount>=200:
        a=amount//200
        amount=amount-(200*a)
        print("200 rupees are:",a)
    if amount>=100:
        b=amount//100
        amount=amount-(100*b)
        print("100 rupees are:",b)
    if amount>=50:
        c=amount//50
        amount=amount-(50*c)
        print("50 rupees are:",c)
    if amount>=20:
        d=amount//20
        amount=amount-(20*d)
        print("20 rupees are:",d)
    if amount>=10:
        e=amount//10
        amount=amount-(10*e)
        print("10 rupees are:",e)
else:
    print("Not vaild money")
        
        