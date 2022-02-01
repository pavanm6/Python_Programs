#max and second Max

max=0
smax=0
for i in range(6):
    num=int(input("Enter number:"))
    if max<num:
        smax=max                               
        max=num
    elif smax<num:
        smax=num
print("Max value: ",max)
print("Second Max value: ",smax) 