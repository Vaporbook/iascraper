import fileinput
import requests
import os
import sys
import math

# for large file downloads with stream=True
from contextlib import closing

# download a single url and save file to disk


class MyDownloader():

    chunk_evt_handler = False

    def set_chunk_evt(self,h):
        self.chunk_evt_handler = h

    def save(self, url):

        with closing(requests.get(url, stream=True)) as r:

            print r.headers['content-length'], ' bytes'

            #set chunk size
            chunk_size = 12288

            # round up for num chunks indicator
            chunks = int(math.ceil(int(r.headers['content-length'])/chunk_size))
            print 'Will dowload ',chunks,' chunks'

            # get local filename to save to
            filename = os.path.basename(r.url)

            chunknum = 0

            if os.path.isfile(filename):
                print "File already exists locally!"
                return

            #stream it into the local file with progress chunknum
            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size):
                    chunknum += 1
                    self.chunk_evt_handler(r.url, chunknum, chunks)
                    fd.write(chunk)



