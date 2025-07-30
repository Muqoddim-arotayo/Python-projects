print('Word Inverter')
user_input = input('Input the sentence you want to invert >>> ').lower().strip()
inverted_input = user_input[::-1]
print(inverted_input)
if user_input == inverted_input:
    print('The word is a palendrom')
else :
    print('The word is not a palendrom')