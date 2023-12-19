a=[1,2,3,3,3]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
    print(count)

a=[10,20,29,20,20,30,20]
dup_items=set()
uniq_items=[]
for i in a:
    if i not in dup_items:
        uniq_items.append(i)
        dup_items.add(i)
    print(dup_items)



lst=[1,2,3,4,5,5]
print(lst.pop())
print(lst)



lst=[1,2,3,4,5,6,1,2,3,3]
result=[1,2,3,4,5]
for i in lst:
    if i not in result:
        result.append(i)
    print(result)



