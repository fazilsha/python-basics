'''
Guessing Game. Accept a guess number and tell us if it's higher or less than the hardcoded number
'''

hd_num = 10

user_num = int(input("Guess the number: "))

if user_num > hd_num:
    print(f"Your number is higher {hd_num}")
else:
    print(f"Your number is lower than {hd_num}")

'''

u0_a184@localhost  ~/python-basics/python_learn/day3   main ±  python ex4.py
Guess the number: 2
Your number is lower than 10

'''
