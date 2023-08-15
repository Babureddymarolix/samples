l1=[1,2,3]
l2=[4,5,6]
l1=l1+l2
print(l1)


lst=[5,10,15,20]
print(sum(lst))


num=[2,3,4,5,6,66,77,88,99,54,65,34,43]
for i in num:
    if i%2==0:
        print(i)

lst=[2,3,5,8,9,7,10,32,23,39,55,42]
for i in lst:
    if i%2!=0:
        print(i)


workdays=["monday","tuesday","wednesday","friday","saturday"]
workdays.remove("saturday")
print(workdays) 



l=[1,2,3,4,5,6]
print(l.pop())
print(l)


mylist=["tamota","apple","orange","lemon"]
print(mylist)
mylist.insert(3,"guava")
print("updated list=\n",mylist)


if __name__ == '__main__':

	l = ['A', 'B', 'C']
	x = 'D'

	l.insert(len(l), x)
	print(l)  


