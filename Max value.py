#print("Maximum of 4,12,43.3,19 and 100 is : ",end="")
#print (max( 4,12,43.3,19,100 ) )

set ={10,76,84,98,74,32,56}
s=list(set)
max=0
min=s[0]
for  i in s:
    if i>max:
        max=i
        print(max)