# grab links from html stdin input and canonicalize them
# spit them out on newlines for processing

from MyHTMLParser import MyHTMLParser
import fileinput
import sys
import argparse

argparser = argparse.ArgumentParser(description='Parse an html dump of an IA page for matching links')
#argparser.add_argument('--path', dest='path',
#                   default='/',
#                   help='path to match in links')

args = argparser.parse_args()

parser = MyHTMLParser()
html = sys.stdin.read()
parser.feed(html)
for link in parser.get_details():
	print link