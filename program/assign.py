python=["Babu","nani","hemanth","chaitu"]
print(python.remove("hemanth"))
print(python)



s=input("enter palindrome:")
if(s==s[::-1]):
    print("it is palindrome")
else:
    print("it is not a palindrome") 
    


s=input("enter single alphabet:")
if s in("a","e","i","o","u","A","E","I","O","U"):
    print("the entered alphabet is vowel")
else:
    print("the entered alphabet is consonent")


s="we love ms"
s2=s.replace("","dhoni")  
print(s2)      



s="aabbcc112233**"
digitc=0
alphac=0
speciac=0
for i in s:
    if i.isdigit():
        digitc=digitc+1
    elif i.isalpha():
        alphac=alphac+1
    else:
        specialc=alphac+1
print("number of special",specialc)
print("number of digit",digitc) 
print("number of alpha",alphac)  




s=input("enter string:")
s2=s.replace("","")
print(s2)


str=input("enter a string:")
sum=0
for i in str:
  if i.isdigit():
    sum=sum+int(i)
print("sum=",sum)  


s=["babu","nani","chaitu","chaitu","hemmanth"]
s=list(dict.fromkeys(s))
print(s)


string="i love india"
s=string.count("i")
print(s)





