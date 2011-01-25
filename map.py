import string

def decode(word, shift):
    lookup = string.ascii_letters[:26]
    for letter in word :
        if lookup.find(letter) != -1 :
            letter = lookup[(lookup.find(letter) + shift) % 26]
        print letter,
