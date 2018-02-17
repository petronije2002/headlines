#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:39:23 2018

@author: Pera
"""

from flask import Flask
import feedparser

b92_feed = 'http://www.b92.net/info/rss/vesti.xml'

app = Flask(__name__)
rss_feed = {'info': 'http://www.b92.net/info/rss/vesti.xml',
            'sport': 'http://www.b92.net/info/rss/sport.xml',
            'travel': 'http://www.b92.net/info/rss/putovanja.xml '}


@app.route('/')
@app.route('/<publication>')
def get_news(publication='info'):
    feed = feedparser.parse(rss_feed[publication])
    first_article = feed['entries'][0]
    return """<html>
       <body>
           <h1> {0} </h1>
           <b>{1}</b> <br/>
           <i>{2}</i> <br/>
           <p>{3}</p> <br/>
       </body>
   </html>""".format(publication,
                     first_article.get("title"),
                     first_article.get("published"),
                     first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
