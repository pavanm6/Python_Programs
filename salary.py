#3.  WAP to accept salary and 3 shopping bills from user and find 
 #  1. total shopping amount
  # 2. find how much % of amount he/she spent on shopping on his salary.


sal=int(input("Enter salarya amount:"))
s1=int(input("Enter shopping bill:"))
s2=int(input("Enter shopping bill:"))
s3=int(input("Enter shopping bill:"))

total=s1+s2+s3
percentage=(total/3)*100
print("Total amount",total)
print("percentage:",percentage)