import feedparser
from datetime import datetime
import time
import re
import textwrap

f = feedparser.parse('http://cepr.net/publications/reports/feed/rss')

feed_date = f.updated[:-13]

if feed_date == time.strftime('%a, %d %b %Y'):
    # grab pubDate
    pubDate = str(f.entries[0].published_parsed.tm_year) + "-" + str(f.entries[0].published_parsed.tm_mon)
    # grab title
    title = f.entries[0].title
    # grab author names
    authors = f.entries[0].author
    # find names between parentheses
    m = re.search('\(([^)]+)\)', authors)
    # remove 'and'
    authors_string = m.group(1).replace("and", "")
    # convert to list
    authors_list = authors_string.split(',')
    # abstract
    # NOTE THIS IS NOT PULLING THE ACTUAL DESCRIPTION - NEEDS WORK
    abstract = f.entries[0].description

    # use length of list to loop and create individual author-name entries

    # details
    entry_head = textwrap.dedent("""\
                Template-Type: ReDif-Paper 1.0
                Handle: RePEc:epo:papers:"""+pubDate)

# append details to file

with open(time.strftime("%Y") + "-test.rdf", "a") as repec_file:
     repec_file.write(entry_head)
