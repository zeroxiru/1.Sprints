# def first_substring(user_word, user_character):
#     pass
#     start_index = user_word.find(user_character)
#     if start_index != -1 and start_index + 3 <= len(user_word):
#         return user_word[start_index:start_index + 3]
#     else:
#         return None
#
# print_substring = first_substring('Ibrahim', 'r')
# print(print_substring)
#
# def first_sub_word(word, user_character):
#     index_character = word.find(user_character)
#     print(index_character)
#     if index_character != -1 and index_character + 3 <= len(word):
#         return word[index_character: index_character + 3]
#     else:
#         return None




def first_sub_word(word, character):
    given_user_character_index = word.find(character)
    if given_user_character_index != -1 and given_user_character_index + 3 <= len(word):
        return word[given_user_character_index: given_user_character_index + 3]
    else:
        return None




