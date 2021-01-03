#tuples
#syntax: enclosed with parantheses ( )
#tuples are immutable
#we can read but we can't modify
t1 = (1,2,3,"a")
print("Tuples")
print(t1)
print(t1[1])


print("sets")
#sets
#syntax: enclosed with curly braces { }
s1 = { 1,32,2,3,4,2,1,1 } 
#It removes duplicate in action

print(s1)
#the position is unordered
print("After adding 90")
s1.add(90)
#if we do  add existing values in set, it considered as duplicates
#print the unique
print(s1)
