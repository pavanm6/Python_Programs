count=10
count1=90
for i in range(5):
    for j in range(5):
        if i%2==0:
            print(count,end=" ")
            count=count+1
        else:
            print(count1,end=" ")
            count1=count1-1
    print()        
