#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import sys
import codecs
from collections import OrderedDict
from cStringIO import StringIO
import scraperwiki
from dateutil.parser import parse as parse_date
from flickrapi import FlickrAPI, shorturl
import scraperwiki

API_KEY = "8812d02940ff6669b30904b807ecc49b"
flickr = FlickrAPI(API_KEY)


UNIQUE_KEYS = ['id']


def main():
    favs = flickr.walk(tags="kittens", extras="geo")
    for photo in favs:
        if photo.get('latitude') != '0':
            print photo.get('title')
            title = photo.get('title')
            print photo.get('latitude')
            latitude = float(photo.get('latitude'))
            print photo.get('longitude')
            longitude = float(photo.get('longitude'))
            print photo.get('id')
            identity = photo.get('id')
            print shorturl.url(photo.get('id'))
            url = shorturl.url(photo.get('id'))
            submit_to_scraperwiki(identity, title, latitude, longitude, url)

    scraperwiki.status('ok', "OK")

def submit_to_scraperwiki(identity, title, latitude, longitude, url):
    result = {"id" : identity, "title" : title, "latitude" : latitude, "longitude" : longitude, "url" : url}
    scraperwiki.sqlite.save(UNIQUE_KEYS, result, 'kittens')

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main()
