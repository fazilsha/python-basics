input_text = input("Enter the text to encode: ")
main_list= [i for i in input_text]
char_list=[]
ch=[]
for x in main_list:
    c=input_text.count(x)
    if x not in ch:
        ch.append(x)
        char_list.append(f'{c}{x}')
print(f"Encoded text: {''.join(char_list)}")

