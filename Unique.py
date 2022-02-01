#WAP to print unique element in a given list
# list=[23,45,65,90,45,23]
#o/p: 65 90

count=1
list=[23,45,45,23,23,45,65,90,45,23]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            list[j]=None
            count=count+1
    if count==1 and list [i]!=None:
        print(list[i],end=" ")
    count=1    