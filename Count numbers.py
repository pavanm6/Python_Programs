#WAP to count of occurence of search elemnet.
num=int(input("Enter the number:"))
list=[24,45,55,65,55]
count=0
for i in list:
    if num==i:
        count=count+1
if count!=0:

    print(count)
else:
    print("NO")