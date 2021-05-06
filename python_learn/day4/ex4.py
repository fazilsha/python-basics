'''
write an add function that returns some of two numbers.
Accept an optional third parameter that can make it print the output too.
add(2, 3) should return 5
add(2, 3, True) should print 5 to the screen and return 5
'''

def add(a,b,indicator=False):
    if indicator:
        print(f'From print function: {a+b}')
        return f'From return: {a+b}'
    else:
        return f'From default: {a + b}'
print(add(2,3,True))

'''
add(2, 3)
$ python ex4.py
From default: 5

add(2, 3, True)
$ python ex4.py
From print function: 5
From return: 5

'''