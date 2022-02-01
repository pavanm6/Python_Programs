#WAP to accept withdraw amount and print number of notes.
#consider we have 500,200 and 100 rupees notes 
#Sample input:
#  4800
#   output:
 #  500 rupees are :9
 # 200 rupees are:1
 # 100 ruppes are :1
amount=int(input("Enter withdraw amount"))
a=0
b=0
c=0
if amount>=500:
    a=amount//500
    amount=amount-(500*a)
    print("500 rupees notes are :",a)
if amount>=200:
    b=amount//200
    amount=amount-(200*b)
    print("200 rupees notes are :",b)
if amount>=100:
    c=amount//100
    print("100 rupees notes are :",a)

 


 
 
 