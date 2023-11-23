a=[1,2,3,4,2,5]
count={} 

for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)



a=[10,202,202,202,20,10,23,23,44,55,66]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
    print(dup_items)



l=[1,2,3,4,5,6,1]
print(l.pop())
print(l)

list1=[1,2,3,4,5,6,6,7,8,8,9,1,2,3]
result=[1,2,3,4,]
for i in list1:
    if i not in result:
     result.append(i)
print(result)  



str=input("enter string")
vowel_string="aeiouAEIOU"
print("input string",str)
for char in str:
    if char in vowel_string:
        str=str.replace(char,"")
    print("output string without vowels",str)
    


class name(object):
    def delvowels(self,s):
        s=s.replace("a","")
        s=s.replace("e","")
        s=s.replace("i","")
        s=s.replace("o","")
        s=s.replace("u","")
        return s
clr=name()
print(clr.delvowels(input ("enter string:")))