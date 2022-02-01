#WAP to accept 3 subjects marks and print total marks and avg marks

a = int(input("Enter first subject marks"))
b = int(input("Enter second subject marks"))
c = int(input("Enter third subject marks"))

total=a+b+c
average= total//3

print("Total marks :",total)
print("Average marks :",average)