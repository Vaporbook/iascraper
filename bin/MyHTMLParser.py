from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

    initemttl = False
    inlink = False
    divdepth = 0
    lastpdf = '-'
    pdfs = set([])
    details = set([])
    
    def fire_pdf_evt(self,url):
        return url

    def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag
        if tag == 'div':
            #print 'link!'
            self.divdepth += 1
            for attr in attrs:
                if attr[0] == 'class':
                    if 'item-ttl' in attr[1]:
                        #print 'In item-ttl'
                        self.initemttl = True
                        self.initemttldepth = self.divdepth
        if tag == 'a':

            for attr in attrs:
                if attr[0] == 'href':
                    if '.pdf' in attr[1].lower():
                        link = 'https://archive.org'+attr[1]
                        self.lastpdf = link
                        if(not link in self.pdfs):
                            self.fire_pdf_evt(link)
                        self.pdfs.add(link)
                        

            if self.initemttl == True:
                self.inlink = True
                for attr in attrs:
                    if attr[0] == 'href':
                        #print 'https://archive.org'+attr[1]
                        self.details.add('https://archive.org'+attr[1])

            self.inlink = True
    def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
        if tag == 'a':
            if self.initemttl == True:
                self.inlink = False
        if tag == 'div':
            self.divdepth -= 1
            if self.initemttl:
                if self.divdepth == self.initemttldepth:
                    self.initemttl = False
                    #print 'Out of item-ttl'
            #print 'end link!'

    def handle_data(self, data):
        return

    def get_lastpdf(self):
        return self.lastpdf

    def get_links(self):
        return self.pdfs

    def get_details(self):
        return self.details

    def get_numpdfs(self):
        return len(self.pdfs)

    def get_numdetails(self):
        return len(self.details)

    def set_pdf_handler(self, fn):
        self.fire_pdf_evt = fn
        