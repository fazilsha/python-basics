'''
Loop over a dict and print the value and key in the format value belongs to key.
'''

my_dict = {"Name": "Mr.Robot","City":"New York","Age":23}

for key,value in my_dict.items():
    print(f"{value} belongs to the key: {key}")

'''
u0_a184@localhost  ~/python-basics/python_learn/day3   main ±  python ex5.py   

Mr.Robot belongs to the key: Name                             New York belongs to the key: City
23 belongs to the key: Age

'''
