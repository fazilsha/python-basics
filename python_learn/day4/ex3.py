'''
write a product function that produces product of its args.
It should accept any number of args
get_product(1, 2, 3) outputs 6
get_product(5, 20) outputs 25
get_product() outputs 1
'''

def get_product(*N):
    mul = 1
    for num in N:
        mul *= num
    print(mul)
get_product()

'''
$ python ex3.py
6

$ python ex3.py
100

$ python ex3.py
1

'''
