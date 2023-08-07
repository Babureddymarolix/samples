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



s="aaabbbccc1112223333"
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
print("number of special characters",specialc)
print("number of digit",digitc) 
print("number of digit",alphac)               






