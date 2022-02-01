#WAP to find number of even digits and number of odd digits
# By using list
list1 = [10, 21, 4, 45, 66, 93, 11]
#list = input("Enter a list :")
even_count, odd_count = 0, 0
num = 0
while(num < len(list1)):
	if list1[num] % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	num += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


#By using looping Statements

'''print("Enter the number:")
num=int(input())
odd=0
even=0
while(num!=0):
    rem=num%10
    if(rem%2==1):
        odd+=1
    else:
        even+=1
    num//=10
print("Number of even digits = ",even)
print("Number of odd digits = ",odd) '''