


# Internet Archive Scraper scripts

## rationale

This was an exercise in using Python to do something fun.

The goal was to have a simple Python CLI for scraping links and downloading media files from the IA site. IA does provide their own python libraries, but there are issues when using those for large downloads, and they are complex to debug. These are meant to be very simple one line scripts that can be incorporated into any other *nix-style CL workflow and easily modified or improved.

The main input to provide is an html file. I generally retrieve this manually by grabbing the source of any IA page with a list of links to media pages. The list should link to the detail page for each archive item in it, and those detail pages should contain the links to the final resources you want to download. My workflow is to browse to the collection I want to parse, load all the pages of links available by scrolling all the way to the bottom, then use Chrome inspector to grab the rendered HTML source (note: NOT the downloaded HTML source, but the modified DOM representation).

From there, the idea is to derive a list of URIs to media resources which can be downloaded automatically while I go drink some beer and watch movies.

The first input goes to the parse.py script, which will get the list of links to detail pages for the media resources. Then the second script, crawl.py, should be used to crawl each detail page URI in order to collect media URIs. The output of crawl.py can then be sent to download.py, which will sequentially download each media file. There is a *nice* factor to the crawl loop which can be adjusted to suit your needs.

I'm working getting a slicker usage of the curses libs for better script progress display.

I also need to learn more about how to properly structure a CLI python project. Ideally, I want the command scripts in the bin/ dir but the libraries in a lib/ dir.

## testing

`	cat samples/rainbow.html | python bin/parse.py | python bin/crawl.py
`	
`	--> This will output a list of URIs to PDF files of Byte magazine scans on archive.org.
