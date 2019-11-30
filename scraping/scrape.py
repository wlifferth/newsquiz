#!/usr/bin/python3
import argparse
import logging
import feedparser
import sys

from pprint import pprint

sys.path.append('../')

from parsers.nyt_parser import parse as nyt_parse
from parsers import parse_errors 

NYT_RSS_ADDRESS = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'


def scrape(source_rss_uri=None, source_file_path=None, write_function=print):
    l = logging.getLogger('parselog')
    if source_rss_uri:
        feed = feedparser.parse(source_rss_uri)
    elif source_file_path:
        feed = feedparser.parse(open(source_file_path, 'rb'))

    for item in feed['items']:
        try:
            write_function(nyt_parse(item))
            l.info('Successful parse.')
        except Exception as e:
            l.info('Failed parse: {}\n\n{}'.format(e, str(item)))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--source_rss_uri', default=NYT_RSS_ADDRESS)
    argparser.add_argument('--source_file_path')
    args = argparser.parse_args()
    if args.source_file_path:
        scrape(source_file_path=args.source_file_path)
    else:
        scrape(source_rss_uri=args.source_rss_uri)
