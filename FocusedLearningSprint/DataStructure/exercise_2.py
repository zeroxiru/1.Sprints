

def reverse_string_by_stack( string_input):
    char_items =[]

    for character in string_input:
        char_items.append(character)

    reverse_string = ""
    while char_items:
        reverse_string +=char_items.pop()
    return  reverse_string

input_string = " I am a Programmer"
reversed = reverse_string_by_stack(input_string)
print(input_string)
print(reversed)



