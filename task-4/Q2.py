#takes the string as input
str= input("enter the string: ")
#calculates the length of the string
length= len(str)

#loop to print the elements at even position of the string 
for i in range (0,length,2):
    print(str[i], end=" ")
#end operator helps to print them in the same line 
