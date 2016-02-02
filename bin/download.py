import fileinput
import requests
import time
import curses
import sys, math
import pylibs.pycurses_widgets

from MyDownloader import MyDownloader
from MyHTMLParser import MyHTMLParser

def loopit():

    for line in fileinput.input():

        dlit(line.rstrip())

def chunk_event():

    def chunkcounter(url, chunknum, chunks):
        #stdscr.addstr(1,1,' Downloading '+url+' ')
        #stdscr.addstr('['+str(chunknum)+'/'+str(chunks)+']', curses.A_REVERSE)
        #stdscr.refresh()
        #print chunknum % 100
        if(chunknum % 100 == 0):
            sys.stdout.write('|')
            sys.stdout.flush()

        if(chunknum % 10000 == 0):
            print '['+str(chunknum)+'/'+str(chunks)+']'
            sys.stdout.write('['+str(int((float(chunknum)/chunks)*100))+'%]')
            sys.stdout.flush()


    return chunkcounter


def dldone():
    print "\nDone"
    #stdscr.addstr("\n")
    #stdscr.refresh()

def dlit(link):
    if bool('_text.pdf' in link) == False:
        print 'Downloading '+link
        dl.save(link)
        try:
            dl.save(link)
        except E:
            print "Exception downloading that file..."
            print E
            pass

dl = MyDownloader()

dl.set_chunk_evt(chunk_event())

chunksdone = 0

loopit()
