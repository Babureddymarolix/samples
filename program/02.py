text = "i am the your the good"
print(len(text))
x =text.split("the")
print(x)
print(len(x))

s="marolix technology solutions"
splt =s.split()
for x in splt:
    print(x)

s="marolix technology solutions"
print(len(s))
splt =s.split()
print(len(splt))
for x in splt:
    print(x)

date="02-08-2023"
split =date.split(":")
for x in split:
    print(x)


lst=["babu","nani","hemanth"]
s = "+".join(lst) 
print(s)   

tpl=("me","you","we")
print(len(tpl))
s1 = "*".join(tpl)
print(len(s1))
print(s1)


s="learning python"
print(s.upper())

s="learning knowledge"
print(s.lower())

s="many things"
print(s.swapcase())

s2="marolix technology solutions"
print(s2.capitalize())



