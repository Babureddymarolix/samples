dict={0:10,1:20}
print(dict)
dict.update({2:30})
print(dict)

d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
  if x in d:
        print("key is present in the dictionary")
  else:
      print("key is not present in the dictionary")
      is_key_present(5)
      is_key_present(8)

     
      
     