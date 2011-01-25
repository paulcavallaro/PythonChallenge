#!/usr/bin/python

def run() :
    myfile = open("ocr.txt")
    table = dict()
    for line in myfile :
        for letter in line :
            if letter in table :
                table[letter] += 1
            else :
                table[letter] = 1

    for key in table :
        if table[key] < 15:
            print key

    myfile.close()
    myfile = open("ocr.txt")
    string = ''
    for line in myfile :
        for letter in line :
            if table[letter] < 15 :
                string += letter

    print string
        


if __name__ == '__main__' :
    run()
