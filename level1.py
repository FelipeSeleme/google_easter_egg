# level 1 solution (see level1.md file for details)
def solution(encrypted_msg):
    # defines a variable for the solution
    decrypted = ""
    # create a list with the letters of the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # reverses the position of the letters in the alphabet list and assigns the values to a new list
    inverted = alphabet[::-1]
    # cycles through the letters of the encrypted message
    for character in encrypted_msg:
        # if the letter is lower case, find the match in the inverted alphabet list
        if character.islower():
            decrypted += inverted[alphabet.index(character)]
        else:
            decrypted += character
    return decrypted
