def count_upper_lower(string1):
    uppercount=0
    lower_count=0
    for char in string1:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
temp=input("enter the string:") 
count_upper_lower(temp)       


list=[1,2,3,5,3,3,3,4,5,56,6,7,7,7,8]
unique_list=[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)



def check(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        str=input("enter the sentence")
        if(check(str)==true):
            print("the entered  sentence is pangram")
        else:
            print("the entered sentence is not pargram")  



def values():
    l=list()
    for i in range(1,10):
        l.append(i**2)
        print(l)
        values()  

numbers=[8,2,3,0,7]
def sum(numbers):
    total=0
    for x in numbers:
        total +=x
        return total
    print(sum(numbers))                       