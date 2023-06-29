def decrypt():
    with open("Encrypt.txt", encoding="utf8") as file:
        text = file.read()
    with open("Dictionary.txt", "r", encoding="utf8") as file:
        words = file.read()
    text = text.split()
    words = words.split()
    with open("Decrypt.txt", "w", encoding="utf8") as file:
        for word in text:
            i = str(word)
            i = int(i, 36)
            cipher = words[i]
            file.write(cipher + " ")


if __name__ == "__main__":
    decrypt()
