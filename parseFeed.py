import feedparser
import time

f = feedparser.parse('http://cepr.net/publications/reports/feed/rss')

if f.updated >= time.strftime('%x'):
    # grab pubDate
    pubDate = str(f.entries[0].published_parsed.tm_year) + "-" + str(f.entries[0].published_parsed.tm_mon)
    # grab title
    title = f.entries[0].title
    # grab author names
    authors = f.entries[0].author
    # find names between parentheses
    m = re.search('\(([^)]+)\)', authors)
    # remove 'and'
    authors_string = m.group(1).replace("and","")
    # convert to list
    authors.list = authors_string.split()
    # use length of list to loop and create individual author-name entries

# append details to file

# with open("", "a") as myfile:
#     myfile.write("appended text")