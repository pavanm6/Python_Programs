#largest word  in given string
str=input("Enter string :") 
words=str.split(" ")
max=0
result=''
for word in words:
    if max<len(word):
        max=len(word)
        result=word
print(result)