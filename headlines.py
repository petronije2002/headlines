#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:39:23 2018

@author: Pera
"""

from flask import Flask
import feedparser
from flask import render_template
from flask import request

app = Flask(__name__)

rss_feed = {'info': 'http://www.b92.net/info/rss/vesti.xml',
            'sport': 'http://www.b92.net/info/rss/sport.xml',
            'travel': 'http://www.b92.net/info/rss/putovanja.xml '}


@app.route('/',methods=['GET','POST'])
def get_news():
    query = request.form.get("publication")
    if not query or query.lower() not in rss_feed:
        publication = 'info'
    else:
        publication = query.lower()
    feed = feedparser.parse(rss_feed[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
