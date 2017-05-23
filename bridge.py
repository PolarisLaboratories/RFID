#!/usr/bin/env python

import serial
import sys
import atexit
import threading
import requests

tags = []

class Tag:
    def __init__(self, id):
        self.rooms = {}
        self.id = id
    def __eq__(self, other):
        return self.id == other.id

def do_update():
    for tag in tags:
        highest_room = ""
        highest_value = 0
        for key,value in tag.rooms.iteritems():
            if value > highest_value:
                highest_value = value
                highest_room = key
        print tag.id, "probably in", highest_room
        url = "https://paladin.polarislabs.io/users/tag/{0}/location/{1}".format(tag.id, highest_room)
        r = requests.post(url)
        print r.status_code
    threading.Timer(300, do_update).start()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'bridge.py <serial port>'
        sys.exit()
    try:
        ser = serial.Serial(sys.argv[1])
    except serial.SerialException as e:
        print 'An error occurred while opening the serial port'
        sys.exit(1)
        ser.close();
    do_update()
    while 1:
        data = ser.readline()
        tag_data = data.split(",")
        found = False
        for tag in tags:
            if tag.id == tag_data[0]:
                tag.rooms[tag_data[1]] = int(tag_data[2])
                found = True;
        if found == False:
            print "Tag not found, creating..."
            tag = Tag(tag_data[0])
            tags.append(tag)
