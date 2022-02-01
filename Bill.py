#WAP to accept units from user and find the bill
# for first 50 units the charges are : 0.75p/u
#next 100 units the charge are : 2.10p/u
#next 100 units the charges are : 2.50p/u
#above 250 units the charge are:2.80p/u

units=int(input("Enter units"))
bill=0
if units<=50:
    bill=units*0.75;
elif units<=150:
    bill=(50*0.75)+(units-50)*2.50
elif units<=250:
    bill=(50*0.75)+(100*2.10)+(units-150)*2.50
else:
    bill=(50*0.75)+(100*2.10)+(100*2.50)+(units-250)*2.80
# adding 10% GST to bill
print("Bill :",bill)
gst=(bill*10)/100
bill=bill+gst
print("GST: ",gst)
print("final bill:",bill) 
