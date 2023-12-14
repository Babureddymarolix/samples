def remove_vowels(string):
    vowels="aeiouAEIOU"
    result=""
    for char in string:
      if char not in vowels:
        result +=char
    return result
print(remove_vowels("hello world"))




lst=["red","black","green","yellow","blue"]
lst.pop(4)
print(lst)


mylst={"1","1","2","2","3","4","5","1"}
s=lst(dict.fromkeys(mylst))
print(s)