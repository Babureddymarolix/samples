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
