#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://developers.google.com/appengine/docs/python/config/cron

import urllib
import hashlib

sites = \
    ['http://www.liceoclassicoforli.it/prova/viewnews.asp?newsID=408',
     'http://www.liceocalboli.org/Istituto/bandi.htm',
     'http://www.agrariocesena.it/new/index.php?option=com_docman&view=docman&Itemid=489'
     ]


def getMd5(url):
    return hashlib.md5(urllib.urlopen(url).read()).hexdigest()


if __name__ == '__main__':
    for site in sites:
        print getMd5(site)
