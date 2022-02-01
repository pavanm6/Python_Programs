#Wap to accepct project marks , internal marks and external marks and find total marks .
#total_marks=70% from project +20% from external +10% from internal

a = int(input("projectmarks"))
b = int(input("internalmarks"))
c = int(input("externalmarks"))

total=((70/100)*a+(20/100)*b+(10/100)*c)
print("Total marks:",total)