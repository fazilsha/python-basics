a=[1,2,3,4,5]
for i in a:
    print(i)
print(type(a))

#append
a.append(6)
print(a)
#updating
print("updating 0 at 0th index")
a[0]=0
print(a)
print("Removing element at 2nd index")
a.remove(a[2])
print(a)
