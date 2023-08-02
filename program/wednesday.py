s="i want learn python"
print(s.rfind("a"))

s="i love india"
print(s.rfind("e"))

s="mahendra sign dhoni"
print(s.lfind("o"))

s="mahendra shing dhoni"
print(s.rfind("n"))

s="we are all indians"
print(s.rfind("a"))

s="i want learn python"
print(s.rfind("a"))

s="abababababababababaabaaabbb"
print(s.count("a"))


s=input("main string:")
sub=input("sub string:")
if s.index(sub):
    print(sub,"is found")
 else:
    print(sub,"is not found")   


 a="babu"
 b="reddy"
print(a+b) 

a="babu"
print(a*4)



s=" learning python is very easy"
print[1:8:1]


my_dic={"name":"babu","empid":"01691","domine":"python"}
for item in my_dic.items():
   print(item)

num=int(input("enter num:"))
counter=0
while counter<=10:
   ansr=num*counter
print(num,"x","counter,"_",num)
      counter=counter      