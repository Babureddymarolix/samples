t1=["marolix","tcs","techm"]
t2=("amazon","infosys")
t1+=t2
print(t1)



mytuple=(1,2,3,4,5,6)
mylist=[7,8]
addlist=list(mytuple)
addlist+=mylist
print(addlist)


mytuple=(1,2,3,4,5,6)
mylist=[7,8]
addlist=list(mytuple)
addlist+=mylist
print(addlist)
mytuple=tuple(addlist)
print(mytuple)


l=[x for x in range(1,10)]
print(l)


l=[x for x in range(1,10)]
print(l)
print(type(l))

t=(x for x in range(10,20))
print(t)
for x in t:
    print(x,end=" ")


names =["praveen","ravi","babu","sai"]
(python,*java)=names
print(python)
print(java)  