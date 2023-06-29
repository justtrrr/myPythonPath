def rle_encode(data):
    encode = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encode += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encode += str(count) + prev_char
    return encode


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


if __name__ == "__main__":
    print(rle_encode(input("Введите строку: ")))
    print(rle_decode(input("Введите строку: ")))
