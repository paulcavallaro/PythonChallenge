#!/usr/bin/python
import urllib2
import re

def run() :
    number = str(46059)
    html_file = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + number)
    html = html_file.read()
    regex = re.compile('next nothing is (?P<number>\d+)')
    match = regex.search(html)
    while match != None :
        last_number = number
        number = match.group('number')
        try :
            html_file = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + number)
        except Exception as e :
            break
        html = html_file.read()
        match = regex.search(html)
        print number
    print last_number
    print number
        


if __name__ == '__main__' :
    run()
