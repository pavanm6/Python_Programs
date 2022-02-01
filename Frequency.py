#WAP to print frequency of each elemen in a given list
# list=[23,45,65,90,45,23]
#o/p:   #23 frequency is : 2
        #45 frequency is : 2
        #65 frequency is : 1
        #90 frequency is : 1

count=1
list=[23,45,45,23,23,45,65,90,45,23]
for i in range(len(list)):
        for j in range (i+1,len(list)):
                if list[i]==list[j]:
                        list[j]=None
                        count=count+1
        if list[i]!=None:
                print(list[i]," :",count)
        count        
