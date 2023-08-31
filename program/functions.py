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
print(unique_list)
        
