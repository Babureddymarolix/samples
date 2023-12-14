a=[1,2,3,5,6,7,8,2]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
    print(count)



a=[10,20,30,40,20,30,20,101,20,20,20,10]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
    print(dup_items)



l=[1,2,3,4,5,6,4]
print(l.pop())
print(l)




list=[1,2,3,4,5,7,1,2,3,4,5,5]
result=[1,2,3,4,5,7]
for i in list:
    if i not in result:
        result.append(i)
    print(result)