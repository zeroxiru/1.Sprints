from romeo_and_juliet import PLAY

def get_words(text):
    print("List of total words in the Romeo and Juliet play")
    words = text.split()
    return words

def words_frequency(words):
    print("List of total frequency words in the Romeo and Juliet play")
    frequency_of_words = {}
    for word in words:
        frequency_of_words[word] = frequency_of_words.get(word, 0) + 1
    frequency_of_words = dict(sorted(frequency_of_words.items(), key=lambda value: value[1], reverse=True))
    return frequency_of_words

def top_n_words(freq, n):
    print("List of top 50 number of words in the Romeo and Juliet play")
    for word, number in freq.items():
        if n == 0:
            break
        else:
            print(word, number)
            n -= 1

def main():
    play_text = PLAY
    word_list = get_words(play_text)
    print(word_list)
    frequency_of_words = words_frequency(word_list)
    print(frequency_of_words)
    print(top_n_words(frequency_of_words, 50))

if __name__ == "__main__":
    main()