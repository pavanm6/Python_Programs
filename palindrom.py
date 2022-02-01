n=int(input("Enter a number:"))
a=0
b=n
while n:
    a*=10
    a+=n%10
    n//=10
if b==a:
    print("palindrom",b)
else:
    print("not palindrom",b)