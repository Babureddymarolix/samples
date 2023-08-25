dict={0:10,1:20}
print(dict)
dict.update({2:30})
print(dict)

d={}
for k in range(0,5):
    key=input("enter keys")
    value=input("enter values")
    d[key]=value
    print(d)


d1=dict()
for x in range(1,16):
 d1[x]=x**2
 print(d1)   
     
dict={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
   if x in d:
      print("key is present in the dictionary")
   else:
      print("key is not present in the dictionary ")
      is_key_present(5)
      is_key_present(9)    
     

dic1={'data1':10,'data2':20,'data3':30}
print(sum(dic1.values()))     

dic1={'data1':10,'data2':20,'data3':30}
sum=0
for i in dic1.values():
   sum=sum+i
   print(sum)
   print()


   d={}
   for k in range(0,5):
      key=input("enter keys:")
      value=input("enter values:")
      d[key]=value
      print(d)
      remove_key=input("enetr removed key")
      d.pop(remove_key)
      print(d)


d1={'a':100,'b':200}
d2={'x':300,'y':200}
d=d1.copy()
d.update(d2)
print(d)      
   