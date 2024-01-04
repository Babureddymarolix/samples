a=[1,2,3,41,1,2,1,1,1]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
    print(count)


a=[10,20,102,10,10,101,10,20,10,102,20]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
    print(dup_items) 


l=[1,2,3,4,5,3]
print(l.pop())
print(l)         



list[1,2,3,4,5,6,7,1,2,3]
result=[1,2,3,4,5]
for i in list:
    if i not in result:
        result.append(i)
    print(result)

