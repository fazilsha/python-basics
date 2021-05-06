'''
try writing your own print/sum/range
name 'em differently like print_ so they don't cause conflict with the built-in versions
'''

def print_me(*words):
    for w in words:
        print(w,end=" -- ")
print_me("Hello","from","Fazil")

def sum_me(*numbers):
    sum_total = 0
    for num in numbers:
        sum_total+=num
    print(sum_total)
sum_me(1,2,90)
def range_me(start,end,skip=0):
    temp = start
    while temp!=end:
        if skip == 0:
            print(temp,end=" ")
            temp += 1
        else:
            print(temp,end=" ")
            temp += skip
range_me(0,40,4)

'''
print_me("Hello","from","Fazil")
$ python extramile.py
Hello -- from -- Fazil --

sum_me(1,2,90)
$ python extramile.py
93

range_me(1,5)
$ python extramile.py
1 2 3 4

range_me(0,40,4)
$ python extramile.py
0 4 8 12 16 20 24 28 32 36

range_me(1,40,4)

It gives infinte loop when starting with number other than 0...
create issue and help to improve code

'''