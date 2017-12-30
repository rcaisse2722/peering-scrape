#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

print 'Starting script...'

# page to scrape
scrape_page = 'https://www.peeringdb.com/'

# number of seconds in 15 minutes...
interval = 900

# query the website and return the html to the variable page
page = urllib2.urlopen(scrape_page)

# parse it out...
parsed_data = BeautifulSoup(page, 'html.parser')

# get the div that encompasses data we care about
parent_tag = parsed_data.find('h4', text='NETWORKS').parent

# iterate through children
children = parent_tag.findChildren()
for child in children:
    print child