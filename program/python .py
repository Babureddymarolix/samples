arr=[1,2,3,4,5]
print(sum(arr))   


arr=[1,2,3,4,5]
max=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)        


arr=[1,2,3,4,5]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>min:
        min=arr[i]
print(min)





mylist=[1,23,5,6,77,7]
print(mylist)
print("length of list using len()method is:",len(mylist))


mylistlist=[3,545,65,67]
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print("list after swapping:",mylist)