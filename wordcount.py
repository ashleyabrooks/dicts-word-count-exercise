import string


def word_counter(file_name):
    lines = [line.rstrip() for line in open(file_name)]

    word_count = {}

    for line in lines:
        words = line.split()
        clean_words = [word.rstrip(string.punctuation).lower() for word in words]

        for word in clean_words:
            word_count[word] = word_count.get(word, 0) + 1

    for key, value in word_count.items():
        print key, value

word_counter('test.txt')
