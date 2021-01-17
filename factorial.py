n1=int(input("Enter the num to factorial it :"))
x= lambda n:[1,0][n>1] or x(n-1)*n
print(x(n1))
