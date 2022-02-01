# WAP to find number of letters in each word in a given sentence


str1=input("Please Enter a string :")
tot=1;
for i in range(len(str1)):
    if(str1[i]==' ' or str1 == '/n' or str1 == '\t'):
        tot=tot+1
print("Total number of words in the given string= ",tot)
