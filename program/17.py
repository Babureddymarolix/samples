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


names=("praveen","ravi","babu","sai")
(empid1,empid2,empid3,empid4)=names
print(empid1)


names=("praveen","ravi","babu","sai")
(empid1,empid2,empid3,empid4)=names
print(empid1)
print(empid2)

names=("praveen","ravi","babu","sai")
(empid1,empid2,empid3,empid4)=names
print(empid1)
print(empid2)
print(empid3)
print(empid4)