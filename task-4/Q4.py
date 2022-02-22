#a pallindrome is a word which is same when read from the left side and also right side 
#takes the number as input from the user
n=int(input("enter the number: "))

#assigns the variable rem and reversed no. value as 0
#stores the number input by the user in variable original_number 
rem=0
original_number= n
reversed_number=0

#the while loop will extract the indivisual digit and find the reversed number
# the while loop will run till the number is greater than 0
while(n>0):
    rem=n%10
    reversed_number= (reversed_number*10)+ rem
    n=n//10

# checks if the original number and reversed number are equal 
if(original_number==reversed_number):
    print("true")
else:
    print("false")

