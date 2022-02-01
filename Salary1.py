#10. WAP to accept basic salary and find gross salary.
 # Gross_salary= basic+HRA+DA
  #  if basic salary <10000
   #       DA is 70% on basic
    #      HRA is 65% on basic 
   #basic salary is between 10000 to 20000
    #     DA is 75% on basic
     #    HRA is 73% on basic
  # basic salary above 20000
   #      DA is 80% on basic
    #      HRA is 76% on basic

sal=int(input("Enter the number:"))

if (basic<=10000 and basic>0):
    da=(70/100)*basic
    hra=(65/100)*basic
    gross=basic+hra+da
    print("Enter a gross salary",gross)
elif (basic>=10000 and basic<=20000):
    da=(70/100)*basic
    hra=(75/100)*basic
    gross=basic+hra+da
    print("Enter a gross salary",gross)
else:
    da=(80/100)*basic
    hra=(76/100)*basic
    gross=basic+hra+da
    print("Enter a gross salary",gross)