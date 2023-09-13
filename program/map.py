def addition(x):
    return x+x
l=(1,2,3,4,5)
output = list(map(addition,l))
print(output)


l1=[1,2,3,4,5]
result=list(map(lambda x:x+x,l1))
print(result)

l1=["1","2","3","4","5"]
print(type(l1[0]))
result=list(map(int,l))
print(result)


def outerfunction():
    def innerfunction():
        print("this is inner function")
    innerfunction()
    print("this is outerfunction")
outerfunction()    