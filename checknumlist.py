list1=[]
list1=[int(item) for item in input("Enter the list:").split()]

num=int(input("Enter the num to check in list:"))
if num in list1:
    print("List:",list1)
    print("Number found at index: ",list1.index(num))
else:
    print("Number not found in your list")
