#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup
from peering_entry import PeeringEntry
from peering_entry import Participant
from datetime import datetime, timedelta

''' 
    Parse HTML tag that represents participant
    Args: tag
    Return: participant object
'''
def parseParticipant(tag):

    if tag is None:
        raise ValueError("Participant tag is NULL")

    name = tag.find("a").string
    url = "{}{}".format(scrape_page, tag.find("a")["href"])
    id = tag.contents[2]
    id = id[id.find("(") + 1:id.find(")")]
    return Participant(name, id, url)


''' 
    Parse HTML tag that represents age
    Args: tag
    Return: timestamp
'''
def parseAge(tag):
    if tag is None:
        raise ValueError("Age tag is NULL")

    now = datetime.now()
    delta = 0

    if "minutes" in tag.string:
        delta = int(tag.string.split("minutes")[0])
    elif "hours" in tag.string:
        delta = int(tag.string.split("hours")[0]) * 60
    else:
        raise ValueError("Failed to parse age: {}".format(tag.string))

    return now - timedelta(minutes=delta)


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

entries = [] # list of PeeringEntry

with open('output.csv', 'w') as outputfile:
    for i in range(0, len(participants)):

        # TODO Add error checking for index out bounds, etc
        #name = participants[i].find("a").string
        #url = "{}{}".format(scrape_page, participants[i].find("a")["href"])
        #id = participants[i].contents[2]
        #id = id[id.find("(") + 1:id.find(")")]
        entry = PeeringEntry(parseParticipant(participants[i]), parseAge(ages[i]))
        entries.append(entry)

        outputfile.writelines("{},{},{},{}\n".format(
            entry.participant.name, entry.participant.id, entry.participant.url, entry.timestamp))