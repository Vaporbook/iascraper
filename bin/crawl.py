import fileinput
import requests
import time
import curses
import sys, math
import pylibs.pycurses_widgets

from MyHTMLParser import MyHTMLParser

niceInterval = 1

detailparser = MyHTMLParser()

#stdscr = curses.initscr()

def on_pdf(url):
    print url
    sys.stdout.flush()

def loopit():

    for line in fileinput.input():
        #print 'Retrieving link list for detail page...',line
        r = requests.get(line.rstrip())
        detailparser.feed(r.text)
        time.sleep(niceInterval)

detailparser.set_pdf_handler(on_pdf)
loopit()
#curses.wrapper(loopit)



#pdfs = detailparser.get_links()

#for link in pdfs:

#    print link


