num1=10
num2=20
print("the value of num1 beforeswapping:",num1)
print("the value of num2 before swapping:",num2)
temp=num1
num1=num2
num2=temp



num=6
count=0
if num>1:
    for i in range (1,num+1):
        if (num%i)==0:
           count=count+1
if count==2:
    print("number is prime")
else:
    print("number is not prime")







 
 