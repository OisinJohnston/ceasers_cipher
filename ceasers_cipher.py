#!/usr/bin/env python3
import string

alphabet = list(string.ascii_letters)

def encode(data, key):
    resp = ''
    key %= 52
    for i in list(data):
        if i not in alphabet:
            resp += i
            continue
        index = alphabet.index(i)
        index += key
        if index >= 52:
            index -= 52
        resp += alphabet[index]
    return resp
        


def choice(message, options):
    resp = input(message).lower()
    if resp not in options:
        raise Exception(f"Invalid response : {resp} was not one of {options}")
    return resp
        



def main():
    message_type = choice("do you wish too read from a file (F) or enter the message directly (D)? F/D ", ('f', 'd'))
    data = ''
    if message_type == 'd':
        data = input("Enter the data you wish too parse: ")
    else:
        fp = input("Enter the file path you wish too read from: ")
        with open(fp, 'r') as f:
            data = f.read()
    try:
        offset = int(input("Enter the key to use for the cipher: "))
    except ValueError:
        print("you entered an invalid integer, exiting...")
        return

    if choice("Do you wish to encode (E) or decode (D)? E/D ", ('e','d')) == 'd':
        offset *= -1
    
    output_type = choice("do you wish too write too a file (F) or write too stdout (S)? F/S ", ('f','s'))
    output = encode(data, offset)
    if output_type == 'f':
        fp = input('enter the file path you wish too write too: ')
        with open(fp, 'w') as f:
            f.write(output)
    else:
        print(output)

if __name__ == "__main__":
    main()

