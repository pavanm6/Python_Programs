# WAP to print duplicate elements in a given list
# list=[23,45,65,90,45,23]
#o/p: 23 45

num=[23,45,65,90,45,23,45,23]
count=1
print("Enter duplicate values:")
for i in range(6):
    for j in range(i+1,6):
        if num[i]==num[j]:
            num[j]=None
            count=count+1
    if count>1 and num!=None:
        print(num[i],end=" ")
    count=1
    
    
