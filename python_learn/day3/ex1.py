'''
Given a list of names, try printing unique names that are less than 5 character length and do not contain the character 'e'.
names = ["john", "jake", "jack", "george", "jenny", "jason"]
'''
names = ["john", "jake", "jack", "george", "jenny", "jason"]

for name in names:
    if len(name) < 5 and "e" in name:
        print(name)

'''
$ py ex1.py
jake

'''