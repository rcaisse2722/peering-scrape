#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup
from peering_entry import PeeringEntry

print 'Starting script...'

# page to scrape
scrape_page = 'https://www.peeringdb.com'

# number of seconds in 15 minutes...
interval = 900

# query the website and return the html to the variable page
# UNCOMMENT TO GRAB ACTUAL DATA
# page = urllib2.urlopen(scrape_page)

with open('sample_data.html', 'r') as testFile:
    page = testFile.read();

# parse it out...
parsed_data = BeautifulSoup(page, 'html.parser')

# get the div that encompasses data we care about
parent_tag = parsed_data.find('h4', text='NETWORKS').parent

participants = parent_tag.find_all("div", { "class" : "participant"})
ages = parent_tag.find_all("div", { "class" : "age" })

if len(participants) != len(ages):
    print "Length of participants {} does not match length of ages {}".format(len(participants), len(ages))

with open('output.csv', 'w') as outputfile:
    for i in range(0, len(participants)):
        outputfile.writelines("{},{}".format(participants[i], ages[i]))


# iterate through children
# children = parent_tag.findChildren()
#for child in children:
#    print child