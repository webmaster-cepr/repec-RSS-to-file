import feedparser
from datetime import datetime
import time
import re
import textwrap

f = feedparser.parse('http://cepr.net/publications/reports/feed/rss')

# can't use feed build date, so looping through entries for current reports
# FOR TESTING PURPOSES
today = "3-24-2016"
# today = time.strftime('%m-%d-%Y')
# convert month to absolute value to compare to feed dates
# today = str(abs(int(today[0:2]))) + today[2:]

# BEGIN LOOP
for x in f.entries:
    entry_date = str(x.published_parsed.tm_mon) + "-" + str(x.published_parsed.tm_mday) + "-" + str(x.published_parsed.tm_year)
    if entry_date == today:
        # grab pubDate
        pubDate = str(x.published_parsed.tm_year) + "-" + str(x.published_parsed.tm_mon)
        # grab title
        title = x.title
        # grab author names
        authors = x.author
        # find names between parentheses
        m = re.search('\(([^)]+)\)', authors)
        # remove 'and'
        authors_string = m.group(1).replace("and", ",")
        # convert to list
        authors_list = authors_string.split(',')
        # abstract
        # NOTE THIS IS NOT PULLING THE ACTUAL DESCRIPTION - NEEDS WORK
        abstract = x.description
        # use length of list to loop and create individual author-name entries
        #details
        entry_head = textwrap.dedent("""\
            \n
            Template-Type: ReDif-Paper 1.0
            Handle: RePEc:epo:papers:""" + pubDate)
        # append details to file
        with open(time.strftime("%Y") + "-test.rdf", "a") as repec_file:
            repec_file.write(entry_head)
            # need for loop here
            repec_file.write("\nAuthor-Name:" + authors_list[0])
