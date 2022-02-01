#WAP to accept basic salary and find gross salary
#gross_salary = basic +HRA+DA
#DA is 80% on basic
#HRA is 76% on basic


basic = int(input("Enter salary"))
da=(80/100)*basic
hra=(76/100)*basic
gross=hra+da+basic
print("gross salary:", gross)