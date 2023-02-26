def solution(encrypted_msg):
    decrypted = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    inverted = alphabet[::-1]
    for character in encrypted_msg:
        if character.islower():
            decrypted += inverted[alphabet.index(character)]
        else:
            decrypted += character
    return decrypted
