'''
else
write a loop with an else clause being invoked
now modify the program so the else clause doesn't run
'''

#numbers = [2,4,6,8,10] #only even it invokes else clause
numbers = [1,3,5,7] # only odd it invokes in for loops
for num in numbers:
    if num%2 != 0:
        print("Odd number is {}".format(num))
else:
    print("Sorry! All the numbers are Even")
