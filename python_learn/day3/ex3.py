'''
Implement FizzBuzz (look it up if you're not familiar with it) in Python
'''
fizzbuzz=int(input("Enter the number to check FizzBuzz: "))
if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("fizzbuzz")
elif fizzbuzz % 3 == 0:
    print("fizz")
elif fizzbuzz % 5 == 0:
    print("buzz")
print(fizzbuzz)

'''
Enter the number to check FizzBuzz: 15                        fizzbuzz
15
Enter the number to check FizzBuzz: 5                         buzz
5                                                           
Enter the number to check FizzBuzz: 17                        17

'''
