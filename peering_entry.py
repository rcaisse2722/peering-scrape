#!/usr/bin/env python

from datetime import datetime

class PeeringEntry:
    timestamp = datetime.min

    def __init__(self, participant, timestamp):
        self.timestamp = timestamp
        self.participant = participant

class Participant:
    name = ''
    id = ''
    url = ''

    def __init__(self, name, id, url):
        self.name = name
        self.id = id
        self.url = url