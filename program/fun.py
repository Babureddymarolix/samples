num1=10
num2=20
print("the value of num1 beforeswapping:",num1)
print("the value of num2 before swapping:",num2)
temp=num1
num1=num2
num2=temp

num=5
count=0
if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
if count==2:
    print(" number is prime")
else:
    print(" number is not prime")



factorial=1
num=6
if num<0:
    print("factorial doesnot exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial=factorial*i
        print("the factorial of ",num,"is",factorial)




num1=0
num2=1
print(num1)
print(num2)
for i in range(2,13):
    sum=num1+num2
    print(sum)
    num1=num2 
    num2=sum

arr=[1,2,3,4,5]
print(sum)
print(arr)




 
 