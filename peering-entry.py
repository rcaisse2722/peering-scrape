#!/usr/bin/env python

from datetime import datetime


class PeeringEntry:
    timestamp = datetime.min
    name = ''
    id = ''

    def __init__(self, name, id):
        self.name = name
        self.id = id