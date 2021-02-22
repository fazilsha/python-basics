anagram_input=input("Enter the word to check anagram: ")
w1,w2=anagram_input.split()
l1=list(w1)
l2=list(w2)
l2.sort()
l1.sort()
print(l1,l2)
if l1 == l2:
    print("words are Anagram")
else:
    print("words are not anagram")
