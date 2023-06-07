def get_file(file_name):
    f = open(file_name, "r", encoding="utf-8")
    words = f.readlines()
    f.close()

    for i in range(len(words)):
        words[i] = words[i].replace("\n", "")

    return words


def search_near_words(word_list, word_to_search):
    word_to_search = word_to_search.lower()
    word_bank_0, word_bank_1, word_bank_2, word_bank_3 = [], [], [], []

    for word in word_list:

        count = sum(1 for a, b in zip(word, word_to_search) if a != b)
        len_diff = abs(len(word) - len(word_to_search))
        total = count + len_diff

        match total:
            case 0:
                word_bank_0.append(word)
            case 1:
                word_bank_1.append(word)
            case 2:
                word_bank_2.append(word)
            case 3:
                word_bank_3.append(word)
            case _:
                continue

    return word_bank_0, word_bank_1, word_bank_2, word_bank_3


if __name__ == '__main__':

    mot = "boa"
    liste = get_file("gutenberg.txt")
    liste0, liste1, liste2, liste3 = search_near_words(liste, mot)

    print("Existe ? : ", liste0 != [])
    print("Différence de 1 :", liste1)
    print("Différence de 2 :", liste2)
    print("Différence de 3 :", liste3)
