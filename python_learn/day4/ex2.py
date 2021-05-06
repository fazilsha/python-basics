'''
 write a function that accepts N and prints 5 multiples of N
 get_multiple(5) should print 5 10 15 20 25. you'll have to work with range and
 a bit of custom logic to figure out the stop value.
 In case of get_multiples(3), output should be 3 6 9 12 15.
 N can be any positive int. not just 3 or 5.
'''

def get_multiples(N,multiple):
    for num in range(0,N,multiple):
        if num != 0:
            print(num,end=" ")
get_multiples(100,10)

'''
Multiples of 5
$ python ex2.py
5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95

Multiples of 6
$ python ex2.py
6 12 18 24 30 36 42 48 54 60 66 72 78 84 90 96

Multiples of 11
$ python ex2.py
11 22 33 44 55 66 77 88 99

Multiples of 10
$ python ex2.py
10 20 30 40 50 60 70 80 90

'''
