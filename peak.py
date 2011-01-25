#!/usr/bin/python
import pickle

def run() :
    string = ''
    obj = pickle.load(open('banner.p'))
    for lst in obj :
        for tpl in lst :
            string += tpl[0] * tpl[1]
    print string

if __name__ == '__main__' :
    run()
