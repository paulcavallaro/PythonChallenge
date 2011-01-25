#!/usr/bin/python

import urllib2
import re

def run() :
    html_file = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
    html = html_file.read()
    html.replace('\n','')
    regex = re.compile('[a-z][A-Z]{3}(?P<letter>[a-z])[A-Z]{3}[a-z]')
    match = regex.findall(html)
    string = ''
    for item in match :
        string += item
    print string
            

if __name__ == '__main__' :
    run()
