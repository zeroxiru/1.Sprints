from romeo_and_juliet import PLAY
#print(PLAY[:])

def get_words(text):
    print(" List of total words in the Romeo and Juliet play")
    words = text.split()
    return words

def words_frequency(words):
    frequency_of_words = {}
    for word in words:
      frequency_of_words[word] = frequency_of_words.get(word, 0) + 1
      frequency_of_words =dict(sorted(frequency_of_words.items(), key=lambda value: value[1], reverse=True))
    return frequency_of_words
def top_n_words(freq, n):

    for word, number in freq.items():
        #n -= 1
        if n == 0:
            break
        else:
            print(word, number)
            n -= 1

#word_list = get_words(PLAY)
#frequency_of_words = words_frequency(word_list)
#list_of_top_words = top_n_words(frequency_of_words, 10)

#
# for word, freq in frequency_of_words.items():
#     print(word, freq)
#print(get_words(PLAY))
#print(words_frequency(word_list))
#print(list_of_top_words)

def main():
   # print(" List of total words in the Romeo and Juliet play")
    word_list = get_words(PLAY)
    number_of_words_frequency = words_frequency()

print(get_words(PLAY))


if __name__ == "__main__":
    main()