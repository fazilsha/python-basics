'''
subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

'''
list1=[int(item) for item in input("First Array: ").split()]
list2=[int(item) for item in input("Second Array: ").split()]

l1,l2=list1,list2
for j in l2:
    if j in l1:
        c=l1.count(j)
        if c > 1:
          for i in l1:
             if i==j:
               l1.remove(j)
        l1.remove(j)
print(l1)
