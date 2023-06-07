def get_file(file_name):
    f = open(file_name, "r", encoding="utf-8")
    words = f.readlines()
    f.close()

    for i in range(len(words)):
        words[i] = words[i].replace("\n", "")

    return words


def search_near_words(word_list, word_to_search):
    word_to_search = word_to_search.lower()
    dictionary = dict()

    words = []

    biggest = 0

    for word in word_list:

        count = sum(1 for a, b in zip(word, word_to_search) if a != b)
        len_diff = abs(len(word) - len(word_to_search))
        total = count + len_diff

        if biggest < total:
            biggest = total

        dictionary[word] = total

    for i in range(biggest + 1):
        words.append([])

    for word in dictionary:
        words[dictionary[word]].append(word)

    return words


if __name__ == '__main__':

    mot = "antidote"
    liste = get_file("gutenberg.txt")
    NearWords = search_near_words(liste, mot)

    print("Existe ? :", len(NearWords[0]) > 0)
    print("Différence de 1 :", NearWords[1])
    print("Difference de 2 :", NearWords[2])
    print("Différence de 3 :", NearWords[3])
    print("Différence de", len(NearWords) - 1, ":", NearWords[len(NearWords) - 1])
