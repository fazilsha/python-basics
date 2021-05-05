'''

Given a dictionary {"name": "python", "ext": "py", "creator": "guido"}, print both keys and values.
'''
prog = {"name": "python", "ext": "py", "creator": "guido"}

for k,v in prog.items():
    print(f'{k} : {v}')

'''
$ py ex2.py
name : python
ext : py
creator : guido

'''