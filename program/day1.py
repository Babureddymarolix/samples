str="reverse me"
print(str)
print(str[::-1])



s=input("enter palindrome:")
if (s==s[::-1]):
    print("yes it is palindrome")
else:
    print("no it is not palindrome")    



def remove_vowels(string):
    vowels="aeiouAEIOU"
    result=""

    for char in string:
        if char not in vowels:
         result+=char
    return result
print(remove_vowels("hello world"))




mylist=["1","2","3","4","1","1"]
s=list(dict.fromkeys(mylist))
print(s)



colour=["red","black","green","white","blue","red"]
colour.pop(5)
print(colour)