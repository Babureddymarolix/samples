num1=10
num2=20
print("value of num1 before swapping:",num1)
print("value of num2 before swapping:",num2)
temp=num1
num1=num2
num2=temp
print("value of num1 after swapping:",num1)
print("value of num2 after swapping:",num2)



num=5
count=0
if num>1:
    for i in range (1,num+1):
        if(num%i) ==0:
         count=count+1
    if count==2:
        print("number is prime")
    else:
        print("number is not prime")