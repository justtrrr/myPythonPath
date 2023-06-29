def encrypt(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.lower()
    text = text.replace(",", " , ").replace(".", " . ").replace(" ” ", " ' ").replace("—", " - ").replace \
        (".", " . ").replace("?", " ? ").replace("!", " ! ").replace("...", " ... ").replace(":", " : ").replace \
        ("'", " ' ").replace("...", " ... ").replace("„", " „ ").replace(";", " ; ").replace("-", " - ").replace \
        ("—", " — ").replace("…", " … ").replace("»", " » ").replace("«", " « ").replace("(", " ( ").replace \
        ("“", " “ ").replace(")", "  )  ").replace("”", " ” ").replace('"', ' " ').replace("’", " ’ ").replace \
        ("‘", " ‘ ")
    text = text.split()
    words_dictionary = dict()
    for word in text:
        count = words_dictionary.get(word, 0)
        words_dictionary[word] = count + 1
    words_dictionary = list(dict(sorted(words_dictionary.items(), key=lambda x: x[1])))
    list_length = len(words_dictionary)
    words_list = []
    i = 0
    with open("Dictionary.txt", "w", encoding="utf8") as file:
        while i < list_length:
            words_list.append(words_dictionary.pop())
            i += 1
        file.write(' '.join(words_list))
    cipher_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K',
                    21: 'L',
                    22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
                    33: 'X',
                    34: 'Y', 35: 'Z'}
    with open("Encrypt.txt", "w", encoding="utf8") as file:
        for word in text:
            cipher = words_list.index(word)
            result = ''
            if cipher == 0:
                result += cipher_table[0]
            else:
                while cipher != 0:
                    i = cipher % 36
                    cipher = cipher // 36
                    result += cipher_table[i]
            result = ''.join(reversed(result))
            file.write(result + " ")


if __name__ == "__main__":
    encrypt(input('Введите название файла: '))
